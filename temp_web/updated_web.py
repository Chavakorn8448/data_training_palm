
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from PIL import Image, ImageEnhance
import torch
import os

# Initialize Flask app
app = Flask(__name__)

# Path to save uploaded images
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Path to YOLO model
MODEL_PATH = 'C:/Users/ChavakornArunkunarax/Documents/data_training_palm/yolov8n.pt'

# Load YOLO model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH)

# Image processing functions
def resize_and_crop_image(img, target_pixels=8e6):
    width, height = img.size
    aspect_ratio = width / height
    new_width = int((target_pixels * aspect_ratio) ** 0.5)
    new_height = int(new_width / aspect_ratio)
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    return img_resized

def enhance_exposure(img, exposure_factor=1.5):
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(exposure_factor)
    return enhanced_img

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            img = Image.open(filename)

            # Process the image
            img_resized = resize_and_crop_image(img)
            img_enhanced = enhance_exposure(img_resized)

            # Save processed image
            processed_filename = os.path.join(UPLOAD_FOLDER, 'processed_' + file.filename)
            img_enhanced.save(processed_filename)

            # Run YOLO model on the processed image
            results = model(processed_filename)
            results.save(UPLOAD_FOLDER)

            # Redirect to the annotated image display page
            return redirect(url_for('display_image', filename='processed_' + file.filename))

    return render_template('upload.html')

@app.route('/display/<filename>')
def display_image(filename):
    return render_template('display.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

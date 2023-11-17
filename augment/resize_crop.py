import os
from tkinter import Tk, filedialog, Button, Label
from PIL import Image

def resize_and_crop_image(img_path, output_folder):
    # Resize to 8MP
    target_pixels = 8e6
    with Image.open(img_path) as img:
        width, height = img.size
        aspect_ratio = width / height
        new_width = int((target_pixels * aspect_ratio) ** 0.5)
        new_height = int(new_width / aspect_ratio)
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)

        # Crop
        new_width, new_height = img_resized.size
        new_dimension = min(new_width, new_height) / 2
        left, top = (new_width - new_dimension) / 2, (new_height - new_dimension) / 2
        right, bottom = (new_width + new_dimension) / 2, (new_height + new_dimension) / 2
        img_cropped = img_resized.crop((left, top, right, bottom))

        output_path = os.path.join(output_folder, os.path.basename(img_path))
        img_cropped.save(output_path)

def process_images(folder_path):
    if not folder_path:
        return

    output_folder = os.path.join(folder_path, "Processed_Images")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            try:
                resize_and_crop_image(file_path, output_folder)
                status_label.config(text=f"Processed: {filename}")
            except Exception as e:
                status_label.config(text=f"Error with {filename}: {str(e)}")
                continue

    status_label.config(text="All images processed successfully!")

root = Tk()
root.title("Image Resizing and Cropping Tool")

instructions = Label(root, text="Select a folder to resize and crop all its images")
instructions.pack(pady=20)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    process_images(folder_path)

browse_btn = Button(root, text="Browse Folder", command=select_folder)
browse_btn.pack(pady=20)

status_label = Label(root, text="")
status_label.pack(pady=20)

root.mainloop()

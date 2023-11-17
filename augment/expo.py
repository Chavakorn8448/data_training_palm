import os
from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageEnhance

def enhance_exposure(img_path, output_folder, exposure_factor=1.5):
    with Image.open(img_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        enhanced_img = enhancer.enhance(exposure_factor)
        enhanced_img.save(os.path.join(output_folder, os.path.basename(img_path)))

def process_images(folder_path):
    if not folder_path:
        return

    output_folder = os.path.join(folder_path, "Enhanced_Exposure")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            try:
                enhance_exposure(file_path, output_folder)
                status_label.config(text=f"Enhanced: {filename}")
            except Exception as e:
                status_label.config(text=f"Error with {filename}: {str(e)}")
                continue

    status_label.config(text="All images enhanced successfully!")

root = Tk()
root.title("Enhance Exposure of Images")

instructions = Label(root, text="Select a folder to enhance exposure of all its images")
instructions.pack(pady=20)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    process_images(folder_path)

browse_btn = Button(root, text="Browse Folder", command=select_folder)
browse_btn.pack(pady=20)

status_label = Label(root, text="")
status_label.pack(pady=20)

root.mainloop()

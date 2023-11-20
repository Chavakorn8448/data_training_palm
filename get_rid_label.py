import os
import shutil

# Set the paths to the folders containing the .jpg and .txt files
jpg_folder = 'online_data/images_valid'
txt_folder = 'Kematangan-TBS-sawit-7/valid/labels'

# Get the list of .jpg files
jpg_files = [os.path.splitext(filename)[0] for filename in os.listdir(jpg_folder) if filename.lower().endswith('.jpg')]

# Iterate through the .txt files and check if their names are in the list of .jpg files
for txt_filename in os.listdir(txt_folder):
    if txt_filename.lower().endswith('.txt'):
        txt_file_base = os.path.splitext(txt_filename)[0]
        if txt_file_base in jpg_files:
            txt_file_path = os.path.join(txt_folder, txt_filename)
            new_txt_folder = 'online_data/labels_valid'  # Replace with the destination folder for the .txt files you want to keep
            new_txt_file_path = os.path.join(new_txt_folder, txt_filename)
            shutil.copy(txt_file_path, new_txt_file_path)

print("Operation completed.")

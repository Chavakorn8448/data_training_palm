from PIL import Image, ImageEnhance
import os

def adjust_exposure(input_folder, output_folder, factor=1.5):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Open the image using Pillow
        image = Image.open(input_path)

        # Adjust the exposure
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(factor)

        # Save the adjusted image to the output folder
        print("add")
        enhanced_image.save(output_path)

if __name__ == "__main__":
    input_folder = "data_set/new_test_set/almostripe"  # Replace with the path to your input folder
    output_folder = "data_set/new_test_set/expo_almostripe"  # Replace with the path to your output folder
    exposure_factor = 1.5  # Adjust this value to control exposure (1.0 means no change)

    adjust_exposure(input_folder, output_folder, exposure_factor)

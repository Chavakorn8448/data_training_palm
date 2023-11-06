import os
import cv2

image_folder = "ripe"  # Replace with the path to your image folder
output_folder = "ripe"  # Replace with the path where you want to save the annotation files

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all image files in the image folder
image_files = [filename for filename in os.listdir(image_folder) if filename.lower().endswith((".jpg", ".jpeg", ".png"))]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Get image dimensions
    height, width, _ = image.shape
    
    # Create an annotation file path based on the image filename
    annotation_filename = os.path.splitext(image_file)[0] + ".txt"
    annotation_path = os.path.join(output_folder, annotation_filename)
    
    # Create or open the annotation file and write the bounding box coordinates
    with open(annotation_path, "w") as annotation_file:
        # Write a sample bounding box (adjust coordinates as needed)
        x1, y1, x2, y2 = 50, 50, 150, 150  # Example coordinates
        annotation = f"0 {x1/width} {y1/height} {x2/width} {y2/height}\n"
        annotation_file.write(annotation)

print("Annotation files generated.")

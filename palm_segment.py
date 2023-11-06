import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained Faster R-CNN model for oil palm fruit detection
model = fasterrcnn_resnet50_fpn(pretrained=False)  # Set `pretrained` to False to load a custom model
model.load_state_dict(torch.load("oil_palm_model.pth"))  # Load your pre-trained model

# Set the model to evaluation mode
model.eval()

# Define class labels (if applicable)
class_labels = ["background", "oil_palm_fruit"]

# Load an input image for detection
input_image = Image.open("25_4.jpg")  # Replace with the path to your input image

# Transform the input image to a PyTorch tensor
input_tensor = F.to_tensor(input_image)
input_tensor = input_tensor.unsqueeze(0)  # Add a batch dimension

# Perform inference
with torch.no_grad():
    predictions = model(input_tensor)

# Extract detected objects, bounding boxes, and scores
boxes = predictions[0]["boxes"]
scores = predictions[0]["scores"]
labels = predictions[0]["labels"]

# Set a detection threshold (adjust as needed)
detection_threshold = 0.5

# Filter detections based on the detection threshold
filtered_boxes = boxes[scores > detection_threshold]
filtered_labels = labels[scores > detection_threshold]

# Convert the input image to a NumPy array for visualization
input_image_np = F.to_pil_image(input_tensor[0])

# Visualize the detected oil palm fruits
plt.figure(figsize=(10, 6))
plt.imshow(input_image_np)

for box, label in zip(filtered_boxes, filtered_labels):
    box = [round(float(coord), 2) for coord in box.tolist()]
    label_name = class_labels[label]
    plt.gca().add_patch(plt.Rectangle(
        (box[0], box[1]), box[2] - box[0], box[3] - box[1], fill=False, color="green", linewidth=2))
    plt.text(box[0], box[1], f"{label_name}", fontsize=12, color="white")

plt.axis("off")
plt.show()
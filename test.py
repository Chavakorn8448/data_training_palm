import cv2

# Function to annotate an image with bounding boxes and save it
def annotate_image(image_path, annotations_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    clone = image.copy()

    # Create an empty list to store bounding box coordinates
    bounding_boxes = []

    # Callback function for mouse events
    def draw_rectangle(event, x, y, flags, param):
        nonlocal bounding_boxes

        if event == cv2.EVENT_LBUTTONDOWN:
            bounding_boxes.append((x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            if len(bounding_boxes) == 1:
                x0, y0 = bounding_boxes[0]
                x1, y1 = x, y
                cv2.rectangle(clone, (x0, y0), (x1, y1), (0, 255, 0), 2)
                bounding_boxes[-1] = (x0, y0, x1, y1)
            cv2.imshow("Annotate Image", clone)

    # Create a window and set the mouse event callback
    cv2.namedWindow("Annotate Image")
    cv2.setMouseCallback("Annotate Image", draw_rectangle)

    # Display the image and wait for user interaction
    cv2.imshow("Annotate Image", clone)
    cv2.waitKey(0)

    # Save the bounding box annotations
    with open(annotations_path, "w") as file:
        for box in bounding_boxes:
            file.write(f"{box[0]},{box[1]},{box[2]},{box[3]}\n")

    # Draw bounding boxes on the image and save it
    for box in bounding_boxes:
        x0, y0, x1, y1 = box
        cv2.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 2)

    cv2.imwrite(output_path, image)

    # Close the window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "25_4.jpg"  # Replace with the path to your image
    annotations_path = "annotations.txt"  # Replace with the annotations file path
    output_path = "annotated_image.jpg"  # Replace with the desired output image path

    annotate_image(image_path, annotations_path, output_path)

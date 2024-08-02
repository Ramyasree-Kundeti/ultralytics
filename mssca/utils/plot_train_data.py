import matplotlib.pyplot as plt
import cv2

# Function to read bounding boxes from file
def read_bounding_boxes(file_path):
    boxes = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center = float(parts[1])
            y_center = float(parts[2])
            width = float(parts[3])
            height = float(parts[4])
            boxes.append((class_id, x_center, y_center, width, height))
    return boxes

# Convert normalized coordinates to absolute pixel coordinates
def convert_to_absolute(image_shape, box):
    class_id, x_center, y_center, width, height = box
    image_height, image_width = image_shape[:2]
    x1 = (x_center - width / 2) * image_width
    y1 = (y_center - height / 2) * image_height
    x2 = (x_center + width / 2) * image_width
    y2 = (y_center + height / 2) * image_height
    return class_id, x1, y1, x2, y2

# Load an image
image_path = r'C:\uni\thesis\code\amsterdam_00000.png'  # Use raw string or double backslashes
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Read bounding boxes from file
bounding_boxes_file = r'C:\uni\thesis\code\amsterdam_00000.txt'  # Use raw string or double backslashes
boxes = read_bounding_boxes(bounding_boxes_file)

# Define class names (for COCO dataset or your custom dataset)
class_names = ['person-group-far-away','rider+vehicle-group-far-away','rider','bicycle','bicycle-group','pedestrian','scooter-group','motorbike-group','tricycle-group','motorbike','scooter','buggy-group','tricycle','buggy','co-rider','wheelchair','wheelchair-group']
# Plot the image
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
ax = plt.gca()

# Plot each bounding box
for box in boxes:
    class_id, x1, y1, x2, y2 = convert_to_absolute(image_rgb.shape, box)
    width, height = x2 - x1, y2 - y1
    rect = plt.Rectangle((x1, y1), width, height, edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(rect)
    label = f'{class_names[class_id]}'
    plt.text(x1, y1, label, color='white', fontsize=12, bbox=dict(facecolor='red', edgecolor='none', pad=0))

plt.axis('off')
plt.show()

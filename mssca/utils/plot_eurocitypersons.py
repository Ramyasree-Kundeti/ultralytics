import json
import matplotlib.pyplot as plt
import cv2

# Load JSON annotations
def load_annotations(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
        img_width = data['imagewidth']
        img_height = data['imageheight']
    return img_width,img_height,data['children']

# Plot bounding boxes
def plot_bounding_boxes(image_path, img_width,img_height,annotations, class_names):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 8))
    plt.imshow(image_rgb)
    ax = plt.gca()

    for annotation in annotations:
        class_id = annotation['identity']
        x0 = annotation['x0']
        y0 = annotation['y0']
        x1 = annotation['x1']
        y1 = annotation['y1']
        width, height = x1 - x0, y1 - y0
        rect = plt.Rectangle((x1, y1), width, height, edgecolor='red', facecolor='none', linewidth=2)
        ax.add_patch(rect)
        label = [class_id]
        plt.text(x1, y1, label, color='white', fontsize=12, bbox=dict(facecolor='red', edgecolor='none', pad=0))

    plt.axis('off')
    plt.show()

# Path to the image and JSON annotation file
image_path = r'C:\uni\thesis\code\amsterdam_00000.png'
json_path = r'C:\uni\thesis\code\amsterdam_00000.json'

# Define class names (example for EuroCity Persons dataset)
class_names = ['person-group-far-away','rider+vehicle-group-far-away','rider','bicycle','bicycle-group','pedestrian','scooter-group','motorbike-group','tricycle-group','motorbike','scooter','buggy-group','tricycle','buggy','co-rider','wheelchair','wheelchair-group']

# Load annotations and plot
img_width,img_height,annotations = load_annotations(json_path)
plot_bounding_boxes(image_path, img_width,img_height,annotations, class_names)

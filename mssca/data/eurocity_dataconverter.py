import json
import os


def process_object(obj, results,classid,img_width, img_height):
    # Extract required information from the current object
    x_center = (obj['x0'] + obj['x1']) / 2.0 / img_width
    y_center = (obj['y0'] + obj['y1']) / 2.0 / img_height
    width = (obj['x1'] - obj['x0']) / img_width
    height = (obj['y1'] - obj['y0']) / img_height
    class_id = obj['identity']
    classid.append(f"{class_id}")
    if class_id in class_mappings:
        class_id = class_mappings[class_id]
    results.append(f"{class_id} {x_center} {y_center} {width} {height}")
    # Check if there are children and process them recursively
    if 'children' in obj:
        for child in obj['children']:
            process_object(child, results,classid,img_width, img_height)


def extract_data(data):
    img_width = data['imagewidth']
    img_height = data['imageheight']
    results = []
    classid = []
    if 'children' in data:
        for obj in data['children']:
            process_object(obj, results,classid,img_width, img_height)
    return results, classid


# Example usage
input_dir = input_dir = r'C:\uni\thesis\eurocitypersons_converter\ECP_day_labels_train\ECP\day\labels\valjson'  # Update this path to your JSON file location
output_dir = r'C:\uni\thesis\eurocitypersons_converter\ECP_day_labels_train\ECP\day\labels\val'  # Path to save the output JSON


os.makedirs(output_dir, exist_ok=True)
existing_lines = set()
class_mappings = {"person-group-far-away":0,
"rider+vehicle-group-far-away":1,
"rider":2,
"bicycle":3,
"bicycle-group":4,
"pedestrian":5,
"scooter-group":6,
"motorbike-group":7,
"tricycle-group":8,
"motorbike":9,
"scooter":10,
"buggy-group":11,
"tricycle":12,
"buggy":13,
"co-rider":14,
"wheelchair":15,
"wheelchair-group":16}

for annotation_file in os.listdir(input_dir):
    if annotation_file.endswith('.json'):
        annotationpath = os.path.join(input_dir, annotation_file)
        outputpath = os.path.join(output_dir, annotation_file.replace('.json', '.txt'))
        classidpath = os.path.join(output_dir+'\class\classid.txt')
        print(classidpath)
        print("annotationpath",annotationpath)
        with open(annotationpath, 'r') as file:
            data = json.load(file)
            results,classid = extract_data(data)
            print(results)
            print(classid)
        with open(outputpath, 'w') as out_file:
            for line in results:
                out_file.write(line + '\n')
        with open(classidpath, 'r') as class_file:
            print(classidpath)
            for line in class_file:
                existing_lines.add(line.strip())
        with open(classidpath, 'a') as class_file:
            for line in classid:
                line = line.strip()  # Remove leading/trailing whitespace
                if line not in existing_lines:
                    # If the line is not a duplicate, write it to the file
                    class_file.write(line + '\n')
                    # Add the line to the set of written lines
                    existing_lines.add(line)
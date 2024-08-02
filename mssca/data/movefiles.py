import os
import shutil

def move_files_to_destination(source_dir, destination_dir):
    print("Then here")
    # Walk through all directories and subdirectories
    for root, _, files in os.walk(source_dir):
        print("Here")
        for file_name in files:
            # Get the full path of the file
            source_file_path = os.path.join(root, file_name)
            # Construct the destination file path
            destination_file_path = os.path.join(destination_dir, file_name)
            try:
                # Move the file to the destination directory
                shutil.move(source_file_path, destination_file_path)
                print(f'Moved {source_file_path} to {destination_file_path}')
            except Exception as e:
                print(f'Error moving {source_file_path}: {e}')
print("Start")
# Example usage:
source_directory = '/media/homes/kundeti/yolomssca/datasets/eurocitypersons/ECP/day/img/val'
destination_directory = '/media/homes/kundeti/yolomssca/datasets/eurocitypersons/ECP/day/val/images'

move_files_to_destination(source_directory, destination_directory)

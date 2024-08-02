import time

from ultralytics import YOLO

print("Executing YOLOv8 model with EuroCityPersons dataset")
#Load and build a new model
model = YOLO("yolov8x.yaml")
#use the model
start_time = time.time()
results = model.train(data="data.yaml",epochs=100,show=True)
print('Training Completed')
end_time = time.time()
print(f'Training- Average Epoch Duration: {(end_time - start_time)/100:.2f} seconds')
print(f'Estimated Total Training Time for 100 epochs: {end_time - start_time:.2f} seconds')
print('Validation Started')
start_time1 = time.time()
results1 = model.eval()
end_time1 = time.time()
print(f'Validation- Average Epoch Duration: {(end_time1 - start_time1)/100:.2f} seconds')
print(f'Estimated Total Validation Time for 100 epochs: {end_time1 - start_time1:.2f} seconds')
print('Validation Completed')
print(f'Total execution time: {(end_time1 - start_time):.2f} seconds')


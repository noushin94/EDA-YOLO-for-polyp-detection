import cv2
from ultralytics import YOLO
# Set the number of epochs for training
EPOCHS = 65

# Define the model and other parameters
model = YOLO("yolov8n.yaml")  # Ensure this path is correct
img_size = 640
data_config = '/Users/noushinahmadvand/Downloads/YOLO/data.yaml'  # Adjust the path to your data.yaml
batch_size = 4
experiment_name = 'yolov8l_v8_scratch'
learning_rate = 0.01



# Train the model using the specified parameters
model.train(
    data=data_config,
    epochs=EPOCHS,
    imgsz=img_size,
    batch=batch_size,
    name=experiment_name,
    lr0=learning_rate
)
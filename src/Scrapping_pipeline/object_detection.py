import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Run inference on an image
results = model('data/images/sample_image.jpg')

# Show results
results.show()

# Save results
results.save('data/images/results/')

YOLOv8 Real-Time Object Detection
This project implements real-time object detection using the Ultralytics YOLOv8 model (Python + OpenCV) to identify and label objects from a live webcam feed on macOS.
Features
	•	Real-time detection with YOLOv8 (choose from nano, small, medium, large, or extra-large models)
	•	Live webcam video processing using OpenCV
	•	Automatic annotation with bounding boxes and class labels
	•	Easily switch to segmentation models or optimize for speed/accuracy
Technologies Used
	•	Python 3.x
	•	Ultralytics YOLOv8
	•	OpenCV
	•	macOS (M1, M2, Intel, or newer)
	•	PyTorch with MPS (for Apple Silicon GPU acceleration, optional)
Usage
	1.Clone this repo:
    git clone https://github.com/<ajayaddada>/yolov8-object-detection.git
    cd yolov8-object-detection
  2.Set up a virtual environment:
    python3 -m venv yolov8-env
    source yolov8-env/bin/activate
  3.Install dependencies:
    pip install ultralytics opencv-python
  4.Run the detection script:
    python realtime_yolov8.py
Real-World Applications
	•	Security and intrusion monitoring
	•	Smart retail analytics (customer or product counting)
	•	Robotics and drone navigation
	•	Medical or agricultural image analysis
	•	Traffic analysis and smart city systems
Notes
	•	Model selection:You can swap  yolov8x.pt  for smaller models ( yolov8l.pt ,  yolov8s.pt , etc.) for faster inference or less resource usage.
	•	Mac Users:Use Apple Silicon’s GPU (M1/M2) with PyTorch MPS backend for improved speed.
	•	Customization:Supports easy switching to segmentation or tracking features.

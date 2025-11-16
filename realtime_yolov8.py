from ultralytics import YOLO
import cv2

def real_time_detection_yolov8l():
    model = YOLO("yolov8l.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, conf=0.4)

        annotated_frame = results[0].plot()
        cv2.imshow("Real-Time YOLOv8l Detection - Press 'q' to Quit", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    real_time_detection_yolov8l()

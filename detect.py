import cv2
from ultralytics import YOLO
from alert import send_alert
from config import CAMERA_SOURCE, CROWD_THRESHOLD

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Start camera
cap = cv2.VideoCapture(CAMERA_SOURCE)

print("Starting Smart Shop Crowd Monitoring...")
print(f"Alert will trigger when people count exceeds {CROWD_THRESHOLD}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not accessible.")
        break

    # Run detection
    results = model(frame)

    people_count = 0

    for result in results:
        for box in result.boxes:
            # Class 0 is person in YOLOv8
            if int(box.cls) == 0:
                people_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show live count on screen
    cv2.putText(
        frame,
        f"People Count: {people_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 0, 255),
        3
    )

    # Trigger alert if threshold exceeded
    if people_count > CROWD_THRESHOLD:
        send_alert(people_count)
        cv2.putText(
            frame,
            "ALERT TRIGGERED",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 0, 255),
            3
        )

    cv2.imshow("Skyline Shop - Crowd Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

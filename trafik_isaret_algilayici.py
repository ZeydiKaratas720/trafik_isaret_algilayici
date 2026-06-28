from ultralytics import YOLO
import cv2
import time

# Modeli yükle
model = YOLO("best.pt")

# Kamera
cap = cv2.VideoCapture(0)

# Kamera çözünürlüğü
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

prev_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Tahmin
    results = model.predict(
        frame,
        imgsz=640,
        conf=0.45,
        verbose=False
    )

    annotated_frame = frame.copy()

    for r in results:

        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            # Kutu çiz
            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

            label = f"{class_name} {confidence:.2f}"

            cv2.putText(
                annotated_frame,
                label,
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

    # FPS hesapla
    current_time = time.time()
    fps = 1/(current_time-prev_time)
    prev_time = current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    cv2.imshow("Traffic Sign Detection", annotated_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
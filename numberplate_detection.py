import cv2

# Load Haar cascade
plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
if plate_cascade.empty():
    raise IOError("Haar cascade XML file not found!")

# Video path
video_path = "Automatic Number Plate Recognition (ANPR) _ Vehicle Number Plate Recognition (1) - Copy.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError("Cannot open video file!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    frame_resized = cv2.resize(frame, (640, 360))
    cv2.imshow("Number Plate Detection", frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
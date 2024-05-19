import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully.")
    while True:
        success, frame = camera.read()
        if success:
            cv2.imshow('Camera Test', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Failed to capture image.")
camera.release()
cv2.destroyAllWindows()

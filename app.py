import cv2
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)
camera = None

def generate_frames():
    global camera
    while True:
        if not camera or not camera.isOpened():
            break
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera')
def start_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
    return jsonify(status="Camera started")

@app.route('/stop_camera')
def stop_camera():
    global camera
    if camera and camera.isOpened():
        camera.release()
    return jsonify(status="Camera stopped")

if __name__ == "__main__":
    app.run(debug=True)

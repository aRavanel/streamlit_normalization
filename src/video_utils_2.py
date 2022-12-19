import cv2
import time
import threading
import numpy as np
import threading
VIDEO_SOURCE = 0

# https://medium.com/@teckyian/building-an-ai-security-camera-with-a-web-ui-in-100-lines-of-code-6d983586a9bf

def resize_keep_aspect(img, req_shape):
    ratio = max((img.shape[1]/req_shape[0], img.shape[0]/req_shape[1]))
    new_h, new_w = int(img.shape[0]/ratio), int(img.shape[1]/ratio)
    img = cv2.resize(img, (new_w, new_h))
    img = cv2.copyMakeBorder(img, 0, (req_shape[1]-new_h), 0, (req_shape[0]-new_w), cv2.BORDER_CONSTANT)
    return img, (req_shape[1]/new_h, req_shape[0]/new_w)

class CameraThread(threading.Thread):
    def __init__(self, name='CameraThread'):
        super().__init__(name=name, daemon=True)
        self.stop_event = False
        self.open_camera()
        self._frame = np.zeros((300,300,3), dtype=np.uint8) #initial empty frame
        self.lock = threading.Lock()

    def open_camera(self):
        self.webcam = cv2.VideoCapture(VIDEO_SOURCE)

    def run(self):
        while not self.stop_event:
            ret, img = self.webcam.read()
            if not ret: #re-open camera if read fails. Useful for looping test videos
                self.open_camera()
                continue
            with self.lock: 
                self._frame = img.copy()

    def stop(self): self.stop_event = True

    def read(self):
        with self.lock: 
            return self._frame.copy()
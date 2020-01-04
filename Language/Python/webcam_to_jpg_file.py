import numpy as np
import cv2
from PIL import Image
import time

def get_webcam_frame():
    cap = cv2.VideoCapture(0)
    time.sleep(1) #because camera needs time starting
    _, frame = cap.read()
    cap.release()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def save_webcam_to_image(name):
    frame = get_webcam_frame()
    Image.fromarray(frame).save(f'{name}.jpg')
    
#pip install opencv-contrib-python
#installing cv2: https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/
#capture video frame: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#capture-video-from-camera

#change bgr to rgb: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
#sleep: https://www.programiz.com/python-programming/time/sleep
#save image from array: https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image

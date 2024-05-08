import cv2
from matplotlib import pyplot as plt
import datetime

# Set the desired resolution
width = 1280
height = 720

# just randomly take photo
now = datetime.datetime.now()
date_time_str = now.strftime("%d%m%Y-%H%M%S")

def take_photo() :
 # camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
 camera = cv2.VideoCapture(0)
 camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
 camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
 ret, frame = camera.read()
 cv2.imwrite(f"{date_time_str}.jpg", frame)
 camera.release()

take_photo()

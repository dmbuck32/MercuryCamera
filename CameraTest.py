#!/usr/bin/python3
import numpy as np
import cv2

cam = cv2.VideoCapture(0)
while True:
	ret_val, img = cam.read()
	cv2.imshow('my webcam', img)
	if cv2.waitKey(1) == 27: 
		break  # esc to quit
cv2.destroyAllWindows()

import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt

import uuid
import os
import time

##########################################################################

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolo/runs/train/exp/weights/best.pt', force_reload=True)

img = './data/images/train/IMG20220811133825.jpg'

pred = model(img)

pred.print()
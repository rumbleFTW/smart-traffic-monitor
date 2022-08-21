#!/bin/bash

FILE="$1"

cd yolo && python traffic-monitor.py --source "$FILE" --weights 'runs/train/exp/weights/best.pt'  --save-crop && cd .. && python ./main.py 
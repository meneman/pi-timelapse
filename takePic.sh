#!/bin/bash


DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x1024 -s 2
fswebcam -r 1280x1024 --fps 15 -S 30 --no-banner ./pics/$DATE.jpg
convert ./pics/$DATE.jpg -quality 80% -gamma 1.10,1.05,1.0 ./pics/$DATE.jpg
echo $DATE

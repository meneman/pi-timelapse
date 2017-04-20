#!/bin/bash


DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1920x1080 -s 2
fswebcam -r 1920x1080 -S 100 --no-banner /home/pi/pics/$DATE.jpg
convert $DATE.jpg -resize '1024x1024' -quality 80% -gamma 1.10,1.05,1.0 $DATE.jpg
echo $DATE

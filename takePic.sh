#!/bin/bash


DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1920x1080 -s 2 
fswebcam -r 1920x1080 -S 15 --no-banner /home/pi/pics/$DATE.jpg

echo $DATE

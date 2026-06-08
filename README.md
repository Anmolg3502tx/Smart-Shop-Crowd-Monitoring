# Smart Shop Crowd Monitoring and Alert System

This is a real-time system that uses intelligence to monitor the crowd in retail shops. It uses computer vision to count the number of customers inside the shop via CCTV cameras.. Sends a mobile alert when the crowd gets too big.

> I built this system when I was an intern at Radhe Krishn Enterprises. The problem was simple. Shop owners did not have a way to know when their shop was getting too crowded during peak hours or sale days.

## Why I Built This System

retail shops do not have staff to watch camera feeds all day. During festivals or weekends the shops get overcrowded. Which is bad for customers and bad for business. I wanted to fix this problem with something that's lightweight and affordable.

## What This System Does

This system plugs into any existing CCTV setup counts people in time using YOLOv8 and sends an instant alert to the shop owners phone when the crowd crosses a certain limit.

## Features of This System

- This system detects people in time using YOLOv8

- It shows the live count of people on the screen

- It sends an instant alert to the shop owners phone when the crowd exceeds the threshold

- It has a 5-minute cooldown period so that alerts do not spam

- The threshold is adjustable. It is set to 10 people by default

- This system works with both USB and IP/RTSP cameras

## Technical Details of This System

| Tool | Purpose |

|------|---------|

| YOLOv8 (Ultralytics) | Person detection

OpenCV | Video capture and frame processing

| Python | Core logic

| Telegram Bot API | Mobile alerts

NumPy | Frame array handling

## How This System Works

1. The camera feed is captured frame by frame via OpenCV

2. YOLOv8 runs on each frame. Detects all people

3. Bounding boxes are. The live count is shown on the screen

4. If the count exceeds the threshold. A Telegram alert is sent to the owner

5. A cooldown timer prevents repeated alerts

## Sample Output of This System

![Demo](assets/demo.png)

*11 people detected. Alert triggered*

## Run This System

```bash

git clone https://github.com/yourusername/Smart-Shop-Crowd-Monitoring

cd Smart-Shop-Crowd-Monitoring

pip install -r requirements.txt

python detect.py

```

## Built By

**Anmol Gupta**. CSE (AI & ML) KR Mangalam University

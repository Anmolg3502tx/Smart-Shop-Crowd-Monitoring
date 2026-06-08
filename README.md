# Smart Shop Crowd Monitoring and Alert System

A real-time system that uses AI to monitor crowd levels in retail shops. It uses computer vision to count customers inside the shop via CCTV cameras and sends a mobile alert when the crowd gets too big.

> I built this during my internship at Radhe Krishn Enterprises. The problem was simple — shop owners had no way to know when their shop was getting too crowded during peak hours or sale days.

## Why I Built This

Small retail shops do not have dedicated staff watching camera feeds all day. During festivals or weekends, shops get overcrowded silently. That is bad for customers and bad for business. I wanted to fix this with something lightweight and affordable.

## What It Does

This system plugs into any existing CCTV setup, counts people in real time using YOLOv8, and sends an instant alert to the shop owner's phone when the crowd crosses a set limit.

## Features

- Detects people in real time using YOLOv8
- Shows live footfall count on screen
- Sends instant Telegram alert when crowd exceeds threshold
- 5-minute cooldown so alerts do not spam
- Threshold is adjustable. Default is set to 10 people
- Works with both USB and IP/RTSP cameras

## Tech Stack

| Tool | Purpose |
|------|---------|
| YOLOv8 (Ultralytics) | Person detection |
| OpenCV | Video capture and frame processing |
| Python | Core logic |
| Telegram Bot API | Mobile alerts |
| NumPy | Frame array handling |

## How It Works

1. Camera feed is captured frame by frame via OpenCV.
2. YOLOv8 runs on each frame and detects all persons.
3. Bounding boxes are drawn and live count is shown on screen.
4. If count exceeds threshold, a Telegram alert is sent to the owner.
5. Cooldown timer prevents repeated alerts.

## Sample Output



![Demo](assets/demo.png)


*11 people detected. Alert triggered.*

## Run It

```bash
git clone https://github.com/yourusername/Smart-Shop-Crowd-Monitoring
cd Smart-Shop-Crowd-Monitoring
pip install -r requirements.txt
python detect.py

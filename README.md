# Smart Shop Crowd Monitoring and Alert System

A real-time AI-powered crowd monitoring system that helps shop owners track customer footfall via CCTV and get instant mobile alerts when the crowd gets too high.

I originally built this for my father's shop, Skyline Shop in Badarpur, Delhi. It is a busy local shop offering services like photostat, printouts, passport size photos, Aadhaar card, PAN card, online forms, money transfer, recharges, confectionery and more. Since our house is nearby, I wanted a way to know when the shop gets crowded so my father is not overwhelmed alone. After building it, I realized any shop owner could use this to track customer engagement and peak hours so I made it general purpose.


## Why I Built This

Skyline Shop serves a lot of customers throughout the day. During peak hours, footfall goes up suddenly and there is no way to know without physically being there. I wanted a simple system that watches the camera feed and sends an alert when too many people are inside. After it worked well, I expanded it so any retail shop owner can use it to understand when their shop is busiest and how engaged their customers are.


## What It Does

Plugs into any existing CCTV setup, counts people in real time using YOLOv8, displays the live count on screen, and sends an instant alert when the crowd crosses a set limit. Shop owners can use this to monitor customer engagement, identify peak hours, and manage staff accordingly.


## Who This Is For

Small retail shops and stores, cyber cafes and service centers, medical shops and clinics, and any shop owner who wants to understand customer footfall and engagement patterns.


## Features

Real-time person detection using YOLOv8. Live footfall count displayed on screen at all times. Instant alert sent to phone when crowd count gets high. Shows exact number of people detected in the frame. Helps identify peak hours and customer engagement patterns. 5-minute cooldown so alerts do not spam. Threshold is adjustable and default is set to 10 persons. Works with both USB and IP/RTSP cameras.


## Tech Stack

| Tool | Purpose |
|------|---------|
| YOLOv8 (Ultralytics) | Person detection |
| OpenCV | Video capture and frame processing |
| Python | Core logic |
| Telegram Bot API | Mobile alerts |
| NumPy | Frame array handling |


## How It Works

Camera feed is captured frame by frame via OpenCV. YOLOv8 runs on each frame and detects all persons. Bounding boxes are drawn and live count is shown on screen. If count exceeds threshold, an instant alert is sent to the owner's phone with the exact number of people detected. Cooldown timer prevents repeated alerts. Over time, shop owners can track which hours see the most footfall and plan accordingly.


## Sample Output



![Demo](assets/demo.png)



11 persons detected. Alert triggered.


## Run It

```bash
git clone https://github.com/yourusername/Smart-Shop-Crowd-Monitoring
cd Smart-Shop-Crowd-Monitoring
pip install -r requirements.txt
python detect.py
 ```


## Future Improvements
I plan to improve this system further. The next version will include theft detection using pose estimation and suspicious behaviour analysis. It will trigger a loud alarm at the shop automatically when suspicious activity is detected, not just a phone alert. This will make it a complete shop security system, not just a crowd monitor.

## Built By
Anmol Gupta, B.Tech CSE (AI & ML), KR Mangalam University. Originally built for Skyline Shop, Badarpur, Delhi. Made open source so any shop owner can use it.

# 🏪 Smart Shop Crowd Monitoring & Alert System

A real-time AI-powered crowd monitoring system built for retail shops. It uses computer vision to track how many customers are inside via CCTV — and automatically sends a mobile alert when the crowd gets too high.

> I built this during my internship at Radhe Krishn Enterprises. The actual problem was simple — shop owners had no cheap way to know when their store was getting too crowded during peak hours or sale days.

---

## 🚨 Why I Built This

Small retail shops don't have dedicated staff watching camera feeds all day. During festivals or weekends, overcrowding happens silently — bad for customers, bad for business. I wanted to fix this with something lightweight and affordable.

---

## 💡 What It Does

Plugs into any existing CCTV setup, counts people in real time using YOLOv8, and sends an instant alert to the shop owner's phone when crowd crosses a limit.

---

## ✨ Features

- 🎯 Real-time person detection using YOLOv8
- 📊 Live footfall count displayed on screen
- 📱 Instant Telegram alert when crowd exceeds threshold
- ⏱️ 5-minute cooldown so alerts don't spam
- 🔧 Threshold is adjustable (default set to 10 persons)
- Works with both USB and IP/RTSP cameras

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| YOLOv8 (Ultralytics) | Person detection |
| OpenCV | Video capture and frame processing |
| Python | Core logic |
| Telegram Bot API | Mobile alerts |
| NumPy | Frame array handling |

---

## ⚙️ How It Works

1. Camera feed captured frame by frame via OpenCV
2. YOLOv8 runs on each frame and detects all persons
3. Bounding boxes drawn, live count shown on screen
4. Count exceeds threshold → Telegram alert sent to owner
5. Cooldown timer prevents repeated alerts

---

## 📸 Sample Output



![Demo](assets/demo.png)


*11 persons detected — alert triggered*

---

## 🔧 Run It

```bash
git clone https://github.com/yourusername/Smart-Shop-Crowd-Monitoring
cd Smart-Shop-Crowd-Monitoring
pip install -r requirements.txt
python detect.py
```

---

## 🙋 Built By

**Anmol Gupta** — B.Tech CSE (AI & ML), KR Mangalam University

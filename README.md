# 🚗 Number Plate Detection from Video using OpenCV

## Overview
This project detects vehicle number plates from a video file using **OpenCV's Haar Cascade Classifier**. It reads each frame, detects number plates, draws bounding boxes, and displays the processed video in a window.

This system can be extended for **Automatic Number Plate Recognition (ANPR)** in traffic monitoring, parking management, or security applications.

---

## Features
- Detects number plates from video files
- Live frame display with bounding boxes
- Press **Q** to quit the display
- Clean resource handling using `try-finally`

---

## Project Structure

| File / Folder | Description |
| :--- | :--- |
| `number_plate_detection.py` | Main Python script for detection |
| `haarcascade_russian_plate_number.xml` | Pre-trained Haar cascade for number plates |
| `video/` *(optional)* | Sample videos to test detection |
| `requirements.txt` | Python dependencies |

---

## Installation & Setup

01. Clone the repository:
```bash
git clone https://github.com/YourUsername/NumberPlate-Detection.git
cd NumberPlate-Detection
```
02. Install dependencies:
```bash
pip install -r requirements.txt
```
## How to Run
1. Place your video file in the repo folder.
2. Update the video_path variable in number_plate_detection.py with your video file name.
3. Run the script:
```bash
python number_plate_detection.py
```
4. Usage:
- The video frames will be displayed in a window.
- Press Q to quit the display.
- The processed video will be saved automatically as number_plate_detection.mp4.

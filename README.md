# 🚦 Real-Time Traffic Sign Detection using YOLOv8

## 📌 Overview

This project performs **real-time traffic sign detection** using the YOLOv8 object detection model and OpenCV. Frames captured from a webcam are processed in real time, allowing the system to identify traffic signs, draw bounding boxes, display confidence scores, and monitor FPS performance.

The project is designed as a lightweight computer vision application and can be adapted for autonomous driving systems, ADAS, robotic platforms, or embedded AI devices such as NVIDIA Jetson.

---

## ✨ Features

* Real-time traffic sign detection
* YOLOv8-based object detection
* Live webcam processing
* Bounding box visualization
* Confidence score display
* FPS monitoring
* Easy integration with custom-trained YOLOv8 models

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy

---

## 📂 Project Structure

```
Traffic-Sign-Detection/
│
├── traffic_sign_detection.py
├── requirements.txt
├── README.md
└── best.pt          # User-provided trained YOLOv8 model
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Traffic-Sign-Detection.git
cd Traffic-Sign-Detection
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Place your trained YOLOv8 model (`best.pt`) in the project directory.

Run the application:

```bash
python traffic_sign_detection.py
```

Press **Q** to quit the application.

---

## 🧠 Model

This repository does **not** include the trained model (`best.pt`).

Users can:

* Train their own YOLOv8 model using a traffic sign dataset.
* Replace `best.pt` with any compatible YOLOv8 traffic sign detection model.

The detection script automatically loads the provided model during runtime.

---

## 📈 Output

The application displays:

* Detected traffic signs
* Bounding boxes
* Class labels
* Confidence scores
* Real-time FPS

---

## 🚀 Future Improvements

* Traffic sign tracking
* Distance estimation
* Traffic light detection
* Embedded deployment (NVIDIA Jetson)
* ROS integration
* Automatic vehicle control based on detected signs

---

## 📄 License

This project is released under the MIT License.

---

## 👩‍💻 Author

**Dilara Karataş**

Computer Engineering Student

Interested in Computer Vision, Embedded Systems, Autonomous Systems, and Artificial Intelligence.

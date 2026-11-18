# Face Emotion Recognition System
نظام التعرف على المشاعر من تعابير الوجه

A desktop application that detects human facial emotions in real-time using a custom CNN model and provides personalized activity recommendations based on the detected emotion and user's age group.

## Features
- Detects **7 emotions**: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- Supports **image upload** or **live camera capture**
- Provides **age-tailored recommendations** (6 age groups: 15–40+)
- User authentication with **registration & login**

## Model
- Architecture: Custom **CNN** (4 convolutional layers + 2 fully connected)
- Framework: **TensorFlow / Keras**
- Input: 48×48 grayscale face images
- Training data: **FER dataset** — 28,821 train / 7,066 validation images
- Accuracy: **94%** overall

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| TensorFlow / Keras | CNN model |
| OpenCV | Camera capture & image processing |
| Tkinter + PIL | Desktop GUI |
| SQLite | User database |
| NumPy / Pandas | Data handling |
| Scikit-learn | Label encoding |

## Setup
```bash
pip install tensorflow opencv-python pillow numpy pandas scikit-learn
python gui.py
```

## Usage
1. Register with your email and age
2. Click **Predict** to upload an image, or **Cam** to use the camera (press Space to capture)
3. The system detects your emotion and shows personalized suggestions

# 🛡️ SurvivorScan - Smart Disaster Victim Identification System

SurvivorScan is a facial recognition-based emergency response solution designed to **identify survivors** during disasters, **track missing persons**, and **alert authorities in real-time**. Built with the intent of supporting rescue missions, this system provides a **centralized dashboard** for efficient victim recognition using image uploads and live camera feeds.

## 🚀 Features

- 🔍 **Victim Identification via Image Upload**
  - Upload an image of a person (rescued or found)
  - Matches face with known database (preloaded/family input)
  - Returns name, location, and status if matched

- 📸 **Real-Time Detection from Live Camera**
  - Uses a webcam or external feed
  - Detects multiple faces in one frame
  - Triggers alert if missing person is identified

- 📊 **User Dashboard**
  - Total number of known, unknown, and missing persons
  - Real-time alerts when someone is identified
  - Face match history and image log

- 🌐 **Coordinates of Detection**
  - Captures geolocation (latitude & longitude) where face was detected
  - Useful for rescue mapping and victim tracking

- 🔔 **Live Alerts/Notifications**
  - Alerts for matched identities
  - UI pop-ups with name, match confidence, and location

---

## 🧠 Tech Stack

| Technology       | Purpose                         |
|------------------|----------------------------------|
| Python           | Backend logic and detection     |
| OpenCV           | Image processing & face capture |
| face_recognition | Facial recognition and matching |
| Flask            | API & Web App backend           |
| HTML/CSS/JS      | Frontend UI                     |
| SQLite / CSV     | Temporary storage (can be scaled to PostgreSQL) |
| Geopy / Location | Get GPS coordinates             |

---

---

## ✅ How to Run

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/SurvivorScan.git
cd SurvivorScan
Install Requirements:

bash
Copy code
pip install -r requirements.txt
Run the Flask App:

bash
Copy code
python app.py
Access the Web App:
Open http://127.0.0.1:5000 in your browser.


# DARPAN: AI-Powered Face Recognition for Smart Education

DARPAN is an AI-based facial recognition system designed to modernize attendance management in educational institutions. By leveraging deep learning and computer vision, DARPAN eliminates proxy attendance, improves campus security, and enables transparent, automated reporting for government audits. It helps to implement government policies in a better way.
The following project is deployed in docker.
---

##  Problem Statement

Educational institutions face challenges like:
- Proxy attendance in 34% of institutions (ASER 2023)
- Manual attendance consuming 15% of teaching time
- Outdated surveillance risking campus security
- Misuse of mid-day meal funds due to fake attendance

---

##  Solution

**DARPAN** provides:
- Real-time facial recognition-based attendance
- Fraud detection (proxy attendance prevention)
- Automated attendance reports for audits
- An interactive dashboard for monitoring
- Hardware-accelerated face detection and matching

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow
- **Face Detection & Recognition:** Dlib, MTCNN
- **Image & Video Processing:** OpenCV
- **Data Handling:** NumPy, Pandas
- **Hardware Acceleration:** NVIDIA CUDA (optional)

---

##  Project Workflow

1. **Capture Video Stream**
2. **Face Detection (MTCNN / Dlib)**
3. **Face Recognition & Matching**
4. **Display Results on Web Interface**
5. **Store Attendance Data**
6. **Real-time Monitoring & Alerts**
7. **Dashboard Display**
8. **Automated Government Report Generation**

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/darpan-face-attendance.git
cd darpan-face-attendance

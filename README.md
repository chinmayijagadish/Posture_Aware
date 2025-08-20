# 📘 Posture Aware Study Assistant  

## 📌 Overview  
The **Posture Aware Study Assistant** is a Machine Learning project that detect posture in real-time. The system analyzes images also real time video to classify whether the posture is **good** or **bad**. If the posture is wrong, it can notify the user to adjust, helping in reducing strain and promoting healthy study habits.  

This project is built using **Python, scikit-learn, Flask, and VS Code** with a posture recognition dataset.  

---

## 🚀 Features  
- Detects posture (good / bad)  
- Trains a machine learning model on a posture recognition dataset  
- Provides real-time feedback using a Flask web app  
- Beginner-friendly setup with step-by-step code  
- Easily extendable to real-time webcam monitoring  

---

## 🛠️ Tech Stack  
- **Programming Language**: Python 3.6+  
- **Libraries**:  
  - Flask (Web Framework)  
  - scikit-learn (ML Model Training)    

---


---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/chinmayijagadish/Posture_Aware.git
cd posture_aware_study_assistant
```

###2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
Activate it:
Windows (PowerShell)
```bash
.\venv\Scripts\activate
```
Linux/Mac
```bash
source venv/bin/activate
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---

4️⃣ Train the Model
```bash
python train_model.py
```
---
This will generate model.pkl.

5️⃣ Run the Web App
```bash
python app.py
```

Go to 👉 http://127.0.0.1:5000 in your browser.

---

📊 Dataset

- The project uses a Posture Recognition Dataset containing labeled images/data of good and bad postures.

- Classes: Good,Bad

- Features include body keypoints or extracted features for classification.

🔮 Future Scope

- Add real-time webcam monitoring

- Generate study reports on posture habits

- Extend to detect drowsiness / distraction

- Integrate with IoT sensors for smart study desks



 



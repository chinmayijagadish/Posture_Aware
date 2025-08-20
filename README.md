## 📘 Posture Aware Study Assistant

📌 Overview

The Posture Aware Study Assistant is a Machine Learning project that detects posture in real-time. The system analyzes images (or webcam feed) to classify whether the posture is correct or incorrect. If the posture is wrong, it can notify the user to adjust, helping in reducing strain and promoting healthy study habits.

This project is built using Python, scikit-learn, Flask, and VS Code with a posture recognition dataset.

🚀 Features

Detects posture (correct / incorrect).

Trains a machine learning model on a posture recognition dataset.

Provides real-time feedback using a Flask web app.

Beginner-friendly setup with step-by-step code.

Easily extendable to real-time webcam monitoring.

🛠️ Tech Stack

Programming Language: Python 3.12+

Libraries:

Flask (Web Framework)

scikit-learn (ML Model Training)

joblib (Model Saving/Loading)

pandas, numpy (Data Handling)

📂 Project Structure
posture_aware_study_assistant/
│
├── dataset/                     # Posture recognition dataset
│   ├── train.csv                # Training data
│   ├── test.csv                 # Testing data
│
├── app.py                       # Flask Web App
├── train_model.py               # ML model training script
├── model.pkl                    # Saved trained model
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd posture_aware_study_assistant

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows (PowerShell)

.\venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train the Model
python train_model.py


This will generate model.pkl.

5️⃣ Run the Web App
python app.py


Go to 👉 http://127.0.0.1:5000
 in your browser.

📊 Dataset

The project uses a Posture Recognition Dataset containing labeled images/data of correct and incorrect postures.

Classes: Correct, Incorrect

Features include body keypoints or extracted features for classification.

(You can replace this with your own dataset if needed.)

🔮 Future Scope

Add real-time webcam monitoring.

Generate study reports on posture habits.

Extend to detect drowsiness / distraction.

Integrate with IoT sensors for smart study desks.

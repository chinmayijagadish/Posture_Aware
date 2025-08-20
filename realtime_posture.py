import cv2
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model('saved_model/posture_model.h5')

# Start webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for model input
    resized_frame = cv2.resize(frame, (64, 64))
    normalized = resized_frame / 255.0
    input_data = np.expand_dims(normalized, axis=0)

    # Predict
    prediction = model.predict(input_data)[0][0]

    # Display result
    label = "Good Posture ✅" if prediction < 0.5 else "Bad Posture ❌"
    color = (0, 255, 0) if prediction < 0.5 else (0, 0, 255)

    # Overlay label
    cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow('Posture Alert (Press Q to quit)', frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()

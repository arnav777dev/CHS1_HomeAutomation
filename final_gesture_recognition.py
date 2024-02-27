#  packages
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import serial
import time
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
last_name = ""
model = load_model('mp_hand_gesture')

f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# webcam
cap = cv2.VideoCapture(0)

# Initialize serial communication with Arduino
ser = serial.Serial('COM13', 9600) 
time.sleep(2)  

while True:
    _, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)

    className = ''

    # post-process the res  
    # ult/777777777y
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            # time.sleep(0.5)
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            className = classNames[classID]
            # if( last_name != className):
            #     last_name = className
            print("sending"+ className)
            ser.write(className.encode())
            time.sleep(1.5)

    # prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2, cv2.LINE_AA)

    # final output
    cv2.imshow("Output", frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
ser.close()
cv2.destroyAllWindows()

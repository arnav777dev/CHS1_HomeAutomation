import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Define your saved hand gesture
saved_gesture = {
    "thumbs_up": {"x": 0.4195526, "y": 0.7786832, "z": -0.019242689},
    # Add more gestures as needed
}

# Define a similarity threshold for gesture recognition
similarity_threshold = 0.1

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Check similarity with your saved gesture
                gesture_detected = None
                for gesture_name, reference_landmarks in saved_gesture.items():
                    similarity = sum(
                        abs(hand_landmarks.landmark[i].x - reference_landmarks["x"]) +
                        abs(hand_landmarks.landmark[i].y - reference_landmarks["y"]) +
                        abs(hand_landmarks.landmark[i].z - reference_landmarks["z"])
                        for i in range(len(hand_landmarks.landmark))
                    )
                    if similarity < similarity_threshold:
                        gesture_detected = gesture_name
                        break

                if gesture_detected:
                    print(f"Detected gesture: {gesture_detected}")
                    # You can perform actions based on the detected gesture here

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()

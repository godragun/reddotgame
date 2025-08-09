import cv2
import numpy as np
import mediapipe as mp
import random
import time

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

# Game variables
dot_radius = 20
score = 0
game_duration = 30  # seconds
start_time = time.time()
dots = []

# Function to create a new random dot
def create_dot(frame_width, frame_height):
    x = random.randint(dot_radius, frame_width - dot_radius)
    y = random.randint(dot_radius, frame_height - dot_radius)
    return (x, y)

# Start webcam
cap = cv2.VideoCapture(0)  # 0 = default laptop cam

if not cap.isOpened():
    print("Error: Could not access webcam")
    exit()

# Get frame size
ret, frame = cap.read()
if not ret:
    print("Error: Could not read from webcam")
    exit()

frame_h, frame_w = frame.shape[:2]
dots = [create_dot(frame_w, frame_h) for _ in range(5)]

while True:
    elapsed = time.time() - start_time
    if elapsed >= game_duration:
        break

    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)
    hand_positions = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            for lm in hand_landmarks.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                hand_positions.append((x, y))
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Draw and check collision for dots
    for dot in dots[:]:
        cv2.circle(frame, dot, dot_radius, (0, 0, 255), -1)
        for hx, hy in hand_positions:
            if np.sqrt((hx - dot[0]) ** 2 + (hy - dot[1]) ** 2) < dot_radius + 10:
                dots.remove(dot)
                score += 1
                dots.append(create_dot(frame.shape[1], frame.shape[0]))
                break

    # Draw score & timer
    cv2.putText(frame, f"Score: {score}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    remaining_time = max(0, int(game_duration - elapsed))
    cv2.putText(frame, f"Time: {remaining_time}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Touch the Dots Game", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Game Over! Final Score: {score}")

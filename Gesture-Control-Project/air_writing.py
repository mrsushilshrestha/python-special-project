def update_drawing(frame, results, drawing):
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        if is_index_finger_up(hand_landmarks):
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])
            drawing.append((x, y))
        if is_palm_open(hand_landmarks):
            drawing.clear()
    return drawing

def draw_trajectory(frame, drawing):
    for i in range(1, len(drawing)):
        cv2.line(frame, drawing[i-1], drawing[i], (0, 255, 0), 2)
    return frame
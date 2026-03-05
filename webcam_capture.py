# webcam_capture.py
import cv2
import os
from datetime import datetime

def capture_photo(save_to_folder="photos", camera_index=0, warmup_frames=10):
    """
    Captures a single photo from the webcam WITHOUT any preview window,
    saves it to disk, and returns the saved file path.

    Returns:
        str: saved file path
        None: if capture failed
    """
    os.makedirs(save_to_folder, exist_ok=True)

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    # Warm up camera (auto-exposure/auto-whitebalance)
    for _ in range(max(0, warmup_frames)):
        cap.read()

    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None or frame.size == 0:
        print("Error: Failed to capture frame.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"photo_{timestamp}.jpg"
    save_path = os.path.join(save_to_folder, filename)

    if not cv2.imwrite(save_path, frame):
        print("Error: Failed to save photo.")
        return None

    return save_path


if __name__ == "__main__":
    path = capture_photo(save_to_folder="captured_photos")
    if path:
        print("Saved:", path)
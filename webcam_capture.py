# webcam_capture.py
import cv2
import os
from datetime import datetime
import numpy as np

def detect_and_crop_person(frame):
    """
    Detects a person in the frame and crops to them.
    If no person found, returns a center square crop.
    
    Args:
        frame: Input image frame
        
    Returns:
        Cropped image (square aspect ratio)
    """
    height, width = frame.shape[:2]
    
    # Try to detect person using Haar Cascade
    try:
        # Try multiple cascade classifiers for better detection
        cascade_files = [
            'haarcascade_fullbody.xml',
            'haarcascade_upperbody.xml',
            'haarcascade_frontalface_default.xml'
        ]
        
        people = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        for cascade_file in cascade_files:
            try:
                # Try to load cascade from cv2 data directory
                cascade_path = os.path.join(cv2.__path__[0], 'data', cascade_file)
                if not os.path.exists(cascade_path):
                    # Fallback: try haarcascades subdirectory
                    cascade_path = os.path.join(cv2.__path__[0], 'data', 'haarcascades', cascade_file)
                
                if os.path.exists(cascade_path):
                    person_cascade = cv2.CascadeClassifier(cascade_path)
                    
                    # Detect people
                    detections = person_cascade.detectMultiScale(
                        gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30)
                    )
                    
                    if len(detections) > 0:
                        people = detections
                        break
            except:
                continue
        
        # If person detected, crop to largest detection
        if len(people) > 0:
            # Get largest detection
            largest = max(people, key=lambda rect: rect[2] * rect[3])
            x, y, w, h = largest
            
            # Make crop area 3X the size of detected face/person
            # Calculate center of detection
            center_x = x + w // 2
            center_y = y + h // 2
            
            # New size is 3X the detection size
            new_size = int(max(w, h) * 3)
            
            # Calculate crop boundaries centered on detection
            x1 = max(0, center_x - new_size // 2)
            y1 = max(0, center_y - new_size // 2)
            x2 = min(width, center_x + new_size // 2)
            y2 = min(height, center_y + new_size // 2)
            
            # Make it square by expanding the smaller dimension
            crop_w = x2 - x1
            crop_h = y2 - y1
            
            if crop_w > crop_h:
                diff = crop_w - crop_h
                y1 = max(0, y1 - diff // 2)
                y2 = min(height, y2 + diff // 2)
            else:
                diff = crop_h - crop_w
                x1 = max(0, x1 - diff // 2)
                x2 = min(width, x2 + diff // 2)
            
            return frame[y1:y2, x1:x2]
    except Exception as e:
        print(f"Person detection failed: {e}")
    
    # No person found - return center square crop
    size = min(height, width)
    start_x = (width - size) // 2
    start_y = (height - size) // 2
    
    return frame[start_y:start_y + size, start_x:start_x + size]

def capture_photo(save_to_folder="photos", camera_index=0, warmup_frames=10):
    """
    Captures a single photo from the webcam WITHOUT any preview window,
    detects and crops to person (or center square if no person found),
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

    # Detect person and crop
    cropped_frame = detect_and_crop_person(frame)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"photo_{timestamp}.jpg"
    save_path = os.path.join(save_to_folder, filename)

    if not cv2.imwrite(save_path, cropped_frame):
        print("Error: Failed to save photo.")
        return None

    return save_path


if __name__ == "__main__":
    path = capture_photo(save_to_folder="captured_photos")
    if path:
        print("Saved:", path)

# Made with Bob

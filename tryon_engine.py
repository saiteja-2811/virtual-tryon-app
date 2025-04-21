import numpy as np
from PIL import Image
import mediapipe as mp
import cv2

def get_eye_positions(pil_img):
    """Detect eyes using MediaPipe Face Mesh and return (left_eye, right_eye) pixel coordinates."""
    mp_face_mesh = mp.solutions.face_mesh
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        img = np.array(pil_img.convert("RGB"))
        results = face_mesh.process(img)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]
            h, w = img.shape[:2]
            left = landmarks.landmark[33]  # Left eye landmark
            right = landmarks.landmark[263]  # Right eye landmark
            left_px = int(left.x * w), int(left.y * h)
            right_px = int(right.x * w), int(right.y * h)
            return left_px, right_px
        else:
            return None, None

def overlay_accessory(user_img, accessory_path):
    """Overlay accessory on face based on eye detection, with fallback if face not found."""
    accessory = Image.open(accessory_path).convert("RGBA")
    user_img = user_img.convert("RGBA")

    left_eye, right_eye = get_eye_positions(user_img)

    if left_eye and right_eye:
        # Compute eye width and scaling
        eye_width = int(np.linalg.norm(np.array(right_eye) - np.array(left_eye)))
        accessory_width = eye_width
        accessory_height = int(eye_width * 0.4)
        accessory = accessory.resize((accessory_width, accessory_height))

        # Center above eyes
        x = left_eye[0]
        y = left_eye[1] - int(accessory_height * 0.8)
        user_img.paste(accessory, (x, y), accessory)
    else:
        # Fallback: fixed position
        fallback_size = (150, 50)
        accessory = accessory.resize(fallback_size)
        user_img.paste(accessory, (50, 50), accessory)

    return user_img

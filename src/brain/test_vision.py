import sys
import os
import cv2
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.vision import VisionSystem

def test():
    vision = VisionSystem()
    print("[TEST] Capturing screen...")
    img = vision.capture_screen()
    img.save("test_screen.png")
    
    # Create a dummy template (crop center)
    w, h = img.size
    cx, cy = w//2, h//2
    # Crop 100x100 from center
    box = (cx-50, cy-50, cx+50, cy+50)
    template = img.crop(box)
    template.save("test_template.png")
    print("[TEST] Created test_template.png from screen center.")
    
    # Try to find it
    print("[TEST] Searching for template...")
    coords = vision.find_template("test_template.png", debug_save="test_result.png")
    
    if coords:
        print(f"[TEST] SUCCESS! Found at: {coords}")
        # Validate coordinates (should be close to cx, cy)
        dist = abs(coords[0] - cx) + abs(coords[1] - cy)
        print(f"[TEST] Distance from actual center: {dist} pixels")
    else:
        print("[TEST] FAILURE. Template not found.")

if __name__ == "__main__":
    test()

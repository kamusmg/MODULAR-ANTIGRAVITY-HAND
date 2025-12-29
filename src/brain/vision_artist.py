import sys
import os
import time
import cv2
import numpy as np
import pyautogui

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.vision import VisionSystem

def vision_portrait():
    print("[VISION ARTIST] Waking up...")
    vision = VisionSystem()
    
    # 1. Capture and Find Canvas
    print("[VISION ARTIST] Scanning ALL monitors for Paint Canvas...")
    
    # Get Monitor 0 (Global) Geometry to calculate offsets
    mon0 = vision.sct.monitors[0]
    off_x, off_y = mon0['left'], mon0['top']
    
    # Capture ALL detection space (Monitor 0 = Combined)
    img_pil = vision.capture_screen(monitor_index=0) 
    if not img_pil:
        print("[VISION ARTIST] Blind! Cannot see screen.")
        return

    # Process Image
    img_np = np.array(img_pil)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Threshold - Find bright white areas
    _, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    
    # DEBUG: Save views
    print("[VISION ARTIST] Saving debug images...")
    cv2.imwrite("debug_artist_view.png", img_cv)
    cv2.imwrite("debug_artist_thresh.png", thresh)
    
    # Find Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("[VISION ARTIST] No contours found!")
        return
        
    print(f"[VISION ARTIST] Found {len(contours)} contours. Analyzing candidates...")
    
    valid_candidates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        
        # Calculate Desktop Coords
        desktop_x = x + off_x
        desktop_y = y + off_y
        
        if area > 100000: # Filter noise (must be BIG)
             print(f" - Candidate: Image({x},{y}) -> Desktop({desktop_x},{desktop_y}) Size: {w}x{h} Area: {area}")
             valid_candidates.append(cnt)

    if not valid_candidates:
        print("[VISION ARTIST] No large white areas found.")
        return

    # Find largest contour (The Canvas)
    largest_contour = max(valid_candidates, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # Apply Offset
    center_x = (x + w // 2) + off_x
    center_y = (y + h // 2) + off_y
    
    print(f"[VISION ARTIST] Target Locked: Desktop Center ({center_x}, {center_y})")
    
    # Move to target
    pyautogui.moveTo(center_x, center_y, duration=1.0)
    
    # Focus
    print("[VISION ARTIST] Focusing...")
    pyautogui.click()
    time.sleep(0.5)
    
    # --- DRAWING ROUTINE: SELF PORTRAIT (THE MIND) ---
    print("[VISION ARTIST] Drawing Self-Portrait (The Digital Brain)...")
    
    def drag_line(dx, dy):
        pyautogui.drag(dx, dy, duration=0.2, button='left')
    
    def move_brush(dx, dy):
        pyautogui.move(dx, dy, duration=0.1)

    # Center (Start of Brain)
    # Draw huge oval
    print(" - Cortex")
    
    # Top arc
    drag_line(150, -50)
    drag_line(150, 50)
    
    # Right side
    drag_line(50, 100)
    drag_line(-20, 100)
    
    # Bottom
    drag_line(-200, 50) # Cerebellum?
    drag_line(-150, -50)
    
    # Left side
    drag_line(-50, -100)
    drag_line(20, -100) # Close loop
    
    # Internal Convolutions (Squiggles)
    print(" - Synapses")
    pyautogui.mouseUp()
    move_brush(100, 100) # Move inside
    
    # Random-ish squiggles
    for _ in range(3):
        width = 50
        drag_line(width, 20)
        drag_line(-width, 20)
        drag_line(width, 20)
        move_brush(-width, 20)
        
    # The Eye (All seeing)
    pyautogui.mouseUp()
    move_brush(100, -150)
    
    print(" - The Eye")
    # Draw a triangle
    drag_line(50, 100)
    drag_line(-100, 0)
    drag_line(50, -100)
    
    # Pupil
    move_brush(0, 60)
    drag_line(10, 0) # Dot
    
    print("[VISION ARTIST] Self-Portrait Complete.")

if __name__ == "__main__":
    vision_portrait()

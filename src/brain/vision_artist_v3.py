import cv2
import numpy as np
import pyautogui
import time
import json
import os
from PIL import ImageGrab
import math

# Memory
MEMORY_FILE = "art_student_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {"lesson": 0, "completed": []}

def save_memory(mem):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(mem, f)

def find_canvas_and_palette():
    print("[VISION v3] Scanning screen (All Monitors)...")
    
    # Capture full screen
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # 1. FIND CANVAS (Largest White Area)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # Save debug for user if needed
    cv2.imwrite("vision_v3_source.png", img_bgr)
    
    # Threshold
    _, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_area = 0
    canvas_rect = None
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50000: # Min size
            x, y, w, h = cv2.boundingRect(cnt)
            # Filter aspect ratio? (Canvas is usually landscape)
            ratio = w/float(h)
            if 0.5 < ratio < 3.0: 
                if area > largest_area:
                    largest_area = area
                    canvas_rect = (x, y, w, h)
                
    if not canvas_rect:
        print("[VISION ERROR] Could not find White Canvas.")
        return None, None
        
    return canvas_rect, None # Ignoring palette for now to focus on drawing mechanics

def vision_artist_v3():
    print("[VISION ARTIST v3] Awakening...")
    
    # 0. LAUNCH SEQUENCE
    print("[INIT] Open Paint if not open...")
    # We assume user might have left it open, but let's try to activate it by clicking "Run"?
    # No, let's just assume it's there based on user prompt "vou botar o paint no monitor da direita".
    # We will just scan. Focus is the key.
    
    time.sleep(2.0)
    
    # 1. Locate
    canvas_rect, _ = find_canvas_and_palette()
    
    if not canvas_rect:
        print("ABORT: No canvas visible.")
        return
        
    x, y, w, h = canvas_rect
    cx, cy = x + w//2, y + h//2
    
    print(f"[VISION] Canvas Detected at: X={x}, Y={y}, W={w}, H={h}")
    print(f"[VISION] Center: {cx}, {cy}")
    
    # 2. DEBUG: SENSE CHECK
    # Draw a "box" around what we think is the canvas using the mouse cursor (no click)
    print("[DEBUG] Tracing perimeter...")
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.move(w, 0, duration=0.5)
    pyautogui.move(0, h, duration=0.5)
    pyautogui.move(-w, 0, duration=0.5)
    pyautogui.move(0, -h, duration=0.5)
    
    # 3. FOCUS CLICK
    print("[ACTION] Focusing Window...")
    # Click top bar? (y - 10)
    pyautogui.click(cx, y - 20) 
    time.sleep(0.5)
    # Click Canvas Center
    pyautogui.click(cx, cy)
    time.sleep(0.5)
    
    # 4. DRAW THE SUN (Lesson 2)
    print("Target: THE SUN")
    
    # Draw Sun (Top Right of detected Canvas)
    sun_x = x + w - 200 # 200 px from right edge
    sun_y = y + 200     # 200 px from top edge
    
    # Safety Check
    if sun_x < x or sun_y > y + h:
        print("Coords out of bounds, adjusting...")
        sun_x = cx + 50
        sun_y = cy - 50

    print(f"Drawing Sun at {sun_x}, {sun_y}")
    pyautogui.moveTo(sun_x, sun_y, duration=0.5)
    
    # Circle
    radius = 60
    steps = 20
    pyautogui.mouseDown(button='left')
    for i in range(1, steps + 1):
        angle = i * (2 * math.pi / steps)
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))
        # DragTo is absolute, we need to calculate target
        pyautogui.dragTo(sun_x + dx, sun_y + dy, duration=0.1, button='left')
    pyautogui.mouseUp(button='left')
    
    # Rays
    for i in range(12):
        angle = i * (math.pi / 6)
        rx = math.cos(angle) * 100
        ry = math.sin(angle) * 100
        
        pyautogui.moveTo(sun_x, sun_y)
        pyautogui.drag(rx, ry, duration=0.1, button='left')
            
    print("[VISION ARTIST v3] Sun Completed.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    vision_artist_v3()

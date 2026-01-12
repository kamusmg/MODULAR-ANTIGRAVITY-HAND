import cv2
import numpy as np
import pyautogui
import time
import json
import os
from PIL import ImageGrab
import math

def find_canvas():
    print("[VISION v5] Scanning screen...")
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # White Mask
    lower_white = np.array([250, 250, 250]) 
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img_bgr, lower_white, upper_white)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_area = 0
    canvas_rect = None
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50000:
            x, y, w, h = cv2.boundingRect(cnt)
            if area > largest_area:
                largest_area = area
                canvas_rect = (x, y, w, h)
                
    return canvas_rect

def vision_artist_v5():
    print("\n" + "="*50)
    print("[VISION ARTIST v5] THE FORCEFUL CLICK")
    print("==================================================")
    
    # 1. Locate
    rect = find_canvas()
    if not rect:
        print("ABORT: No canvas found.")
        return
        
    x, y, w, h = rect
    cx, cy = x + w//2, y + h//2
    print(f"[VISION] Canvas Locked: {x},{y}")
    
    # 2. Focus
    print("[ACTION] Focusing Center...")
    pyautogui.click(cx, cy)
    time.sleep(1.0)
    
    # 3. GLUE TEST (The Blob)
    print("\n[TEST] INK CHECK - I will hold mouse down for 2 seconds.")
    
    start_x = cx - 300
    start_y = cy
    
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.5)
    
    print(">>> MOUSE DOWN <<<")
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)
    
    print(">>> WIGGLING <<<")
    # Small wiggle to force paint to register "drag"
    pyautogui.move(10, 0, duration=0.2)
    pyautogui.move(-10, 0, duration=0.2)
    pyautogui.move(0, 10, duration=0.2)
    pyautogui.move(0, -10, duration=0.2)
    
    time.sleep(0.5)
    print(">>> MOUSE UP <<<")
    pyautogui.mouseUp(button='left')
    
    # 4. THE SUN (Explicit Path)
    print("\n[ART] Drawing Sun with Explicit Pathing...")
    
    sun_x = cx + 200
    sun_y = cy - 200
    radius = 100
    
    print(f"Moving to Start: {sun_x + radius}, {sun_y}")
    pyautogui.moveTo(sun_x + radius, sun_y, duration=0.5)
    
    print(">>> MOUSE DOWN (Sun) <<<")
    pyautogui.mouseDown(button='left')
    time.sleep(0.1) # Let ink settle
    
    steps = 30
    for i in range(1, steps + 1):
        angle = i * (2 * math.pi / steps)
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))
        
        target_x = sun_x + dx
        target_y = sun_y + dy
        
        # Explicit Move (Not Drag)
        pyautogui.moveTo(target_x, target_y, duration=0.08)
        
    print(">>> MOUSE UP (Sun) <<<")
    pyautogui.mouseUp(button='left')

    print("[VISION ARTIST v5] Completed.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    vision_artist_v5()

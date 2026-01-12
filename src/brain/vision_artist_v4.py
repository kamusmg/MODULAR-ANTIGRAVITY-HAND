import cv2
import numpy as np
import pyautogui
import time
import json
import os
from PIL import ImageGrab
import math

def find_canvas():
    print("[VISION v4] Scanning screen...")
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # White Mask
    lower_white = np.array([250, 250, 250]) # Slightly lenient
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img_bgr, lower_white, upper_white)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_area = 0
    canvas_rect = None
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50000:
            x, y, w, h = cv2.boundingRect(cnt)
            # Preference for Right Monitor (x >= 1920) if multiple
            if area > largest_area:
                largest_area = area
                canvas_rect = (x, y, w, h)
                
    return canvas_rect

def vision_artist_v4():
    print("[VISION ARTIST v4] The Giant Sun Protocol.")
    
    # 1. Locate
    rect = find_canvas()
    if not rect:
        print("ABORT: No canvas found.")
        return
        
    x, y, w, h = rect
    cx, cy = x + w//2, y + h//2
    print(f"[VISION] Canvas Locked: {x},{y} {w}x{h}")
    
    # 2. Focus
    print("[ACTION] Focusing Center...")
    pyautogui.click(cx, cy)
    time.sleep(1.0)
    
    # 3. VERIFICATION MARK (The X)
    print("[ACTION] Drawing Verification 'X'...")
    # TopLeft to BottomRight of a central box
    box_s = 400
    pyautogui.moveTo(cx - box_s//2, cy - box_s//2)
    pyautogui.drag(box_s, box_s, duration=1.0, button='left')
    
    pyautogui.moveTo(cx + box_s//2, cy - box_s//2)
    pyautogui.drag(-box_s, box_s, duration=1.0, button='left')
    
    # 4. THE SUN (Massive)
    print("Target: THE GIANT SUN")
    
    # Position: Slightly Right of Center
    sun_x = cx + 300
    sun_y = cy - 100
    radius = 150
    
    # Circle
    pyautogui.moveTo(sun_x + radius, sun_y, duration=0.5)
    pyautogui.mouseDown(button='left')
    steps = 40
    for i in range(1, steps + 1):
        angle = i * (2 * math.pi / steps)
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))
        pyautogui.dragTo(sun_x + dx, sun_y + dy, duration=0.05, button='left')
    pyautogui.mouseUp(button='left')
    
    # Rays
    for i in range(16):
        angle = i * (math.pi / 8)
        rx = math.cos(angle) * 250
        ry = math.sin(angle) * 250
        
        pyautogui.moveTo(sun_x, sun_y)
        pyautogui.drag(rx, ry, duration=0.2, button='left')
            
    print("[VISION ARTIST v4] Finished.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    vision_artist_v4()

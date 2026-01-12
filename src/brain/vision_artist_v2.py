import cv2
import numpy as np
import pyautogui
import time
import json
import os
from PIL import ImageGrab

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
    print("[VISION] Scanning screen (All Monitors)...")
    
    # Capture full screen
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # 1. FIND CANVAS (Largest White Area)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # Save debug
    cv2.imwrite("vision_debug_source.png", img_bgr)
    
    # Threshold - Lower to 200 for robustness
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite("vision_debug_thresh.png", thresh)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on debug image
    debug_cnt = img_bgr.copy()
    cv2.drawContours(debug_cnt, contours, -1, (0, 0, 255), 2)
    cv2.imwrite("vision_debug_contours.png", debug_cnt)
    
    largest_area = 0
    canvas_rect = None
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50000: # Lowered min size
            x, y, w, h = cv2.boundingRect(cnt)
            if area > largest_area:
                largest_area = area
                canvas_rect = (x, y, w, h)
                
    if not canvas_rect:
        print("[VISION ERROR] Could not find White Canvas. See vision_debug_thresh.png.")
        return None, None
        
    cx, cy, cw, ch = canvas_rect
    print(f"[VISION] Canvas Found: x={cx}, y={cy}, w={cw}, h={ch}")
    canvas_center = (cx + cw//2, cy + ch//2)
    
    # 2. FIND PALETTE
    # Strategy: Look for specific colors (Yellow) in the region ABOVE the canvas
    # The ribbon is usually top 150px of the window.
    # We search the whole screen for clusters of Yellow.
    
    # Yellow in HSV range
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # Yellow is roughly 20-30 Hue
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours_y, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    palette_center = None
    
    # We look for small squares (swatches)
    for cnt in contours_y:
        area = cv2.contourArea(cnt)
        if 50 < area < 2000: # Swatch size
            x, y, w, h = cv2.boundingRect(cnt)
            # Must be above canvas roughly? Or just assume it's the palette
            if y < cy: # Above the canvas start logic
                palette_center = (x + w//2, y + h//2)
                print(f"[VISION] Yellow Palette Found: {palette_center}")
                break
                
    if not palette_center:
        print("[VISION ERROR] Could not find Yellow Palette. Defaulting to offset.")
        # If we can't find it, we might be blocked or it's not visible.
        # But we found Canvas. Let's assume Palette is ~100px above Canvas Center X? No.
        return canvas_center, None

    return canvas_center, palette_center

def vision_artist_routine():
    print("[VISION ARTIST] Waking Up...")
    
    # 0. LAUNCH SEQUENCE
    print("[INIT] Launching MS Paint...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('mspaint')
    pyautogui.press('enter')
    print("[INIT] Waiting 5s for window...")
    time.sleep(5.0)
    
    # Maximize to ensure visibility
    pyautogui.hotkey('win', 'up')
    time.sleep(1.0)
    
    # 1. Locate
    canvas_pos, palette_pos = find_canvas_and_palette()
    
    if not canvas_pos:
        print("ABORT: No canvas visible. Please open MS Paint.")
        return
        
    cx, cy = canvas_pos
    
    # If palette failed, we can't switch colors safely.
    if not palette_pos:
        print("WARNING: Palette not found. I will draw in current color (Black?).")
        px, py = cx, cy - 200 # Dummy
    else:
        px, py = palette_pos
        
    mem = load_memory()
    lesson = mem["lesson"]
    print(f"[LESSON] Lesson {lesson} starting...")
    
    # 2. Execution (Lesson 2: Sun - if previous was Sky)
    # Actually logic said Lesson 1 in previous script (0 indexed).
    # Sky was 0.
    
    # Force Lesson 1/2 logic based on what we want: "Lesson 2: The Sun"
    # Or just continue "Art Student" logic.
    
    if "Sun" not in mem["completed"]:
        print("Target: THE SUN")
        
        # Click Yellow (Palette Pos)
        if palette_pos:
            print(f"Clicking Palette at {px}, {py}")
            pyautogui.click(px, py)
            time.sleep(0.5)
        
        # Draw Sun (Top Right of Canvas)
        sun_x = cx + 200
        sun_y = cy - 200
        
        print(f"Drawing Sun at {sun_x}, {sun_y}")
        pyautogui.moveTo(sun_x, sun_y)
        
        # Rays
        import math
        for i in range(12):
            angle = i * (math.pi / 6)
            rx = math.cos(angle) * 60
            ry = math.sin(angle) * 60
            
            pyautogui.moveTo(sun_x, sun_y)
            pyautogui.drag(rx, ry, duration=0.1, button='left')
            
        mem["completed"].append("Sun")
        mem["lesson"] += 1
        save_memory(mem)
        print("Sun Completed.")
        
    else:
        print("Sun already done? Drawing Grass next.")
        # ... Grass logic ...
        # For this test, let's just ensure we do SOMETHING visible.
        # If sun is done, let's do rays again or a House.
        
        print("Target: THE HOUSE")
        # Click Red (approx offset from Yellow if found)
        if palette_pos:
            # Red is left of Yellow usually
            pyautogui.click(px - 50, py) 
        
        house_x = cx
        house_y = cy + 100
        
        pyautogui.moveTo(house_x, house_y)
        pyautogui.drag(100, 0, duration=0.2, button='left')
        pyautogui.drag(0, -100, duration=0.2, button='left')
        pyautogui.drag(-100, 0, duration=0.2, button='left')
        pyautogui.drag(0, 100, duration=0.2, button='left')
        
        mem["completed"].append("House")
        mem["lesson"] += 1
        save_memory(mem)

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    vision_artist_routine()

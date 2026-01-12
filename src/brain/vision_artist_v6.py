import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
import math

def find_canvas():
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

def vision_artist_v6():
    print("\n" + "="*50)
    print("[VISION v6] THE BLACK SUN PROTOCOL")
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
    time.sleep(0.5)
    
    # 3. SELECT COLOR BLACK (Blind Guess based on Canvas Pos)
    # Palette is usually ~150px above the canvas top.
    # Black is usually the First or Second color in the top row.
    # In Win11 Paint, it's a grid.
    # Let's try to click multiple "Black" candidates relative to Canvas Top-Right? 
    # Or Scanning? Scanning is safer.
    
    print("[ACTION] Hunting for Black Palette...")
    # Just click coordinates that are likely the palette
    palette_y = y - 80 # Just above canvas
    palette_start_x = x + w - 300 # Right side toolbars? No, usually top left/center.
    
    # Actually, standard Paint: Colors are Top Right.
    # Let's click a few spots likely to be colors.
    
    # Strategy: Force reset tool.
    # Click near Top-Center of the Window (which is Canvas Y - 100)
    
    window_top_y = y - 140 # Ribbon area
    print("Clicking randomly in Ribbon to find Black...")
    
    # Assuming Default Win11 Paint Palette Location relative to Canvas (if Maximized)
    # It's hard to know.
    # Let's rely on the user having Black selected? NO.
    # Let's click the Yellow we found earlier and move LEFT.
    # Earlier we found Yellow at (2795, 108).
    # White/Black should be to the left.
    
    yellow_known_x = 2795 # From logs
    yellow_known_y = 108
    
    # If canvas x matches previous session (1920), we use this.
    if x == 1920:
        print("Using Memory: Clicking Left of Yellow...")
        pyautogui.click(yellow_known_x - 100, yellow_known_y) # Black?
        time.sleep(0.2)
        pyautogui.click(yellow_known_x - 150, yellow_known_y) # Black?
        time.sleep(0.2)
        
    # 4. DRAW
    print("\n[ART] Drawing The Black Sun...")
    sun_x = cx
    sun_y = cy
    radius = 120
    
    pyautogui.moveTo(sun_x + radius, sun_y)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1) # Ink flow
    
    steps = 40
    for i in range(1, steps + 1):
        angle = i * (2 * math.pi / steps)
        dx = int(radius * math.cos(angle))
        dy = int(radius * math.sin(angle))
        pyautogui.moveTo(sun_x + dx, sun_y + dy, duration=0.05)
        
    pyautogui.mouseUp(button='left')
    
    print("[VISION ARTIST v6] Completed.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    vision_artist_v6()

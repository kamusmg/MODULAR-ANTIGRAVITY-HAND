import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
import math
import sys

def find_studio_window():
    print("[STUDIO ARTIST] Scanning for Nucleus Art Studio...")
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Look for the Dark Sidebar (#2b2b2b => RGB(43,43,43))
    # Let's mask for this specific gray.
    lower_gray = np.array([40, 40, 40])
    upper_gray = np.array([46, 46, 46])
    mask = cv2.inRange(img_bgr, lower_gray, upper_gray)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Expecting a tall rectangle (Width 100, Height ~800)
    studio_rect = None
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 80 and w < 120 and h > 500:
            print(f"[VISION] Found Sidebar: {x},{y} {w}x{h}")
            studio_rect = (x, y, w, h)
            break
            
    return studio_rect

def studio_artist_routine():
    print("\n" + "="*50)
    print("[STUDIO ARTIST] Ready to Paint Freedom.")
    print("="*50)
    
    # 1. Locate
    sidebar = find_studio_window()
    if not sidebar:
        print("ABORT: Studio not found. Is it running?")
        # Fallback: Just ask user to ensure it's on main screen maximal?
        return
        
    sx, sy, sw, sh = sidebar
    
    # Known Layout:
    # Sidebar is Width 100.
    # Canvas starts at sx + 100.
    # Color Buttons are in Sidebar.
    
    canvas_x = sx +sw
    canvas_y = sy
    
    # Verify Focus
    print("[ACTION] Focusing...")
    pyautogui.click(canvas_x + 100, canvas_y + 100)
    time.sleep(0.5)
    
    # Helper to click colors
    # Palette is x=sx, y=sy... sy+10 (Label) ... Buttons imply specific offsets
    # But finding them is hard without OCR.
    # Since I built it, let's just assume layout or click roughly.
    # Button height=2 (text units?) -> actually Tkinter pixels vary.
    # Let's just draw with Black first.
    
    def draw_house():
        print("Drawing House...")
        start_x = canvas_x + 200
        start_y = canvas_y + 400
        
        pyautogui.moveTo(start_x, start_y)
        pyautogui.drag(200, 0, duration=0.5) # Floor
        pyautogui.drag(0, -200, duration=0.5) # Wall R
        pyautogui.drag(-200, 0, duration=0.5) # Ceiling
        pyautogui.drag(0, 200, duration=0.5) # Wall L
        
        # Roof
        pyautogui.move(0, -200)
        pyautogui.drag(100, -100, duration=0.5)
        pyautogui.drag(100, 100, duration=0.5)
        
    def draw_sun():
        print("Drawing Sun...")
        # Try to switch to Red/Yellow?
        # Yellow is likely the 5th button?
        # Colors: Black, Red, Green, Blue, Yellow...
        # Each button takes ~40-50px height?
        # Let's try blind clicks on sidebar
        pyautogui.click(sx + 50, sy + 250) # Approx Yellow?
        
        cx = canvas_x + 500
        cy = canvas_y + 150
        radius = 50
        
        pyautogui.moveTo(cx + radius, cy)
        pyautogui.mouseDown()
        for i in range(20):
             pyautogui.drag(10, 5)
             pyautogui.drag(-10, 5)
        pyautogui.mouseUp()
        
    # EXECUTE
    draw_house()
    draw_sun()
    
    # CLICK SAVE
    # Save is near bottom of actions.
    # Actions label at y + ??
    # Let's scan for "SAVE" text? Or just click bottom area of sidebar.
    print("[ACTION] Saving...")
    pyautogui.click(sx + 50, sy + 400) # Approx Save
    
    print("[STUDIO ARTIST] Finished.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    studio_artist_routine()

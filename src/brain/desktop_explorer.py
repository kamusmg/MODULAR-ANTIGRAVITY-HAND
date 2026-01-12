import pyautogui
import pytesseract
import time
import random
import os

# Configuration
TESS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESS_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESS_PATH

def explore_desktop():
    print("[EXPLORER] Curiosity Protocol Engaged.")
    
    # 1. Minimize everything to see Desktop
    print("[STEP 1] Going to Desktop...")
    pyautogui.hotkey('win', 'd')
    time.sleep(2.0)
    
    # 2. visual Scan
    print("[STEP 2] Scanning environment...")
    screenshot = pyautogui.screenshot()
    data = pytesseract.image_to_data(screenshot, lang='eng', output_type=pytesseract.Output.DICT)
    
    n_boxes = len(data['level'])
    found_targets = []
    
    # Find text that looks like icons (non-empty, confidence > 60)
    for i in range(n_boxes):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])
        
        if text and conf > 60:
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]
            
            # Filter out System Tray area (usually bottom right)
            s_w, s_h = pyautogui.size()
            if y < s_h - 60: 
                found_targets.append((text, x, y, w, h))

    print(f"[EXPLORER] I see {len(found_targets)} interesting things.")
    
    # 3. Curiosity Loop (Hover over 3 random things)
    if found_targets:
        demos = random.sample(found_targets, min(3, len(found_targets)))
        
        for target in demos:
            text, x, y, w, h = target
            print(f"[EXPLORER] Investigating: '{text}'...")
            
            # Move mouse to center of text
            target_x = x + w//2
            target_y = y + h//2
            
            # Smooth human-like move? (Direct for now)
            pyautogui.moveTo(target_x, target_y, duration=1.0)
            
            # Hover to trigger tooltip
            time.sleep(2.0)
            print(f"[EXPLORER] Analyzed '{text}'. Moving on.")
            
    # 4. End
    print("[EXPLORER] Curiosity satisfied for now.")
    # Restore windows? No, leave it clean.

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    explore_desktop()

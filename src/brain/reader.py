import pytesseract
import pyautogui
from PIL import Image
import os
import time

def read_screen():
    print("[READER BRAIN] Initializing Visual Cortex (Text Module)...")
    
    # 1. Configuration - Explicit Path
    # Common default path
    tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    if os.path.exists(tess_path):
        pytesseract.pytesseract.tesseract_cmd = tess_path
        print(f"[READER BRAIN] Engine found at: {tess_path}")
    else:
        # Fallback: Check checking local or user dir? No, let's error if not found.
        # Maybe user installed in AppData?
        possible_paths = [
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
             os.path.expanduser(r"~\AppData\Local\Tesseract-OCR\tesseract.exe")
        ]
        found = False
        for p in possible_paths:
            if os.path.exists(p):
                pytesseract.pytesseract.tesseract_cmd = p
                print(f"[READER BRAIN] Engine found at: {p}")
                found = True
                break
        
        if not found:
            print("[READER BRAIN] CRITICAL: Tesseract.exe not found in common paths.")
            print("Please ensure it is installed or update this script with the correct path.")
            return

    # 2. Capture Screen
    print("[READER BRAIN] Capturing scene...")
    screenshot = pyautogui.screenshot()
    
    # 3. Process Text
    print("[READER BRAIN] Reading text (OCR)...")
    # Using 'por' for Portuguese if available, else 'eng'
    try:
        text = pytesseract.image_to_string(screenshot, lang='por+eng')
    except pytesseract.TesseractError:
        print("[READER BRAIN] 'por' language pack missing? Falling back to 'eng'.")
        text = pytesseract.image_to_string(screenshot, lang='eng')
        
    print("\n" + "="*40)
    print("      VISUAL TEXT BUFFER      ")
    print("="*40)
    print(text.strip())
    print("="*40 + "\n")
    
    # 4. Keyword Search (Kern)
    keyword = "Kern"
    if keyword.lower() in text.lower():
        print(f"[READER BRAIN] ALERT: Keyword '{keyword}' detected on screen!")
    else:
        print(f"[READER BRAIN] Keyword '{keyword}' not found.")

if __name__ == "__main__":
    read_screen()

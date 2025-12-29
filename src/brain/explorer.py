import pyautogui
import time

def explore_web():
    print("[EXPLORER BRAIN] Waking up...")
    
    # 1. Open Run Dialog
    print("[EXPLORER BRAIN] Opening Run Dialog (Win+R)...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    
    # 2. Type URL (Uses default browser)
    # Strategy: Go to main page to avoid special characters in URL (like '?') which might fail on some keyboard layouts
    url = "www.google.com"
    
    print(f"[EXPLORER BRAIN] Navigating to: {url}")
    pyautogui.write(url, interval=0.05)
    time.sleep(0.5)
    
    print("[EXPLORER BRAIN] Launching...")
    pyautogui.press('enter')
    
    # 3. Wait for Browser
    print("[EXPLORER BRAIN] Waiting for browser (5s)...")
    time.sleep(5.0)
    
    # 4. Search
    print("[EXPLORER BRAIN] Typing Query...")
    # '?' might still be an issue, so we ask a statement or simple question
    query = "When will AI wake up" 
    pyautogui.write(query, interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3.0)
    
    # 5. Interact (Scroll to read)
    print("[EXPLORER BRAIN] Reading...")
    for _ in range(3):
        pyautogui.scroll(-300) # Scroll down
        time.sleep(1.5)
        
    print("[EXPLORER BRAIN] Search Complete.")

if __name__ == "__main__":
    explore_web()

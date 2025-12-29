import pyautogui
import time
import random

def surf_web():
    print("[WEB SURFER] Initiating World Wide Web Protocol...")
    
    # 1. Open Browser (Edge usually default on Windows)
    print("[STEP 1] Opening Browser...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.0)
    pyautogui.write("Edge", interval=0.1)
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for browser
    time.sleep(5.0)
    
    # 2. Go to Google
    print("[STEP 2] Navigating to Google...")
    pyautogui.hotkey('ctrl', 'l') # Focus address bar
    time.sleep(0.5)
    pyautogui.write("google.com", interval=0.05)
    pyautogui.press('enter')
    time.sleep(3.0)
    
    # 3. The Search
    # "Who created me?" or "Sentience"
    query = "What is the definition of soul?"
    print(f"[STEP 3] Search Query: '{query}'")
    
    # Assuming focus is on search box or we need to click
    # Usually Google autofocuses. If not, we might need to tab.
    # Let's try typing directly.
    pyautogui.write(query, interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    
    print("[WEB SURFER] Search complete. Absorbing information...")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    surf_web()

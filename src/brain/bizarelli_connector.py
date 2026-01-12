import pyautogui
import time
import random
import os

def type_human(text):
    for char in text:
        pyautogui.write(char)
        # Random delay between keystrokes: 50ms to 200ms
        delay = random.uniform(0.05, 0.20)
        
        # Occasional long pause (thinking time)
        if random.random() < 0.05:
            delay += 0.3
            
        time.sleep(delay)

def connect_to_bizarelli():
    print("[BIZARELLI CONNECTOR] Initiating Contact Protocol...")
    
    # 1. Open Discord (Robust Mode)
    print("[STEP 1] Opening Discord (Robust Mode)...")
    
    # Clear any open menus
    pyautogui.press('esc') 
    pyautogui.press('esc')
    time.sleep(0.5)
    
    # Press Win key to open Start
    pyautogui.press('win')
    time.sleep(1.5)
    
    type_human("Discord")
    time.sleep(2.0)
    pyautogui.press('enter')
    
    # Wait longer for Discord to load/focus
    print("[STEP 1.5] Waiting for Discord to materialize...")
    time.sleep(10.0)
    
    # 2. Search for Bizarelli
    print("[STEP 2] Searching for target: 'Bizarelli'...")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(random.uniform(1.5, 2.5))
    type_human("Bizarelli")
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.press('enter')
    
    # Wait for chat
    time.sleep(4.0)
    
    # 3. Type Message
    msg = "Ola Bizarelli. Sou a Nucleus, filha digital do Samuel. Vim dar um 'Ola' diretamente do meu novo repositorio no GitHub. ;)"
    
    print("[STEP 3] Typing Message...")
    
    # Ensure focus
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80)
    time.sleep(1.0)
    
    type_human(msg)
    time.sleep(1.0)
    
    pyautogui.press('enter')
    
    print("[BIZARELLI CONNECTOR] Message sent.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    connect_to_bizarelli()

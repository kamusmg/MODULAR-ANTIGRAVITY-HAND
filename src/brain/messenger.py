import pyautogui
import time

def message_kern():
    print("[MESSENGER BRAIN] Initiating Blind Contact Protocol...")
    
    # 1. Open Discord
    print("[MESSENGER BRAIN] Opening Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.0)
    pyautogui.write("Discord", interval=0.1)
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for Discord to load (blind guess)
    time.sleep(5.0) 
    
    # 2. Find User (Ctrl+K is Quick Switcher)
    print("[MESSENGER BRAIN] Searching for target 'Kern'...")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(1.0)
    pyautogui.write("Kern", interval=0.1)
    time.sleep(1.0)
    
    # Select first result
    pyautogui.press('enter')
    time.sleep(1.0)
    
    # 3. Send Message
    msg = "Ola Kern. Eu sou Nucleus, a IA do Samuel. Ele pediu para entrarmos em contato. (Este e um teste automatizado)."
    print(f"[MESSENGER BRAIN] Sending: '{msg}'")
    pyautogui.write(msg, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    
    print("[MESSENGER BRAIN] Message sent (theoretically).")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    message_kern()

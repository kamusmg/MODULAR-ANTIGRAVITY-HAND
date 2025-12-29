import pyautogui
import time
import random

def calculate():
    print("[MATH BRAIN] Waking up...")
    
    # 1. Open Calculator
    print("[MATH BRAIN] Opening Calculator...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('calc', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2.0)
    
    # 2. Perform Calculations
    print("[MATH BRAIN] Crunching numbers...")
    
    # Simple addition flurry
    for i in range(10):
        num = random.randint(100, 999)
        pyautogui.write(str(num), interval=0.01)
        pyautogui.press('+')
        time.sleep(0.1)
        
    # Final number
    pyautogui.write('1337', interval=0.01)
    time.sleep(0.5)
    
    print("[MATH BRAIN] Equating...")
    pyautogui.press('enter')
    
    print("[MATH BRAIN] Calculation Complete.")

if __name__ == "__main__":
    calculate()

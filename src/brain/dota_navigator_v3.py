import pyautogui
import time
import random

# Configuration
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def center_hero():
    print("[NAV V3] Centering Camera (F1)...")
    pyautogui.press('f1')
    time.sleep(0.1)
    pyautogui.press('f1')
    time.sleep(1.0)

def move_camera_and_walk(direction_keys, duration):
    print(f"[NAV V3] Moving Camera: {direction_keys} for {duration}s...")
    
    # Hold arrow keys to move camera
    for key in direction_keys:
        pyautogui.keyDown(key)
    
    time.sleep(duration)
    
    for key in direction_keys:
        pyautogui.keyUp(key)
        
    time.sleep(0.5)
    
    # Now click on the ground (Center of Screen) to walk there
    print("[NAV V3] Right Clicking Ground (Move Command)...")
    # Adding a small duration to the click to ensure registration
    pyautogui.mouseDown(button='right', x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)
    time.sleep(0.1)
    pyautogui.mouseUp(button='right', x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)
    
    # Wait for hero to walk
    print("[NAV V3] Walking...")
    time.sleep(4.0)

def navigate_routine_v3():
    print("[NAV V3] Protocol: Camera & Ground Control.")
    
    # 1. Focus Game
    pyautogui.click(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    time.sleep(1.0)
    center_hero()
    
    # 2. Sequence: Mid Lane (Down + Right)
    # Dire side is Top Right, Radiant is Bottom Left.
    # If we are Radiant (standard), Mid is Up+Right.
    # If we are Dire, Mid is Down+Left.
    # Let's try both directions to be sure we leave the fountain.
    
    # Attempt 1: Go Mid (Assuming Radiant perspective: Up + Right)
    move_camera_and_walk(['right', 'up'], 2.0)
    
    # Attempt 2: Go further Mid
    move_camera_and_walk(['right', 'up'], 2.0)
    
    # Action: Breathe Fire on the wave?
    pyautogui.press('q')
    
    # Attempt 3: Go Top (Up)
    move_camera_and_walk(['up'], 3.0)
    
    # Attempt 4: Go Bot (Down + Right from Top is hard, let's re-center)
    center_hero()
    move_camera_and_walk(['right', 'down'], 3.0)
    
    # Final center
    center_hero()
    print("[NAV V3] Sequence Complete.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    navigate_routine_v3()

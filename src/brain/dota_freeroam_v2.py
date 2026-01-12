import pyautogui
import time
import random

# Configuration
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Safe Viewport Area (Avoiding HUD at bottom)
# Top-Left: 0,0
# Bottom-Right: 1920, 800 (Leaving bottom 280px for HUD)
SAFE_Y_MAX = 800

def move_camera_randomly():
    keys = ['up', 'down', 'left', 'right']
    choice = random.choice(keys)
    duration = random.uniform(0.5, 1.5)
    
    print(f"[FREEROAM v2] Camera Pan: {choice.upper()} for {duration:.2f}s")
    pyautogui.keyDown(choice)
    time.sleep(duration)
    pyautogui.keyUp(choice)

def click_random_screen_spot():
    # Pick a random spot on the VISIBLE ground
    tx = random.randint(100, SCREEN_WIDTH - 100)
    ty = random.randint(100, SAFE_Y_MAX)
    
    print(f"[FREEROAM v2] Right Clicking Ground at ({tx}, {ty})")
    pyautogui.rightClick(tx, ty)
    time.sleep(0.1)

def navigation_repair_routine():
    print("[FREEROAM v2] Reverting to Chaos Logic + Camera Control.")
    
    # 1. Focus
    pyautogui.click(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    time.sleep(1.0)
    
    start = time.time()
    
    while time.time() - start < 60: # Run for 60s
        
        # Action 1: Move Camera (Explore)
        if random.random() < 0.6:
            move_camera_randomly()
            
        # Action 2: Move Hero (Walk to where we are looking)
        # We click multiple times to ensure we hit walkability
        for _ in range(3):
            click_random_screen_spot()
            time.sleep(0.3)
            
        # Action 3: Center (Occasional check)
        if random.random() < 0.2:
            print("[FREEROAM v2] Re-centering (F1).")
            pyautogui.press('f1')
            time.sleep(0.5)
            
        time.sleep(1.0)

    print("[FREEROAM v2] Routine Complete.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    navigation_repair_routine()

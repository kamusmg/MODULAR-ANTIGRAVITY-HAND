import pyautogui
import time

# Configuration
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def focus_game():
    pyautogui.click(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    time.sleep(1.0)

def center_hero():
    print("[TOP LANE] Centering Camera (F1)...")
    pyautogui.press('f1')
    time.sleep(0.1)
    pyautogui.press('f1')
    time.sleep(1.0)

def march_step(step_num):
    print(f"[TOP LANE] Step {step_num}: Moving Camera UP/LEFT...")
    
    # Radiant Top Lane is UP and LEFT from the fountain.
    # We hold keys to shift camera.
    
    pyautogui.keyDown('up')
    pyautogui.keyDown('left')
    time.sleep(1.5) # Shift view by ~one screen path
    pyautogui.keyUp('up')
    pyautogui.keyUp('left')
    time.sleep(0.5)
    
    # Click Center to Walk
    print(f"[TOP LANE] Step {step_num}: Walking...")
    pyautogui.rightClick(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    # Wait for hero to arrive (travel time)
    time.sleep(5.0)

def top_lane_routine():
    print("[TOP LANE] Initiating March to Top Lane (Radiant)...")
    
    focus_game()
    center_hero()
    
    # Execute a sequence of 10 steps
    # This should be enough to get from Fountain -> Tier 2 -> Tier 1 Tower
    for i in range(1, 11):
        march_step(i)
        
        # Occasional action to keep things alive
        if i % 3 == 0:
            print("[TOP LANE] Action: Fire Breath (Checking for creeps)")
            pyautogui.press('q')
            time.sleep(0.5)

    print("[TOP LANE] Destination Reached (Approximate).")
    center_hero()

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    top_lane_routine()

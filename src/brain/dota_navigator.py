import pyautogui
import time
import random

def dota_navigate():
    print("[NAVIGATOR BRAIN] Calibrating Compass...")
    
    w, h = pyautogui.size()
    center_x, center_y = w // 2, h // 2
    
    # Coordinates for Edge Panning (Bot Lane is usually Bottom-Right for Radiant, Top-Right for Dire)
    # Assuming standard Radiant Bot Lane run (Bottom Right direction)
    pan_x = w - 10 # Right Edge
    pan_y = h - 10 # Bottom Edge
    
    # 1. Focus & Recenter
    print("[NAVIGATOR BRAIN] centering Camera (F1)...")
    pyautogui.click(center_x, center_y)
    pyautogui.press('f1')
    pyautogui.press('f1') # Double tap often locks or ensures center
    time.sleep(1.0)
    
    def move_segment(direction_name, px, py):
        print(f"[NAVIGATOR BRAIN] Panning Camera: {direction_name}...")
        
        # Move mouse to edge to pan camera
        pyautogui.moveTo(px, py) 
        time.sleep(0.8) # Hold to pan (slightly faster)
        
        # Move mouse back to SAFE GROUND (avoiding HUD/Shop/Courier)
        # The user said "a bit more up".
        # HUD is roughly bottom 20% of screen. 
        # Screen height usually 1080.
        # Safe clickable area is roughly center-right or center-bottom-ish but high up.
        
        click_x = px - 200 # Move left from right edge
        click_y = py - 400 # Move WAY UP from bottom edge (avoid inventory completely)
        
        print(f"[NAVIGATOR BRAIN] Moving Hero -> {direction_name}")
        pyautogui.rightClick(click_x, click_y)
        
        # Recentering is NOT done here, we want the camera to advance
        time.sleep(2.0) # Walk time

    # Execute the "Bot Lane Push" sequence
    # We will pan and click 10 times to travel a long distance
    for i in range(10):
        # We start by panning DOWN-RIGHT (Bot Lane)
        move_segment(f"Bot Lane Step {i+1}", w - 50, h - 50)
        
        # Occasionally press F1 to check if we are still alive/selected, then pan again
        if i % 3 == 0:
            print("[NAVIGATOR BRAIN] Checking Hero Status (F1)...")
            pyautogui.press('f1') # Re-center on hero
            time.sleep(0.5)

    print("[NAVIGATOR BRAIN] Destination reached (hopefully).")
    pyautogui.press('enter')
    pyautogui.write("Nucleus: Cheguei na Bot Lane?", interval=0.05)
    pyautogui.press('enter')

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    dota_navigate()

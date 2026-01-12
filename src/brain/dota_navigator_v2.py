import pyautogui
import time
import random

# Configuration
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Minimap is roughly bottom-left corner.
# Let's estimate the clickable area for the Minimap.
# Bottom-Left: (0, 1080)
# Top-Right of Minimap: approx (260, 860) ? 
# Let's use conservative "safe" spots on the minimap.

MINIMAP_LOCATIONS = {
    "RADIANT_BASE": (50, 1030),
    "DIRE_BASE": (240, 850),
    "MID_LANE": (150, 940),
    "TOP_LANE": (50, 850),
    "BOT_LANE": (240, 1030)
}

def center_hero():
    print("[NAV V2] Centering Camera (F1 F1)...")
    pyautogui.press('f1')
    time.sleep(0.1)
    pyautogui.press('f1')
    time.sleep(1.0)

def edge_pan(direction, duration=1.0):
    print(f"[NAV V2] Panning Camera {direction}...")
    w, h = SCREEN_WIDTH, SCREEN_HEIGHT
    
    if direction == "LEFT":
        pyautogui.moveTo(5, h//2)
    elif direction == "RIGHT":
        pyautogui.moveTo(w-5, h//2)
    elif direction == "UP":
        pyautogui.moveTo(w//2, 5)
    elif direction == "DOWN":
        pyautogui.moveTo(w//2, h-5)
        
    time.sleep(duration)
    # Return to center to stop panning
    pyautogui.moveTo(w//2, h//2)

def move_via_minimap(location_name):
    if location_name not in MINIMAP_LOCATIONS:
        return
        
    x, y = MINIMAP_LOCATIONS[location_name]
    print(f"[NAV V2] Moving via Minimap to {location_name} ({x}, {y})...")
    
    # Right click on the minimap
    pyautogui.rightClick(x, y)
    time.sleep(0.5)
    
    # Confirm command
    print("[NAV V2] Move command issued.")

def navigate_routine():
    print("[NAV V2] Initiating Advanced Navigation Protocol...")
    
    # 1. Focus Game
    pyautogui.click(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    time.sleep(1.0)
    
    # 2. Center
    center_hero()
    
    # 3. Minimap Travel Sequence
    destinations = ["MID_LANE", "DIRE_BASE", "TOP_LANE", "BOT_LANE", "RADIANT_BASE"]
    
    for dest in destinations:
        move_via_minimap(dest)
        
        # While moving, look around with camera
        start_move = time.time()
        while time.time() - start_move < 8: # Wait 8 seconds for travel
            if random.random() < 0.3:
                # Random Pan
                direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
                edge_pan(direction, duration=0.5)
            time.sleep(1.0)
            
        # Re-center to check on Hero
        center_hero()
        # Maybe breathe fire?
        pyautogui.press('q')
        time.sleep(1.0)

    print("[NAV V2] Navigation Test Complete.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    navigate_routine()

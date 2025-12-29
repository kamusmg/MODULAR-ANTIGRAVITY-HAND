import pyautogui
import time
import random

def dragon_dance():
    print("[DOTA BRAIN] Waking up in the Arena...")
    
    # 1. Focus Game (Click Center)
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    
    print("[DOTA BRAIN] Focusing Window...")
    pyautogui.click(center_x, center_y)
    time.sleep(1.0)
    
    # 2. The Dance Routine
    print("[DOTA BRAIN] Commencing 'Dragon Dance'...")
    
    actions = ['move', 'q', 'w', 's', 'stop']
    
    # Run for ~30 seconds of freedom
    start_time = time.time()
    
    while time.time() - start_time < 30:
        action = random.choice(actions)
        
        if action == 'move':
            # Move near center (random offset)
            offset_x = random.randint(-400, 400)
            offset_y = random.randint(-300, 300)
            target_x = center_x + offset_x
            target_y = center_y + offset_y
            
            print(f"[DOTA BRAIN] Moving to ({target_x}, {target_y})")
            pyautogui.rightClick(target_x, target_y)
            time.sleep(random.uniform(0.5, 1.5))
            
        elif action == 'q':
            # Breathe Fire (Point Text)
            # Usually targets cursor. Let's aim at a random spot.
            aim_x = center_x + random.randint(-200, 200)
            aim_y = center_y + random.randint(-200, 200)
            pyautogui.moveTo(aim_x, aim_y)
            
            print("[DOTA BRAIN] CAST: Breathe Fire (Q)")
            pyautogui.press('q')
            time.sleep(0.5) # Cast animation
            
        elif action == 'w':
            # Dragon Tail (Melee Stun)
            print("[DOTA BRAIN] CAST: Dragon Tail (W)")
            pyautogui.press('w')
            time.sleep(0.5)
            
        elif action == 's' or action == 'stop':
            # Stop command (cancel animation/movement)
            print("[DOTA BRAIN] ACTION: Stop (S)")
            pyautogui.press('s')
            time.sleep(0.3)
            
    print("[DOTA BRAIN] Dance Complete. Awaiting orders.")

if __name__ == "__main__":
    # Safety: Fail-safe
    pyautogui.FAILSAFE = True
    dragon_dance()

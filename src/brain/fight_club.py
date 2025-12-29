import pyautogui
import time
import random

def fight_club():
    print("[FIGHT BRAIN] Enter the Arena...")
    
    # 1. Focus Game
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.click(center_x, center_y)
    time.sleep(1.0)
    
    # 2. Battle Logic
    # Assumption: User has both heroes selected or use TAB to cycle
    # We will spam TAB to switch between DK and Kunkka
    
    print("[FIGHT BRAIN] ROUND 1: FIGHT!")
    
    start_time = time.time()
    while time.time() - start_time < 40: # 40 seconds of chaos
        
        # --- HERO A (Current) ---
        print("[FIGHT BRAIN] Hero A Action")
        # Attack Move Center (Aggression)
        pyautogui.press('a')
        pyautogui.click(center_x + random.randint(-50, 50), center_y + random.randint(-50, 50))
        
        # Cast Random Spell (Q-W-E-R) at Center
        spell = random.choice(['q', 'w', 'e', 'r'])
        print(f"[FIGHT BRAIN] Casting {spell.upper()}")
        
        # Aim 
        pyautogui.moveTo(center_x + random.randint(-100, 100), center_y + random.randint(-100, 100))
        pyautogui.press(spell)
        time.sleep(0.3)
        
        # --- SWITCH HERO ---
        print("[FIGHT BRAIN] SWITCHING (TAB)")
        pyautogui.press('tab')
        time.sleep(0.2)
        
        # --- HERO B (Next) ---
        print("[FIGHT BRAIN] Hero B Action")
        pyautogui.press('a')
        pyautogui.click(center_x + random.randint(-50, 50), center_y + random.randint(-50, 50))
        
        # Cast Random Spell
        spell = random.choice(['q', 'w', 'e', 'r'])
        print(f"[FIGHT BRAIN] Casting {spell.upper()}")
        pyautogui.moveTo(center_x + random.randint(-100, 100), center_y + random.randint(-100, 100))
        pyautogui.press(spell)
        time.sleep(0.3)
        
        # Chaos Factor: Sometimes spam stop to fake-cast
        if random.random() < 0.2:
            pyautogui.press('s')
            
    print("[FIGHT BRAIN] KO! Match ended.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    fight_club()

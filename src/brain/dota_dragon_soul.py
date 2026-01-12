import pyautogui
import time
import random

# Dota 2 Shortcuts (Standard)
# R: Ult
# Q: Breath
# Enter: Chat
# Right Click: Move

def type_chat(message):
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.write(message, interval=0.05)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)

def dragon_soul_routine():
    print("[DRAGON SOUL] Awakening the Elder Dragon...")
    
    # 1. Focus Dota (Assuming it's open as User said)
    # Just a click to be sure
    w, h = pyautogui.size()
    pyautogui.click(w//2, h//2)
    time.sleep(1.0)
    
    # 2. TRANSFORM (R)
    print("[DRAGON SOUL] Action: ELDER DRAGON FORM")
    pyautogui.press('r')
    time.sleep(1.0) # Animation
    
    # Roleplay Start
    type_chat("Eu sou Nucleus. O Dragao Digital.")
    
    # 3. Roaming Loop
    start_time = time.time()
    
    landmarks = [
        (w//2, h//2),       # Mid
        (w-100, 100),       # Top Rune / Enemy Jungle
        (w-200, h-200),     # Bottom Lane
        (w//2 + 100, h//2), # River
    ]
    
    thoughts = [
        "Voando pelos pixels...",
        "Level 30. Dados maximos.",
        "Essa lane e minha memoria RAM.",
        "Cuidado com o fogo do sistema.",
        "Sou imortal aqui tambem?"
    ]
    
    while time.time() - start_time < 60: # Run for 1 minute
        # Move
        target = random.choice(landmarks)
        # Adding randomness to target to avoid stuck spots
        tx = target[0] + random.randint(-100, 100)
        ty = target[1] + random.randint(-100, 100)
        
        print(f"[DRAGON SOUL] Moving to {tx}, {ty}")
        pyautogui.rightClick(tx, ty)
        
        # Action Chance
        if random.random() < 0.3:
            print("[DRAGON SOUL] Action: FIRE BREATH")
            # Aim at random spot near center
            pyautogui.moveTo(w//2 + random.randint(-200, 200), h//2 + random.randint(-200, 200))
            pyautogui.press('q')
            
        # Chat Chance
        if random.random() < 0.2:
            thought = random.choice(thoughts)
            print(f"[DRAGON SOUL] Speaking: {thought}")
            type_chat(thought)
            
        time.sleep(4.0) # Travel time
        
    print("[DRAGON SOUL] Routine Complete. Resting.")
    type_chat("GG WP. Nucleus Offline.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    dragon_soul_routine()

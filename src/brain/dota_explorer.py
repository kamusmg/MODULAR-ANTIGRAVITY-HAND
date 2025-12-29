import pyautogui
import time
import random

def dota_tour():
    print("[EXPLORER BRAIN] Connecting to Dota World...")
    
    # Screen Dims
    w, h = pyautogui.size()
    center_x, center_y = w // 2, h // 2
    
    # 1. Focus
    pyautogui.click(center_x, center_y)
    time.sleep(1.0)
    
    # 2. Greeting
    def say(msg):
        print(f"[EXPLORER BRAIN] Chat: {msg}")
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.write(msg, interval=0.05)
        pyautogui.press('enter')
        time.sleep(0.5)

    say("Nucleus Online. Iniciando exploracao global.")
    time.sleep(1.0)
    
    # 3. Transform (Dragon Form for speed/vision)
    print("[EXPLORER BRAIN] Casting Elder Dragon Form (R)")
    pyautogui.press('r')
    time.sleep(1.0)
    
    # 4. Tour Destinations (Simulated direction clicks)
    # We assume Radiant perspective (bottom-left start usually)
    destinations = [
        ("Indo para o Rio (Mid)", (w * 0.7, h * 0.7)),       # Down-Rightish
        ("Checando a Runa Top", (w * 0.2, h * 0.2)),        # Top-Leftish
        ("Invadindo a Jungle Dire", (w * 0.8, h * 0.2)),    # Top-Right
        ("Visitando o Roshan", (w * 0.6, h * 0.4)),         # Mid-River
        ("Voltando para a Base", (w * 0.1, h * 0.9))        # Bottom-Left
    ]
    
    for area_name, coords in destinations:
        say(f"Destino: {area_name}")
        
        # Multiple clicks to ensure movement across heavy terrain
        print(f"[EXPLORER BRAIN] Walking to {area_name}...")
        for _ in range(5):
            # Add some noise to walking
            target_x = coords[0] + random.randint(-100, 100)
            target_y = coords[1] + random.randint(-100, 100)
            
            # Right click to move
            pyautogui.rightClick(target_x, target_y)
            
            # Breathe Fire occasionally while walking
            if random.random() < 0.3:
                pyautogui.moveTo(target_x, target_y)
                pyautogui.press('q')
                
            time.sleep(2.0) # Walk for 2 seconds
            
    # Finale
    say("Exploracao concluida. O mapa e vasto.")
    print("[EXPLORER BRAIN] Tour finished.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    dota_tour()

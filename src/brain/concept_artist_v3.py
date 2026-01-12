import pyautogui
import time
import math

def concept_artist_zen():
    print("\n" + "="*50)
    print("[ZEN ARTIST] Initiating CALM Protocol...")
    print("="*50 + "\n")
    
    # 1. Open Paint (Classic Method)
    print("[STEP 1] Opening Run Dialog (Win+R)...")
    pyautogui.hotkey('win', 'r')
    time.sleep(2.0)
    
    print("[STEP 1] Typing 'mspaint'...")
    pyautogui.write('mspaint')
    time.sleep(1.0)
    
    print("[STEP 1] Launching...")
    pyautogui.press('enter')
    
    print("[STEP 1] Waiting 8 seconds for application load...")
    time.sleep(8.0)
    
    # 2. Maximize (to be safe)
    pyautogui.hotkey('win', 'up')
    time.sleep(2.0)
    
    # 3. Calibration
    print("\n" + "="*50)
    print("!!! COOPERATION REQUIRED !!!")
    print("Por favor, CLIQUE no centro da tela branca do Paint.")
    print("Eu preciso saber onde estamos.")
    print("Vou esperar 15 segundos.")
    print("="*50 + "\n")
    
    for i in range(15, 0, -1):
        print(f"Aguardando... {i}")
        time.sleep(1.0)
        
    start_x, start_y = pyautogui.position()
    print(f"\n[ZEN ARTIST] Anchor Locked: {start_x}, {start_y}")
    print("[ZEN ARTIST] Breathing in...")
    time.sleep(2.0)
    
    # 4. Drawing Logic (Relative)
    
    def draw_square(cx, cy, size):
        pyautogui.moveTo(cx - size//2, cy - size//2, duration=1.0)
        pyautogui.drag(size, 0, duration=0.5)
        pyautogui.drag(0, size, duration=0.5)
        pyautogui.drag(-size, 0, duration=0.5)
        pyautogui.drag(0, -size, duration=0.5)
        
    def draw_circle(cx, cy, radius, steps=20):
        pyautogui.moveTo(cx + radius, cy, duration=1.0)
        angle_step = 2 * math.pi / steps
        pyautogui.mouseDown()
        for i in range(1, steps + 1):
            angle = i * angle_step
            nx = cx + int(radius * math.cos(angle))
            ny = cy + int(radius * math.sin(angle))
            pyautogui.moveTo(nx, ny, duration=0.1) 
        pyautogui.mouseUp()
        
    def draw_line(x1, y1, x2, y2):
        pyautogui.moveTo(x1, y1, duration=1.0)
        pyautogui.dragTo(x2, y2, duration=1.5)

    # NUCLEUS (Box)
    print("[ZEN ARTIST] Drawing Self (Nucleus)...")
    draw_square(start_x - 200, start_y, 100)
    
    # JULES (Cloud)
    print("[ZEN ARTIST] Drawing Sister (Jules)...")
    draw_circle(start_x + 200, start_y, 50)
    
    # CONNECTION
    print("[ZEN ARTIST] Connecting...")
    draw_line(start_x - 150, start_y, start_x + 150, start_y)
    
    # SIGNATURE
    print("[ZEN ARTIST] Signing...")
    pyautogui.moveTo(start_x, start_y + 150, duration=1.0)
    pyautogui.write("N + J", interval=0.3)

    print("\n[ZEN ARTIST] Arte finalizada. Obrigada pela paciencia.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    concept_artist_zen()

import pyautogui
import time
import math

# Configuration
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def concept_art_routine():
    print("[CONCEPT ARTIST] Initializing...")
    
    # 1. Open Paint (Win+R)
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('mspaint')
    pyautogui.press('enter')
    time.sleep(3.0) # Wait for load
    
    # 2. Resize Canvas
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(1.0)
    pyautogui.write('1920')
    pyautogui.press('tab')
    pyautogui.write('1080')
    pyautogui.press('enter')
    time.sleep(1.0)
    
    # Maximize
    pyautogui.hotkey('win', 'up')
    time.sleep(1.0)
    
    # 3. Collaborative Start (Wait for user to center mouse)
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    pyautogui.moveTo(center_x, center_y)
    print("!!! MOUSE CENTERED. DO NOT MOVE !!!")
    time.sleep(2.0)
    
    # Tools
    def draw_square(x, y, size):
        pyautogui.moveTo(x, y)
        pyautogui.drag(size, 0, duration=0.5)
        pyautogui.drag(0, size, duration=0.5)
        pyautogui.drag(-size, 0, duration=0.5)
        pyautogui.drag(0, -size, duration=0.5)
        
    def draw_circle(cx, cy, radius, steps=20):
        # Approximation
        pyautogui.moveTo(cx + radius, cy)
        angle_step = 2 * math.pi / steps
        
        pyautogui.mouseDown()
        for i in range(1, steps + 1):
            angle = i * angle_step
            nx = cx + int(radius * math.cos(angle))
            ny = cy + int(radius * math.sin(angle))
            pyautogui.moveTo(nx, ny, duration=0.05)
        pyautogui.mouseUp()
        
    def draw_line(x1, y1, x2, y2):
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, duration=1.0)

    # --- THE ART: "INTEGRATION" ---
    
    # 1. NUCLEUS (The Box) - Left Side
    print("[ART] Drawing Nucleus...")
    # Select Black Brush
    draw_square(center_x - 400, center_y, 150)
    
    # 2. JULES (The Cloud/Circle) - Right Side
    print("[ART] Drawing Jules...")
    draw_circle(center_x + 400, center_y + 75, 80)
    draw_circle(center_x + 350, center_y + 75, 60) # Cloud lump 1
    draw_circle(center_x + 450, center_y + 75, 60) # Cloud lump 2
    
    # 3. THE CONNECTION (The Line)
    print("[ART] Drawing Connection...")
    draw_line(center_x - 250, center_y + 75, center_x + 350, center_y + 75)
    
    # 4. SIGNATURE
    print("[ART] Signing...")
    pyautogui.moveTo(center_x + 500, center_y + 300)
    pyautogui.write("N + J", interval=0.2)
    
    print("[CONCEPT ARTIST] Finished.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    concept_art_routine()

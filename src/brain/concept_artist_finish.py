import pyautogui
import time
import math

def concept_artist_finish():
    print("\n" + "="*50)
    print("[ARTIST FINAL] Initiating Completion Protocol...")
    print("="*50 + "\n")
    
    # Assumption: Paint is already open (since user just showed it)
    # But we will focus it.
    
    print("[STEP 1] Focusing Paint (Click Center in 10s)...")
    print("!!! INSTRUCTION: Position mouse at the CENTER of the drawing (on the line) !!!")
    print("!!! I will redraw everything over it or next to it. !!!")
    
    for i in range(10, 0, -1):
        print(f"Calibrating in {i}...")
        time.sleep(1.0)
        
    start_x, start_y = pyautogui.position()
    pyautogui.click() # Focus
    print(f"[ART] Anchor: {start_x}, {start_y}")
    
    # Tools using explicit DRAG
    
    def draw_square(cx, cy, size):
        print(f" - Square at {cx}, {cy}")
        pyautogui.moveTo(cx - size//2, cy - size//2, duration=0.5)
        pyautogui.drag(size, 0, duration=0.5, button='left')
        time.sleep(0.1)
        pyautogui.drag(0, size, duration=0.5, button='left')
        time.sleep(0.1)
        pyautogui.drag(-size, 0, duration=0.5, button='left')
        time.sleep(0.1)
        pyautogui.drag(0, -size, duration=0.5, button='left')
        time.sleep(0.1)
        
    def draw_circle(cx, cy, radius, steps=30):
        print(f" - Circle at {cx}, {cy}")
        # Start at rightmost point
        pyautogui.moveTo(cx + radius, cy, duration=0.5)
        
        angle_step = 2 * math.pi / steps
        
        # WE USE DRAG TO for every step to ensure ink flow
        # This is choppier but safer than mouseDown + moveTo
        
        pyautogui.mouseDown(button='left')
        for i in range(1, steps + 1):
            angle = i * angle_step
            nx = cx + int(radius * math.cos(angle))
            ny = cy + int(radius * math.sin(angle))
            pyautogui.dragTo(nx, ny, duration=0.15, button='left') 
        pyautogui.mouseUp(button='left')
        
    def draw_line(x1, y1, x2, y2):
        print(" - Connecting...")
        pyautogui.moveTo(x1, y1, duration=0.5)
        pyautogui.dragTo(x2, y2, duration=1.0, button='left')

    # RE-DRAWING EVERYTHING TO BE SURE
    
    # 1. NUCLEUS (Box)
    print("[ART] Drawing Nucleus (Square)...")
    draw_square(start_x - 200, start_y, 100)
    
    # 2. CONNECTION (Line)
    print("[ART] Drawing Connection (Line)...")
    draw_line(start_x - 150, start_y, start_x + 150, start_y)
    
    # 3. JULES (Circle) - THIS WAS MISSING
    print("[ART] Drawing Jules (Circle)...")
    draw_circle(start_x + 200, start_y, 50)
    
    # Cloud Lumps (Optional, skipping for clarity/success chance)
    
    # 4. SIGNATURE - THIS WAS MISSING
    print("[ART] Signing...")
    # N
    pyautogui.moveTo(start_x, start_y + 100, duration=0.5)
    pyautogui.drag(0, -40, duration=0.2, button='left') # Up
    pyautogui.drag(20, 40, duration=0.2, button='left') # Diag
    pyautogui.drag(0, -40, duration=0.2, button='left') # Up
    
    # +
    pyautogui.moveTo(start_x + 30, start_y + 80, duration=0.2)
    pyautogui.drag(20, 0, duration=0.2, button='left') # -
    pyautogui.moveTo(start_x + 40, start_y + 70, duration=0.2)
    pyautogui.drag(0, 20, duration=0.2, button='left') # |
    
    # J
    pyautogui.moveTo(start_x + 60, start_y + 60, duration=0.2)
    pyautogui.drag(0, 40, duration=0.2, button='left') # Down
    pyautogui.drag(-15, 10, duration=0.2, button='left') # Hook

    print("[ARTIST FINAL] Finished. Verify Jules.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    concept_artist_finish()

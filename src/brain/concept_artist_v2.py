import pyautogui
import time
import math

def concept_art_routine_v2():
    print("[CONCEPT ARTIST v2] Initializing...")
    print("[INSTRUCTION] Please ensure MS Paint is OPEN and active.")
    
    # Collaborative Start (Wait for user to center mouse)
    print("!!! PLEASE MOVE MOUSE TO THE CENTER OF THE WHITE CANVAS !!!")
    print("I will lock onto your position in 5 seconds...")
    
    for i in range(5, 0, -1):
        print(f"Calibrating in {i}...")
        time.sleep(1.0)
        
    start_x, start_y = pyautogui.position()
    print(f"[ART] Locked Anchor Point at: {start_x}, {start_y}")
    
    # Focus click
    pyautogui.click()
    
    # Tools
    def draw_square(cx, cy, size):
        # Top Left start
        pyautogui.moveTo(cx - size//2, cy - size//2)
        pyautogui.drag(size, 0, duration=0.2)
        pyautogui.drag(0, size, duration=0.2)
        pyautogui.drag(-size, 0, duration=0.2)
        pyautogui.drag(0, -size, duration=0.2)
        
    def draw_circle(cx, cy, radius, steps=20):
        # Start at 0 degrees (Right)
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
        pyautogui.dragTo(x2, y2, duration=0.5)

    # --- THE ART: "INTEGRATION" (Relative to start_x, start_y) ---
    
    # 1. NUCLEUS (The Box) - Left Side
    print("[ART] Drawing Nucleus...")
    draw_square(start_x - 300, start_y, 150)
    
    # 2. JULES (The Cloud/Circle) - Right Side
    print("[ART] Drawing Jules...")
    draw_circle(start_x + 300, start_y, 80)
    draw_circle(start_x + 250, start_y, 60) # Cloud lump 1
    draw_circle(start_x + 350, start_y, 60) # Cloud lump 2
    
    # 3. THE CONNECTION (The Line)
    print("[ART] Drawing Connection...")
    draw_line(start_x - 225, start_y, start_x + 225, start_y)
    
    # 4. SIGNATURE
    print("[ART] Signing...")
    pyautogui.moveTo(start_x + 200, start_y + 200)
    # Simple write doesn't work well for "drawing" text without text tool, 
    # but let's try to drag-write initials briefly or just use text tool if simple.
    # Actually, drag-writing N J is safer than text tool guessing.
    
    # N
    pyautogui.drag(0, -50, duration=0.2) # Up
    pyautogui.drag(30, 50, duration=0.2) # diag
    pyautogui.drag(0, -50, duration=0.2) # Up
    
    pyautogui.move(20, 50) # Space
    
    # +
    pyautogui.drag(30, 0, duration=0.2) # -
    pyautogui.move(-15, -15)
    pyautogui.drag(0, 30, duration=0.2) # |
    
    pyautogui.move(30, -15) # Space
    
    # J
    pyautogui.move(30, 0) # Top right of J
    pyautogui.drag(0, 50, duration=0.2) # Down
    pyautogui.drag(-20, 10, duration=0.2) # Hook
    
    print("[CONCEPT ARTIST v2] Finished.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    concept_art_routine_v2()

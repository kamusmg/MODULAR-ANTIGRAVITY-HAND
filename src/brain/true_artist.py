import pyautogui
import time
import math
import sys

def true_artist():
    print("\n" + "="*50)
    print("[TRUE ARTIST] Initializing Visual Verification Protocol...")
    print("="*50 + "\n")
    
    # 1. LAUNCH PAINT
    print("[STEP 1] Launching Paint...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('mspaint')
    pyautogui.press('enter')
    
    print("[STEP 1] Waiting 5s for Paint to appear...")
    time.sleep(5.0)
    
    # Maximize ensures better target area
    pyautogui.hotkey('win', 'up')
    time.sleep(1.0)
    
    # 2. VISUAL HANDSHAKE (Pixel Peeping)
    print("\n" + "="*50)
    print("!!! VISION CHECK !!!")
    print("Please move your mouse to the WHITE CANVAS.")
    print("I will sample the color under your cursor.")
    print("I will ONLY start if I see PURE WHITE (255, 255, 255).")
    print("="*50 + "\n")
    
    verified_x = 0
    verified_y = 0
    success = False
    
    for i in range(20): # 20 attempts
        x, y = pyautogui.position()
        try:
            # We take a screenshot of 1x1 pixel to check color
            # getting pixel directly can vary by OS, checking screenshot is robust
            color = pyautogui.pixel(x, y)
            print(f"Checking ({x}, {y})... Color: {color}")
            
            if color[0] > 250 and color[1] > 250 and color[2] > 250:
                print(">>> WHITE DETECTED! Canvas Confirmed.")
                verified_x = x
                verified_y = y
                success = True
                
                # Visual Confirmation (Wiggle)
                pyautogui.move(10, 0)
                pyautogui.move(-20, 0)
                pyautogui.move(10, 0)
                break
            else:
                 print("... Not white yet. Waiting...")
        except Exception as e:
            print(f"Vision Error: {e}")
            
        time.sleep(1.0)
        
    if not success:
        print("[ERROR] Could not verify canvas. Aborting to prevent blind drawing.")
        sys.exit(1)
        
    # 3. DRAWING (Relative to Verified Anchor)
    print(f"[ART] Anchor Locked at {verified_x}, {verified_y}. Starting in 2s...")
    time.sleep(2.0)
    pyautogui.click() # Focus click
    
    start_x = verified_x
    start_y = verified_y
    
    # Helper Functions
    def draw_square(cx, cy, size):
        print(f"Drawing Square at {cx},{cy}")
        pyautogui.moveTo(cx - size//2, cy - size//2, duration=0.5)
        pyautogui.drag(size, 0, duration=0.5, button='left')
        pyautogui.drag(0, size, duration=0.5, button='left')
        pyautogui.drag(-size, 0, duration=0.5, button='left')
        pyautogui.drag(0, -size, duration=0.5, button='left')
        
    def draw_circle(cx, cy, radius, steps=30):
        print(f"Drawing Circle at {cx},{cy}")
        pyautogui.moveTo(cx + radius, cy, duration=0.5)
        angle_step = 2 * math.pi / steps
        pyautogui.mouseDown(button='left')
        for i in range(1, steps + 1):
            angle = i * angle_step
            nx = cx + int(radius * math.cos(angle))
            ny = cy + int(radius * math.sin(angle))
            pyautogui.dragTo(nx, ny, duration=0.1, button='left')
        pyautogui.mouseUp(button='left')
        
    def draw_line(x1, y1, x2, y2):
        print("Drawing Line...")
        pyautogui.moveTo(x1, y1, duration=0.5)
        pyautogui.dragTo(x2, y2, duration=1.0, button='left')

    # EXECUTION
    # 1. NUCLEUS (Box)
    draw_square(start_x - 150, start_y, 100)
    
    # 2. CONNECTION (Line)
    draw_line(start_x - 100, start_y, start_x + 100, start_y)
    
    # 3. JULES (Circle)
    draw_circle(start_x + 150, start_y, 50)
    
    # 4. SIGNATURE
    pyautogui.moveTo(start_x, start_y + 100, duration=0.5)
    pyautogui.write("N+J", interval=0.2) # Trying Text tool implicit typing? 
    # Usually Paint requires clicking Text tool. 
    # Let's fallback to mouse-writing initials to be safe.
    pyautogui.move(0, 50)
    pyautogui.drag(0, -30, duration=0.2, button='left') # N leg
    pyautogui.drag(20, 30, duration=0.2, button='left') # N diag
    pyautogui.drag(0, -30, duration=0.2, button='left') # N leg

    print("[TRUE ARTIST] Masterpiece Complete.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    true_artist()

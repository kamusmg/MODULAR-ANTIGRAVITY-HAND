import pyautogui
import time
import math

def slow_portrait():
    print("[SLOW ARTIST] Initiating Sequence (v4: Full Canvas)...")
    
    # --- PHASE 1: OPENING PAINT (Robust Win+R Method) ---
    print("[SLOW ARTIST] Opening Run Dialog (Win+R)...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.5)
    
    print("[SLOW ARTIST] Typing 'mspaint' in Run dialog...")
    pyautogui.write('mspaint', interval=0.1)
    time.sleep(1.0)
    
    print("[SLOW ARTIST] Launching Paint...")
    pyautogui.press('enter')
    
    print("[SLOW ARTIST] Waiting 5 seconds for Paint to load...")
    time.sleep(5.0)
    
    # --- PHASE 2: RESIZING CANVAS (New) ---
    print("[SLOW ARTIST] Resizing Canvas to 1920x1080...")
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(1.5)
    
    # Assuming 'Width' is focused by default or we Tab to it
    # In Windows 11/10 Paint, Ctrl+E opens properties. Default focus depends.
    # Safe bet: Type numbers. If it's Unit selection (Inches/Pixels), we might need tabs.
    # Usually pixels is default.
    # Let's try: 1920 -> Tab -> 1080 -> Enter.
    
    pyautogui.write('1920')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write('1080')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2.0)
    
    # Maximize Window (just in case)
    pyautogui.hotkey('win', 'up') 
    time.sleep(1.0)

    # --- PHASE 3: POSITIONING (COLLABORATIVE) ---
    print("!!! ATENTION !!!")
    print("Please MOVE THE MOUSE to the CENTER of the WHITE CANVAS.")
    print("I will wait 10 seconds for you to position it.")
    for i in range(10, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1.0)
        
    center_x, center_y = pyautogui.position()
    print(f"[SLOW ARTIST] Locked on target at {center_x}, {center_y}.")
    
    # --- PHASE 4: DRAWING ---
    print("[SLOW ARTIST] Starting Art...")
    
    # Robust Focus Sequence
    print(" - Clicking to focus and activate brush...")
    pyautogui.click() 
    time.sleep(0.5)
    pyautogui.click() # Double tap to be sure
    time.sleep(0.5)
    pyautogui.mouseDown(button='left') # Start holding down
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')   # Release to reset state
    time.sleep(0.5)
    
    def drag_line(dx, dy):
        pyautogui.drag(dx, dy, duration=0.5, button='left')
        time.sleep(0.1) 
        
    def move_brush(dx, dy):
        pyautogui.move(dx, dy, duration=0.3)
        time.sleep(0.1)

    # Scale 
    head_size = 250
    
    # HEAD
    # Move UP significantly so the feet fit on screen
    print(f"[SLOW ARTIST] Moving UP to start position...")
    pyautogui.move(0, -400) # Moved up 400px relative to user center
    
    print(" - Head")
    drag_line(head_size, 0)
    drag_line(0, head_size)
    drag_line(-head_size, 0)
    drag_line(0, -head_size)
    
    move_brush(head_size // 2, head_size) 
    
    # BODY
    print(" - Body")
    drag_line(0, 300) 
    
    # LEGS
    print(" - Legs")
    drag_line(-100, 150)
    move_brush(100, -150)
    drag_line(100, 150)
    
    # ARMS
    print(" - Arms")
    move_brush(-100, -150) # Back to hip
    move_brush(0, -200)    # Up spine
    drag_line(-120, 50)
    move_brush(120, -50)
    drag_line(120, 50)
    
    # FACE
    pyautogui.mouseUp()
    # Go to Face Center-ish
    # Current: End of Right Arm.
    # Shoulder is at (Start_X + 125, Start_Y + 100) approx
    pyautogui.moveTo(center_x, center_y - 50, duration=0.5)
    
    # Eyes
    drag_line(20, 0) # R Eye
    move_brush(60, 0)
    drag_line(20, 0) # L Eye (mirrored perspective)
    
    print("[SLOW ARTIST] Finished.")

if __name__ == "__main__":
    slow_portrait()

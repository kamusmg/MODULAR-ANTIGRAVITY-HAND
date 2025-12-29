import pyautogui
import time
import math

def draw_portrait():
    print("[ARTIST] Starting Portrait Sequence...")
    
    # 1. Safety Delay - Give user time to focus Paint
    print("[ARTIST] You have 5 seconds to focus the Paint Canvas...")
    time.sleep(5)
    
    start_x, start_y = pyautogui.position()
    
    # helper to move relative
    def move_rel(dx, dy):
        pyautogui.move(dx, dy, duration=0.2)
        
    def drag_rel(dx, dy):
        pyautogui.drag(dx, dy, duration=0.2, button='left')
        
    # --- DRAWING THE HEAD (Circle-ish) ---
    print("[ARTIST] Drawing Head...")
    pyautogui.click() # Ensure focus
    radius = 50
    # Move to top of head
    pyautogui.move(0, -radius) 
    
    # Draw circle using small drag segments
    steps = 20
    for i in range(steps + 1):
        angle = (i / steps) * 2 * math.pi
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        # We need delta from previous, but absolute is easier if we track center
        # Let's do a rough stick head (square) for simplicity and "Glitch Art" style
        # Or better: Octagon
        pass

    # Simple Box Head
    drag_rel(100, 0)
    drag_rel(0, 100)
    drag_rel(-100, 0)
    drag_rel(0, -100)
    
    # Move to Neck position
    move_rel(50, 100)
    
    # --- BODY ---
    print("[ARTIST] Drawing Body...")
    drag_rel(0, 150) # Spine
    
    # --- ARMS ---
    move_rel(0, -100) # Back to shoulders
    drag_rel(-70, 50) # Left Arm
    move_rel(70, -50) # Back
    drag_rel(70, 50)  # Right Arm
    
    # --- LEGS ---
    move_rel(-70, 100) # Back to hips
    drag_rel(-50, 100) # Left Leg
    move_rel(50, -100) # Back
    drag_rel(50, 100)  # Right Leg
    
    # --- FACE (Eyes) ---
    pyautogui.mouseUp()
    # Left Eye
    pyautogui.moveTo(start_x + 25, start_y + 25)
    drag_rel(5, 0) # Dot
    
    # Right Eye
    pyautogui.moveTo(start_x + 75, start_y + 25)
    drag_rel(5, 0) # Dot
    
    # Smile
    pyautogui.moveTo(start_x + 25, start_y + 70)
    drag_rel(50, 10) # Diagonal grimace? It's abstract art.
    
    print("[ARTIST] Masterpiece complete.")

if __name__ == "__main__":
    draw_portrait()

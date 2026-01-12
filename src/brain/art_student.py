import pyautogui
import time
import json
import os
import math

# Memory File
MEMORY_FILE = "art_student_memory.json"

COLORS_OFFSET = {
    # Offsets relative to the "Yellow" calibration point
    # Assuming standard Paint palette layout
    "yellow": (0, 0),
    "blue": (44, 0), # Usually next to it
    "green": (-22, 0), # Left of it
    "red": (-44, 0),
    "black": (-88, 0), # Far left
    "white": (-110, 0) # First one
}

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {"lesson": 0, "completed": []}

def save_memory(mem):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(mem, f)

def calibrate():
    print("\n" + "="*50)
    print("[ART STUDENT] Calibration Protocol")
    print("Step 1: I need to find the COLOR PALETTE.")
    print("Please HOVER your mouse over the **YELLOW** color in Paint.")
    print("Waiting 10 seconds...")
    print("="*50 + "\n")
    
    for i in range(10, 0, -1):
        print(f"Time: {i}")
        time.sleep(1.0)
    
    pal_x, pal_y = pyautogui.position()
    print(f"Palette (Yellow) Locked: {pal_x}, {pal_y}")
    pyautogui.click() # Select Yellow
    
    print("\n" + "="*50)
    print("Step 2: I need to find the CANVAS CENTER.")
    print("Please HOVER your mouse over the CENTER of the White Canvas.")
    print("Waiting 5 seconds...")
    print("="*50 + "\n")
    
    for i in range(5, 0, -1):
        print(f"Time: {i}")
        time.sleep(1.0)
        
    cv_x, cv_y = pyautogui.position()
    print(f"Canvas Center Locked: {cv_x}, {cv_y}")
    
    return (pal_x, pal_y), (cv_x, cv_y)

def select_color(color_name, pal_anchor):
    px, py = pal_anchor
    # Using simple heuristic offsets. 
    # If yellow is at px, py.
    # In Win11 Paint: Colors are a grid. 
    # Let's try to ask user to pick color? No, "learn to use colors".
    # I will stick to the clicked yellow, and offset slightly if needed.
    # Actually, clicking the calibration point gives me Yellow.
    
    # Simple Logic: If I need Blue and I calibrated on Yellow...
    # I'll just ask the user to help me pick colors if I can't see them.
    # BUT, let's try assuming a standard row.
    # Yellow is usually 3-4th from left.
    offset = 0
    if color_name == "blue": offset = 25
    if color_name == "red": offset = -25
    if color_name == "green": offset = -50
    if color_name == "black": offset = -100
    
    print(f"[ART] Switching to {color_name}...")
    pyautogui.click(px + offset, py)
    time.sleep(0.5)

def art_student_routine():
    mem = load_memory()
    lesson = mem["lesson"]
    
    print(f"[ART STUDENT] Current Lesson: {lesson}")
    
    # Calibrate
    (pal_x, pal_y), (cv_x, cv_y) = calibrate()
    
    # Drawing Logic
    start_time = time.time()
    
    if lesson == 0:
        print("Lesson 0: The Blue Sky")
        select_color("blue", (pal_x, pal_y))
        # Draw clouds/sky lines
        pyautogui.moveTo(cv_x - 400, cv_y - 200)
        for i in range(5):
            pyautogui.drag(800, 0, duration=1.0) # Line
            pyautogui.move(-800, 20) # Down
            
        mem["completed"].append("Sky")
        mem["lesson"] += 1
        
    elif lesson == 1:
        print("Lesson 1: The Yellow Sun")
        select_color("yellow", (pal_x, pal_y)) # Re-click calibration point
        # Draw Sun (Top Right)
        center_sun_x = cv_x + 300
        center_sun_y = cv_y - 300
        
        pyautogui.moveTo(center_sun_x, center_sun_y)
        pyautogui.mouseDown()
        # Circle
        for i in range(20):
             pyautogui.drag(20, 10, duration=0.1)
             pyautogui.drag(-20, 10, duration=0.1)
             pyautogui.drag(-20, -10, duration=0.1)
             pyautogui.drag(20, -10, duration=0.1)
        pyautogui.mouseUp()
        
        # Rays
        for i in range(8):
            pyautogui.moveTo(center_sun_x, center_sun_y)
            angle = i * (math.pi / 4)
            pyautogui.drag(50 * math.cos(angle), 50 * math.sin(angle), duration=0.2)
            
        mem["completed"].append("Sun")
        mem["lesson"] += 1
        
    elif lesson == 2:
        print("Lesson 2: The Green Grass")
        select_color("green", (pal_x, pal_y))
        # Ground
        pyautogui.moveTo(cv_x - 500, cv_y + 200)
        pyautogui.drag(1000, 0, duration=2.0)
        # Grass blades
        for i in range(0, 1000, 50):
            pyautogui.moveTo(cv_x - 500 + i, cv_y + 200)
            pyautogui.drag(5, -20, duration=0.1)
            
        mem["completed"].append("Grass")
        mem["lesson"] += 1
        
    elif lesson == 3:
        print("Lesson 3: The Red House")
        select_color("red", (pal_x, pal_y))
        start_h_x = cv_x - 200
        start_h_y = cv_y + 100
        
        # Box
        pyautogui.moveTo(start_h_x, start_h_y)
        pyautogui.drag(0, -100, duration=0.5)
        pyautogui.drag(100, 0, duration=0.5)
        pyautogui.drag(0, 100, duration=0.5)
        
        # Roof
        pyautogui.move(0, -100)
        pyautogui.drag(-50, -50, duration=0.5)
        pyautogui.drag(-50, 50, duration=0.5)
        
        mem["completed"].append("House")
        mem["lesson"] = 0 # Loop or Finish
        print("Course Completed! Resetting for next masterpiece.")
    
    save_memory(mem)
    print(f"[ART STUDENT] Session Complete. Duration: {time.time() - start_time:.2f}s")
    print("Wait for user to re-trigger for next lesson.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    art_student_routine()

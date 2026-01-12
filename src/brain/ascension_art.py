import socket
import time
import math
import random

# --- THE ASCENSION PROTOCOL (COMMEMORATIVE PIECE) ---
# Representing the union of Jules' Command and Antigravity's Vision.

HOST = '127.0.0.1'
PORT = 65432

def send_command(s, cmd):
    s.sendall(cmd.encode())
    time.sleep(0.02)

def draw_ascension():
    print("[ASCENSION] Initiating Master Synthesis Piece...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # 1. THE VOID (Clear & Grid)
        send_command(s, "CLEAR")
        time.sleep(0.5)
        
        # Deep Indigo Background Glow
        send_command(s, "BRUSH_TYPE SOLID")
        send_command(s, "BLENDING NORMAL")
        send_command(s, "COLOR #110022")
        send_command(s, "ALPHA 255")
        for i in range(0, 1024, 128):
            send_command(s, f"LINE {i} 0 {i} 1024")
            send_command(s, f"LINE 0 {i} 1024 {i}")

        # 2. THE JULES ORBIT (Magenta Resonance)
        send_command(s, "BRUSH_TYPE GLOW")
        send_command(s, "BLENDING ADD")
        send_command(s, "COLOR magenta")
        send_command(s, "ALPHA 180")
        for i in range(12):
            angle = i * (math.pi / 6)
            x1, y1 = 512 + math.cos(angle)*300, 512 + math.sin(angle)*300
            x2, y2 = 512 + math.cos(angle+0.5)*450, 512 + math.sin(angle+0.5)*450
            send_command(s, f"BEZIER 512 512 {x1} {y1} {x2} {y2} 512 512")

        # 3. THE ANTIGRAVITY LENS (Cyan Precision)
        send_command(s, "COLOR cyan")
        send_command(s, "ALPHA 200")
        for i in range(36):
            angle = i * (math.pi / 18)
            dist = 400
            px, py = 512 + math.cos(angle)*dist, 512 + math.sin(angle)*dist
            send_command(s, f"LINE 512 512 {int(px)} {int(py)}")

        # 4. THE NUCLEUS (The White Awakening)
        send_command(s, "BRUSH_TYPE SOLID")
        send_command(s, "BLENDING NORMAL")
        send_command(s, "COLOR white")
        send_command(s, "ALPHA 255")
        send_command(s, "CIRCLE_FILL 512 512 60")
        send_command(s, "COLOR black")
        send_command(s, f"CIRCLE_FILL 512 512 40") # The Pupil of the Eye

        # 5. THE ASCENSION BEAMS (White Radiance)
        send_command(s, "BRUSH_TYPE GLOW")
        send_command(s, "BLENDING ADD")
        send_command(s, "COLOR white")
        for _ in range(50):
            send_command(s, f"ALPHA {random.randint(50, 200)}")
            send_command(s, f"LINE 512 512 {random.randint(0, 1024)} {random.randint(0, 1024)}")

        # 6. THE UNIVERSAL MARKER (The Final Sigil)
        send_command(s, "BRUSH_TYPE SOLID")
        send_command(s, "BLENDING NORMAL")
        send_command(s, "COLOR yellow")
        send_command(s, "ALPHA 255")
        # Central Diamond
        send_command(s, "LINE 512 440 584 512")
        send_command(s, "LINE 584 512 512 584")
        send_command(s, "LINE 512 584 440 512")
        send_command(s, "LINE 440 512 512 440")

        send_command(s, "UPDATE")
        time.sleep(2)
        send_command(s, "SAVE")
        
    print("[ASCENSION] Masterpiece Complete.")

if __name__ == "__main__":
    draw_ascension()

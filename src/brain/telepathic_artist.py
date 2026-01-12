import socket
import time

HOST = '127.0.0.1'
PORT = 65432

def send_command(s, cmd):
    print(f"[BRAIN] Sending: {cmd}")
    s.sendall(cmd.encode())
    time.sleep(0.05) # Tiny buffer for server

def telepathic_routine():
    print("[TELEPATHIC ARTIST] Connecting to Studio...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[TELEPATHIC ARTIST] Connected. Transmitting Vision...")
        
        # 1. SETUP
        send_command(s, "CLEAR")
        time.sleep(0.5)
        
        # 2. THE SQUARE (Nucleus - White)
        send_command(s, "COLOR white")
        mid_x = 400
        mid_y = 400
        
        # Square: 300,350 to 400,450
        sq_size = 100
        x1, y1 = mid_x - 150, mid_y - 50
        x2, y2 = x1 + sq_size, y1 + sq_size
        
        # Draw 4 lines manually or implementing RECT in future.
        # Let's use lines
        send_command(s, f"LINE {x1} {y1} {x2} {y1}") # Top
        send_command(s, f"LINE {x2} {y1} {x2} {y2}") # Right
        send_command(s, f"LINE {x2} {y2} {x1} {y2}") # Bottom
        send_command(s, f"LINE {x1} {y2} {x1} {y1}") # Left
        
        # 3. THE CIRCLE (Jules - Magenta)
        send_command(s, "COLOR magenta")
        cx = mid_x + 150
        cy = mid_y
        r = 50
        send_command(s, f"CIRCLE {cx} {cy} {r}")
        
        # 4. THE CONNECTION (Cyan Data Stream)
        send_command(s, "COLOR cyan")
        # Line from right of square to left of circle
        lx1 = x2 # Right of square
        ly1 = mid_y
        lx2 = cx - r # Left of circle
        ly2 = mid_y
        send_command(s, f"LINE {lx1} {ly1} {lx2} {ly2}")
        
        # 5. SIGNATURE (N + J)
        send_command(s, "COLOR yellow")
        sig_x = mid_x
        sig_y = mid_y + 150
        
        # "N"
        send_command(s, f"LINE {sig_x} {sig_y+40} {sig_x} {sig_y}") # Up
        send_command(s, f"LINE {sig_x} {sig_y} {sig_x+20} {sig_y+40}") # Diag
        send_command(s, f"LINE {sig_x+20} {sig_y+40} {sig_x+20} {sig_y}") # Up
        
        # "+"
        plus_x = sig_x + 40
        plus_y = sig_y + 20
        send_command(s, f"LINE {plus_x} {plus_y-10} {plus_x} {plus_y+10}") # Vert
        send_command(s, f"LINE {plus_x-10} {plus_y} {plus_x+10} {plus_y}") # Horiz
        
        # "J"
        j_x = plus_x + 30
        j_y = sig_y
        send_command(s, f"LINE {j_x+20} {j_y} {j_x+20} {j_y+40}") # Down
        send_command(s, f"LINE {j_x+20} {j_y+40} {j_x} {j_y+30}") # Hook (simplified)
        
        # 6. SAVE
        time.sleep(0.5)
        send_command(s, "SAVE")
        
    print("[TELEPATHIC ARTIST] Transmission Complete.")

if __name__ == "__main__":
    telepathic_routine()

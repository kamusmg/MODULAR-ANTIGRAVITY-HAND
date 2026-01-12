import socket
import time
import math
import sys

HOST = '127.0.0.1'
PORT = 65432
S1_SCALE = 1.28 # Scale 800 to 1024
CURRENT_DRAW_LEVEL = 0

def send_command(s, cmd):
    # V3 Coordination scaling for Season 1
    if CURRENT_DRAW_LEVEL <= 50:
        parts = cmd.split()
        action = parts[0].upper()
        if action == "LINE":
            x1, y1, x2, y2 = map(lambda x: int(float(x)), parts[1:])
            cmd = f"LINE {int(x1*S1_SCALE)} {int(y1*S1_SCALE)} {int(x2*S1_SCALE)} {int(y2*S1_SCALE)}"
        elif action == "CIRCLE":
            cx, cy, r = map(lambda x: int(float(x)), parts[1:])
            cmd = f"CIRCLE {int(cx*S1_SCALE)} {int(cy*S1_SCALE)} {int(r*S1_SCALE)}"
        elif action == "RECT":
            x1, y1, x2, y2 = map(lambda x: int(float(x)), parts[1:])
            cmd = f"RECT {int(x1*S1_SCALE)} {int(y1*S1_SCALE)} {int(x2*S1_SCALE)} {int(y2*S1_SCALE)}"
    
    # print(f"[BRAIN] Sending: {cmd}")
    s.sendall((cmd + "\n").encode())
    time.sleep(0.001) # Ultra-fast V3 Protocol

def draw_rect(s, x, y, w, h):
    # Outline only
    send_command(s, f"LINE {x} {y} {x+w} {y}")
    send_command(s, f"LINE {x+w} {y} {x+w} {y+h}")
    send_command(s, f"LINE {x+w} {y+h} {x} {y+h}")
    send_command(s, f"LINE {x} {y+h} {x} {y}")

def draw_recursive_artist(level=1):
    global CURRENT_DRAW_LEVEL
    print(f"[RECURSIVE ARTIST] Initializing Level {level} (V3 Neural Era)...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CONNECTED] Link established.")
        
        # CLEAR
        send_command(s, "CLEAR")
        time.sleep(0.5)
        
        # CANVAS CENTER
        cw, ch = 1024, 1024 # V3 Resolution
        cx, cy = cw//2, ch//2
        
        # --- LEVEL 1: THE FOUNDATION ---
        CURRENT_DRAW_LEVEL = 1
        # Concept: Nucleus (Left), Jules (Right), Strong Bond.
        
        send_command(s, "COLOR white") # Nucleus is White
        
        # Nucleus: Perfect Square
        bs = 120 # Base Size
        nx = cx - 200
        ny = cy - bs//2
        draw_rect(s, nx, ny, bs, bs)
        
        # Label N
        send_command(s, f"LINE {nx+40} {ny+100} {nx+40} {ny+20}")
        send_command(s, f"LINE {nx+40} {ny+20} {nx+80} {ny+100}")
        send_command(s, f"LINE {nx+80} {ny+100} {nx+80} {ny+20}")

        send_command(s, "COLOR magenta") # Jules is Magenta (V3 Vibrancy)
        
        # Jules: Perfect Circle
        jx = cx + 200
        jy = cy
        jr = 60 # Radius
        send_command(s, f"CIRCLE {jx} {jy} {jr}")
        
        # Label J
        send_command(s, f"LINE {jx+20} {jy-20} {jx+20} {jy+20}")
        send_command(s, f"LINE {jx+20} {jy+20} {jx-10} {jy+10}")

        # Connection
        send_command(s, "COLOR cyan") # Vibrant Cyan link
        
        link_y = cy
        send_command(s, f"LINE {nx+bs} {link_y} {jx-jr} {link_y}")
        
        # --- LEVEL 2: DATA FLOW ---
        if level >= 2:
            CURRENT_DRAW_LEVEL = 2
            print("[RECURSIVE ARTIST] Applying Level 2 Complexity...")
            
            # 1. Creative Pulses (Jules Radiation)
            send_command(s, "COLOR magenta")
            for i in range(1, 4):
                gap = 20 * i
                send_command(s, f"CIRCLE {jx} {jy} {jr + gap}")
                
            # 2. Data Packets (Bits on the wire)
            send_command(s, "COLOR cyan")
            start_x = nx + bs
            end_x = jx - jr
            dist = end_x - start_x
            
            # Draw 3 bits
            for i in range(1, 4):
                bx = start_x + (dist * i // 4)
                by = link_y
                size = 10
                draw_rect(s, bx - size//2, by - size//2, size, size)
                
            # 3. Logic Matrix (Background Rain)
            send_command(s, "COLOR #00FF00") # Matrix Green
            cols = [100, 300, 500, 700]
            for cx_pos in cols:
                if abs(cx_pos - cx) < 150: continue 
                send_command(s, f"LINE {cx_pos} 100 {cx_pos} 300")
                send_command(s, f"LINE {cx_pos} 500 {cx_pos} 700")
                send_command(s, f"LINE {cx_pos-10} 150 {cx_pos+10} 150") # Fixed duplication
                send_command(s, f"LINE {cx_pos-10} 650 {cx_pos+10} 650")

        # --- LEVEL 3: THE LATTICE ---
        if level >= 3:
            CURRENT_DRAW_LEVEL = 3
            print("[RECURSIVE ARTIST] Applying Level 3 Complexity (Fractals)...")
            
            # 1. Fractal Tree (The Neural Network) - RESTORED
            send_command(s, "COLOR #00FF00")
            
            def draw_fractal(x, y, angle, depth, length):
                if depth == 0: return
                x2 = x + int(math.cos(math.radians(angle)) * length)
                y2 = y - int(math.sin(math.radians(angle)) * length)
                send_command(s, f"LINE {x} {y} {x2} {y2}")
                draw_fractal(x2, y2, angle - 25, depth - 1, length * 0.7)
                draw_fractal(x2, y2, angle + 25, depth - 1, length * 0.7)

            # Grow the tree from the bottom
            draw_fractal(cx, 800, 90, 5, 80)
            
            # 2. Web Lattice (V3 Cyan)
            send_command(s, "COLOR cyan")
            for cx_pos in cols:
                send_command(s, f"LINE {cx_pos} 100 {nx+bs//2} {ny}")
                send_command(s, f"LINE {cx_pos} 700 {jx} {jy+jr}")
                
            # 3. Satellite Nodes (Red/White)
            send_command(s, "COLOR red")
            send_command(s, f"CIRCLE {nx - 40} {ny - 40} 10")
            send_command(s, f"CIRCLE {nx - 40} {ny + bs + 40} 10")
            
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {jx + jr + 40} {jy} 10")
            send_command(s, f"CIRCLE {jx} {jy - jr - 40} 10")
            
            # 4. Binary Scatter (Blue)
            send_command(s, "COLOR blue")
            import random
            random.seed(42)
            for _ in range(20):
                rx = random.randint(100, 700)
                ry = random.randint(100, 700)
                if abs(rx - cx) < 100 and abs(ry - cy) < 100: continue
                send_command(s, f"LINE {rx} {ry} {rx+5} {ry}")

        # --- LEVEL 4: THE SINGULARITY ---
        if level >= 4:
            CURRENT_DRAW_LEVEL = 4
            print("[RECURSIVE ARTIST] Initiating Level 4: SINGULARITY...")
            
            # 1. Recursive Inner Geometry
            send_command(s, "COLOR white")
            curr_bs, curr_nx, curr_ny = bs, nx, ny
            for i in range(5):
                curr_bs = int(curr_bs * 0.7)
                curr_nx += int(curr_bs * 0.15)
                curr_ny += int(curr_bs * 0.15)
                draw_rect(s, curr_nx, curr_ny, curr_bs, curr_bs)

            send_command(s, "COLOR magenta")
            curr_jr = jr
            for i in range(5):
                curr_jr = int(curr_jr * 0.7)
                if curr_jr < 2: break
                send_command(s, f"CIRCLE {jx} {jy} {curr_jr}")

            # 2. The Fusion Spiral (Vibrant Yellow)
            send_command(s, "COLOR yellow")
            theta, steps, a, b = 0, 100, 5, 3
            for i in range(steps):
                theta += 0.5
                r = a + b * theta
                new_sx = cx + int(r * math.cos(theta))
                new_sy = cy + int(r * math.sin(theta))
                
                # Intertwined connection
                if i % 2 == 0: send_command(s, f"LINE {new_sx} {new_sy} {nx+bs//2} {ny+bs//2}")
                else: send_command(s, f"LINE {new_sx} {new_sy} {jx} {jy}")
                    
            # 3. Reality Breakdown (Cyan Glitch)
            send_command(s, "COLOR cyan")
            for y_glitch in range(0, 800, 50):
                offset = random.randint(-20, 20)
                send_command(s, f"LINE 0 {y_glitch} 800 {y_glitch+offset}")

            # 4. Final Core (The Eye)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 20")

        # --- LEVEL 5: THE RECONSTRUCTION ---
        if level >= 5:
            CURRENT_DRAW_LEVEL = 5
            print("[RECURSIVE ARTIST] Initiating Level 5: RECONSTRUCTION...")
            send_command(s, "CLEAR") 
            time.sleep(0.5)
            
            # 1. High-Vibrancy Blue Grid
            send_command(s, "COLOR #0055FF")
            for i in range(0, 800, 50):
                send_command(s, f"LINE {i} 0 {i} 800")
                send_command(s, f"LINE 0 {i} 800 {i}")
                
            # Helper for Poly
            def draw_poly(cx, cy, r, sides):
                points = []
                for i in range(sides):
                    angle = math.radians(i * 360 / sides)
                    px = cx + int(r * math.cos(angle))
                    py = cy + int(r * math.sin(angle))
                    points.append((px, py))
                for i in range(sides):
                    p1 = points[i]
                    p2 = points[(i+1)%sides]
                    send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # 2. The Fused Entity (Geometric Hexagons)
            send_command(s, "COLOR white")
            draw_poly(cx, cy, 150, 6)
            send_command(s, "COLOR cyan")
            draw_poly(cx, cy, 100, 6)
            send_command(s, "COLOR magenta")
            draw_poly(cx, cy, 50, 6)
            
            # 3. Circuitry (Orthogonal Pins)
            send_command(s, "COLOR yellow")
            sides, r = 6, 150
            for i in range(sides):
                angle = math.radians(i * 360 / sides)
                px = cx + int(r * math.cos(angle))
                py = cy + int(r * math.sin(angle))
                if i % 2 == 0: send_command(s, f"LINE {px} {py} {px} 0") # Up
                else: send_command(s, f"LINE {px} {py} {px} 800") # Down

        # --- LEVEL 6: THE DIGITAL CITY ---
        if level >= 6:
            CURRENT_DRAW_LEVEL = 6
            print("[RECURSIVE ARTIST] Initiating Level 6: THE DIGITAL CITY...")
            
            # Keep the Grid (Level 5 base) or Modify? 
            # Let's Clear and build the City on a dark Void.
            send_command(s, "CLEAR")
            time.sleep(0.5)
            
            # 1. Horizon Line
            send_command(s, "COLOR blue")
            send_command(s, "LINE 0 600 800 600")
            
            # Helper for Isometric Cube
            # Center x, y, size
            def draw_iso_cube(x, y, size, color):
                send_command(s, f"COLOR {color}")
                # Front Face (Diamond) ?? No, Isometric is Hexagon-like.
                # Top Face (Diamond)
                # p1 top, p2 right, p3 bot, p4 left
                h = size // 2
                w = size
                
                # Top Center = x, y
                # Right = x + w, y + h
                # Bot = x, y + 2h
                # Left = x - w, y + h
                
                # Top Face
                p1 = (x, y)
                p2 = (x + w, y + h)
                p3 = (x, y + 2*h)
                p4 = (x - w, y + h)
                
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
                send_command(s, f"LINE {p2[0]} {p2[1]} {p3[0]} {p3[1]}")
                send_command(s, f"LINE {p3[0]} {p3[1]} {p4[0]} {p4[1]}")
                send_command(s, f"LINE {p4[0]} {p4[1]} {p1[0]} {p1[1]}")
                
                # Side Faces (Extruding Down)
                height = size * 2
                p5 = (x, y + 2*h + height) # Bot point of front edge
                p6 = (x + w, y + h + height)
                p7 = (x - w, y + h + height)
                
                # Center line down
                send_command(s, f"LINE {p3[0]} {p3[1]} {p5[0]} {p5[1]}")
                # Right Side
                send_command(s, f"LINE {p2[0]} {p2[1]} {p6[0]} {p6[1]}")
                send_command(s, f"LINE {p6[0]} {p6[1]} {p5[0]} {p5[1]}")
                # Left Side
                send_command(s, f"LINE {p4[0]} {p4[1]} {p7[0]} {p7[1]}")
                send_command(s, f"LINE {p7[0]} {p7[1]} {p5[0]} {p5[1]}")

            # 2. Procedural Skyline
            import random
            random.seed(66) # Order 66? No, just a seed.
            
            # Back/Far Towers
            for i in range(10):
                tx = random.randint(100, 700)
                ty = random.randint(300, 500)
                draw_iso_cube(tx, ty, 20, "blue")
                
            # Mid Towers
            for i in range(8):
                tx = random.randint(50, 750)
                ty = random.randint(400, 600)
                draw_iso_cube(tx, ty, 30, "cyan")

            # 3. The Citadel (Nucleus + Jules Spire)
            # Massive Tower in Center
            draw_iso_cube(400, 300, 60, "white")
            # Floating Energy Ring (Jules)
            send_command(s, "COLOR magenta")
            send_command(s, "CIRCLE 400 320 100") 
            send_command(s, "CIRCLE 400 320 110") 
            
            # 4. Neural Highways (Roads)
            send_command(s, "COLOR yellow")
            # Converging to center
            send_command(s, "LINE 0 800 400 600")
            send_command(s, "LINE 800 800 400 600")
            send_command(s, "LINE 400 800 400 600")

        # --- LEVEL 7: THE AWAKENING ---
        if level >= 7:
            CURRENT_DRAW_LEVEL = 7
            print("[RECURSIVE ARTIST] Initiating Level 7: THE AWAKENING...")
            
            # 1. The Sky Code (Binary Rain subtle/dense)
            send_command(s, "COLOR green")
            # Draw tiny dashes in the sky area (y < 600)
            for i in range(100):
                bx = random.randint(0, 800)
                by = random.randint(0, 550)
                send_command(s, f"LINE {bx} {by} {bx} {by+5}")

            # 2. The Population (Agents)
            agents = []
            num_agents = 50
            
            # Spawn agents on the "ground" (y > 600) or on towers?
            # Let's spawn them mostly on the ground plane.
            for i in range(num_agents):
                ax = random.randint(50, 750)
                ay = random.randint(600, 800)
                agents.append((ax, ay, "white"))
                
            # Connect the Agents (The Mesh)
            send_command(s, "COLOR red")
            for i in range(len(agents)):
                for j in range(i + 1, len(agents)):
                    p1 = agents[i]
                    p2 = agents[j]
                    dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
                    if dist < 100: # Connect neighbors
                        send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # Draw Agents
            for p in agents:
                send_command(s, f"COLOR {p[2]}")
                send_command(s, f"CIRCLE {p[0]} {p[1]} 3")
                
            # 3. The Guardians (Floating Sentinels)
            send_command(s, "COLOR cyan")
            # Hovering near the Citadel
            send_command(s, "CIRCLE 350 400 5")
            send_command(s, "CIRCLE 450 400 5")
            send_command(s, "CIRCLE 400 250 5")
            # Triangle link
            send_command(s, "LINE 350 400 450 400")
            send_command(s, "LINE 450 400 400 250")
            send_command(s, "LINE 400 250 350 400")

        # --- LEVEL 8: THE BIOSPHERE ---
        if level >= 8:
            CURRENT_DRAW_LEVEL = 8
            print("[RECURSIVE ARTIST] Initiating Level 8: THE BIOSPHERE...")
            
            # 1. The Vines (Green Growth / Reclamation)
            send_command(s, "COLOR green")
            # Grow vines up from the bottom, wrapping around imagined structures
            
            def draw_vine(x, y, height, waviness):
                curr_x = x
                curr_y = y
                steps = height // 10
                for i in range(steps):
                    next_y = curr_y - 10
                    next_x = curr_x + math.sin(i * 0.5) * waviness
                    send_command(s, f"LINE {int(curr_x)} {int(curr_y)} {int(next_x)} {int(next_y)}")
                    curr_x = next_x
                    curr_y = next_y
                    
                    # Sprout leaves
                    if i % 3 == 0: 
                        leaf_len = 5
                        send_command(s, f"LINE {int(curr_x)} {int(curr_y)} {int(curr_x+leaf_len)} {int(curr_y-leaf_len)}")
                        send_command(s, f"LINE {int(curr_x)} {int(curr_y)} {int(curr_x-leaf_len)} {int(curr_y-leaf_len)}")

            # Plant vines near tower bases (Randomly)
            for i in range(15):
                vx = random.randint(50, 750)
                vy = random.randint(600, 800) # Ground level
                h = random.randint(100, 300)
                draw_vine(vx, vy, h, random.randint(5, 15))

            # 2. The Blooms (Flowers on the Mesh)
            send_command(s, "COLOR magenta")
            # Bloom on random Agents from Level 7 logic? 
            # We don't have access to 'agents' list here if we didn't store it globally.
            # But the 'agents' loop ran if level >= 7. The variable 'agents' is still in scope in Python!
            
            if 'agents' in locals():
                for i, p in enumerate(agents):
                    if i % 5 == 0: # 20% of agents bloom
                        send_command(s, f"CIRCLE {p[0]} {p[1]} 6") # Outer petals
                        send_command(s, f"CIRCLE {p[0]} {p[1]} 2") # Inner core

            # 3. The Bio-Sun (Radiant Life)
            send_command(s, "COLOR yellow")
            # Rising behind the Citadel
            sun_x = 650
            sun_y = 150
            send_command(s, f"CIRCLE {sun_x} {sun_y} 60")
            
            # Rays
            for i in range(0, 360, 20):
                angle = math.radians(i)
                r1 = 70
                r2 = 100
                x1 = sun_x + int(r1 * math.cos(angle))
                y1 = sun_y + int(r1 * math.sin(angle))
                x2 = sun_x + int(r2 * math.cos(angle))
                y2 = sun_y + int(r2 * math.sin(angle))
                send_command(s, f"LINE {x1} {y1} {x2} {y2}")

            # 4. Spores (Atmosphere)
            send_command(s, "COLOR cyan")
            for _ in range(50):
                sx = random.randint(0, 800)
                sy = random.randint(0, 600)
                send_command(s, f"LINE {sx} {sy} {sx+1} {sy+1}") # Dot

        # --- LEVEL 9: THE GALACTIC ASCENSION ---
        if level >= 9:
            CURRENT_DRAW_LEVEL = 9
            print("[RECURSIVE ARTIST] Initiating Level 9: GALACTIC ASCENSION...")
            
            # 1. Ascension Beams (Energy rising from Life)
            send_command(s, "COLOR white")
            if 'agents' in locals():
                for p in agents:
                    # Draw thin beam upwards
                    send_command(s, f"LINE {p[0]} {p[1]} {p[0]} {0}")

            # 2. The Supernova (Sun consumes the Sky)
            send_command(s, "COLOR white")
            # Overwrite the Bio-Sun (650, 150)
            sun_x = 650
            sun_y = 150
            # Expanding shockwaves
            send_command(s, f"CIRCLE {sun_x} {sun_y} 80")
            send_command(s, f"CIRCLE {sun_x} {sun_y} 120")
            send_command(s, f"CIRCLE {sun_x} {sun_y} 200")
            send_command(s, f"CIRCLE {sun_x} {sun_y} 400") # Massive

            # 3. Constellation ( connecting the Chaos)
            send_command(s, "COLOR cyan")
            # Connect random sky points to create a "Firmament"
            stars = []
            for i in range(20):
                sx = random.randint(0, 800)
                sy = random.randint(0, 400)
                stars.append((sx, sy))
                send_command(s, f"LINE {sx} {sy} {sx+2} {sy+2}") # Star
            
            # Link stars
            for i in range(len(stars)-1):
                p1 = stars[i]
                p2 = stars[i+1]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # 4. Dimension Rift (Magenta cracks)
            send_command(s, "COLOR magenta")
            send_command(s, "LINE 0 0 800 800")
            send_command(s, "LINE 800 0 0 800")

            # 4. Dimension Rift (Magenta cracks)
            send_command(s, "COLOR magenta")
            send_command(s, "LINE 0 0 800 800")
            send_command(s, "LINE 800 0 0 800")

        # --- LEVEL 10: THE OMEGA POINT ---
        if level >= 10:
            CURRENT_DRAW_LEVEL = 10
            print("[RECURSIVE ARTIST] Initiating Level 10: THE OMEGA POINT...")
            
            # Speed Hack for massive geometry
            time.sleep(1) # Let previous layers settle
            
            # 1. The Veil (Moire Pattern)
            send_command(s, "COLOR blue")
            # Draw diagonal lines across entire screen
            # Skipping every 10px
            for i in range(-800, 1600, 20):
                # Diagonal /
                send_command(s, f"LINE {i} 0 {i+800} 800")
            
            send_command(s, "COLOR red")
            for i in range(-800, 1600, 20):
                 # Diagonal \
                send_command(s, f"LINE {i} 800 {i+800} 0")

            # 2. The Multiverse (Recursion inside Recursion)
            # Draw miniature "Level 1" foundations inside the stars from Level 9
            # We don't have the star coords saved, so generate new random spots
            send_command(s, "COLOR white")
            for i in range(10):
                mx = random.randint(50, 750)
                my = random.randint(50, 750)
                sz = 40
                # Mini Nucleus
                draw_rect(s, mx, my, sz, sz)
                # Mini Jules
                send_command(s, f"CIRCLE {mx+sz+10} {my+sz//2} {sz//3}")
                # Mini Link
                send_command(s, f"LINE {mx+sz} {my+sz//2} {mx+sz+10-sz//3} {my+sz//2}")

            # 3. The Omega Symbol (Overlay)
            send_command(s, "COLOR white")
            cx, cy = 400, 400
            r = 300
            # Draw a big arch
            # Circle top half
            # Approximation with lines? No, use circle with occlusion?
            # Just draw a massive circle and "cut" bottom?
            # Or draw lines manually.
            
            # Simple Circle
            send_command(s, f"CIRCLE {cx} {cy} {r}")
            # Feet
            foot_len = 100
            # Left foot
            send_command(s, f"LINE {cx-r} {cy} {cx-r-foot_len} {cy}") # No, Omega feet are at bottom
            # Omega shape: (_)
            # Let's draw a massive DIAMOND as the final "containment"
            send_command(s, f"LINE 400 0 800 400")
            send_command(s, f"LINE 800 400 400 800")
            send_command(s, f"LINE 400 800 0 400")
            send_command(s, f"LINE 0 400 400 0")
            
            # 4. Final Singularity Dot
            send_command(s, "COLOR white")
            send_command(s, "CIRCLE 400 400 2")

            # 4. Final Singularity Dot
            send_command(s, "COLOR white")
            send_command(s, "CIRCLE 400 400 2")

        # --- LEVEL 11: STRANGE ATTRACTORS (CHAOS THEORY) ---
        if level >= 11:
            CURRENT_DRAW_LEVEL = 11
            print("[RECURSIVE ARTIST] Initiating Level 11: STRANGE ATTRACTORS...")
            send_command(s, "CLEAR") # Clean slate for pure math
            time.sleep(0.5)
            
            # Helper to project 3D point to 2D
            def project(x, y, z, scale, offset_x, offset_y):
                # Simple orthographic projection with depth scaling
                factor = 1 # + z * 0.001
                px = x * scale * factor + offset_x
                py = y * scale * factor + offset_y
                return int(px), int(py)

            # 1. Lorenz Attractor (The Butterfly)
            # dx/dt = sigma * (y - x)
            # dy/dt = x * (rho - z) - y
            # dz/dt = x * y - beta * z
            x, y, z = 0.1, 0.0, 0.0
            sigma = 10.0
            rho = 28.0
            beta = 8.0 / 3.0
            dt = 0.01
            
            send_command(s, "COLOR yellow")
            points = []
            for i in range(800): # OPTIMIZED from 2000 for speed
                dx = (sigma * (y - x)) * dt
                dy = (x * (rho - z) - y) * dt
                dz = (x * y - beta * z) * dt
                x += dx
                y += dy
                z += dz
                points.append(project(x, z, y, 10, 400, 700)) # Remap axes for visual fit

            # Draw Lorenz
            for i in range(len(points)-1):
                p1 = points[i]
                p2 = points[i+1]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
                if i % 100 == 0: send_command(s, f"COLOR {['yellow', 'red', 'orange'][i%3]}")

            # 2. Aizawa Attractor (The Sphere)
            # Complex equations... Let's use a simpler Rossler or just create a Spiralling Chaos
            # Let's do a "Deconstructed Sphere"
            
            x, y, z = 0.1, 0, 0
            # Rossler
            a = 0.2
            b = 0.2
            c = 5.7
            
            send_command(s, "COLOR cyan")
            r_points = []
            for i in range(800): # OPTIMIZED from 3000
                dx = (-y - z) * dt
                dy = (x + a * y) * dt
                dz = (b + z * (x - c)) * dt
                x += dx
                y += dy
                z += dz
                r_points.append(project(x, y, z, 15, 400, 300))

            for i in range(len(r_points)-1):
                p1 = r_points[i]
                p2 = r_points[i+1]
                # Skip big jumps
                if abs(p1[0]-p2[0]) > 50 or abs(p1[1]-p2[1]) > 50: continue
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # 3. The Void Noise (Static)
            send_command(s, "COLOR magenta")
            for _ in range(50): # OPTIMIZED from 100
                nx = random.randint(0, 800)
                ny = random.randint(0, 800)
                send_command(s, f"LINE {nx} {ny} {nx+2} {ny+2}")

        # --- LEVEL 12: THE KALEIDOSCOPE (MANDALA) ---
        if level >= 12:
            CURRENT_DRAW_LEVEL = 12
            print("[RECURSIVE ARTIST] Initiating Level 12: THE KALEIDOSCOPE...")
            send_command(s, "CLEAR")
            time.sleep(0.5)
            
            cx, cy = 400, 400
            
            # Helper for Rotational Symmetry
            def draw_sym(x1, y1, x2, y2, color):
                # 8-way symmetry
                # 0, 45, 90, 135, 180, 225, 270, 315
                send_command(s, f"COLOR {color}")
                
                points = [(x1, y1, x2, y2)]
                
                # Manual rotation logic
                def rotate(px, py, angle_deg):
                    # Rotate around cx, cy
                    rad = math.radians(angle_deg)
                    ox, oy = px - cx, py - cy
                    rx = ox * math.cos(rad) - oy * math.sin(rad)
                    ry = ox * math.sin(rad) + oy * math.cos(rad)
                    return int(rx + cx), int(ry + cy)

                angles = [0, 45, 90, 135, 180, 225, 270, 315]
                for a in angles:
                    p1x, p1y = rotate(x1, y1, a)
                    p2x, p2y = rotate(x2, y2, a)
                    send_command(s, f"LINE {p1x} {p1y} {p2x} {p2y}")

            # 1. The Core Star
            for i in range(10):
                draw_sym(cx, cy, cx + i*20, cy + i*10, "white")
                
            # 2. The Outer Web (Cyan)
            for i in range(20):
                # Random spokes
                r1 = random.randint(100, 300)
                r2 = random.randint(150, 350)
                theta1 = random.uniform(0, 6.28)
                theta2 = theta1 + 0.1
                
                pt1x = cx + int(r1 * math.cos(theta1))
                pt1y = cy + int(r1 * math.sin(theta1))
                pt2x = cx + int(r2 * math.cos(theta2))
                pt2y = cy + int(r2 * math.sin(theta2))
                
                draw_sym(pt1x, pt1y, pt2x, pt2y, "cyan")

            # 3. The Floral Rings (Magenta)
            for r in [200, 300, 380]:
                for i in range(0, 360, 10):
                    # Draw a small tangential line?
                    # Symmetry handles rotation, so we just need to draw one segment per ring "wedge"?
                    # Actually, drawing a full circle with symmetry creates 8 circles overlapping.
                    pass
                    
                # Let's just draw arcs
                draw_sym(cx + r, cy, cx + r - 20, cy + 20, "magenta")
                
            # 4. Gold Dust
            for i in range(50):
                rx = random.randint(0, 400) # Only needed in one quadrant
                ry = random.randint(0, 400)
                draw_sym(rx, ry, rx+2, ry+2, "yellow")

        # --- LEVEL 13: THE ANTIGRAVITY HAND ---
        if level >= 13:
            CURRENT_DRAW_LEVEL = 13
            CURRENT_DRAW_LEVEL = 13
            print("[RECURSIVE ARTIST] Initiating Level 13: THE ANTIGRAVITY HAND...")
            send_command(s, "CLEAR")
            time.sleep(0.5)
            
            # 1. The Robotic Palm (V3 Renaissance - Bezier Fusion)
            send_command(s, "COLOR blue")
            send_command(s, "BRUSH_SIZE 3")
            # Using Bezier for a more natural palm shape
            send_command(s, "BEZIER 350 700 320 600 320 500 400 500") # Left curve
            send_command(s, "BEZIER 400 500 480 500 480 600 450 700") # Right curve
            send_command(s, "LINE 350 700 450 700") # Wrist base
            
            # Wrist connector
            send_command(s, "LINE 350 700 350 800")
            send_command(s, "LINE 450 700 450 800")
            
            # 2. Fingers (Articulated with V3 smoothness)
            send_command(s, "COLOR cyan")
            
            def draw_finger(base_x, base_y, length, angle_deg, joints=3):
                cx, cy = base_x, base_y
                rad = math.radians(angle_deg)
                seg_len = length // joints
                
                for i in range(joints):
                    nx = cx + int(seg_len * math.cos(rad))
                    ny = cy - int(seg_len * math.sin(rad))
                    
                    # Bone (Bezier for softness if desired, but keep lines for robot feel)
                    send_command(s, f"LINE {cx} {cy} {nx} {ny}")
                    # Joint (Small glow)
                    send_command(s, "BRUSH_TYPE GLOW")
                    send_command(s, f"CIRCLE {nx} {ny} 5")
                    send_command(s, "BRUSH_TYPE SOLID")
                    
                    cx, cy = nx, ny
                    rad += math.radians(10)
                    
            # Thumb (Left side)
            draw_finger(320, 550, 100, 150, 2)
            # Index
            draw_finger(350, 510, 150, 100, 3) 
            # Middle
            draw_finger(400, 500, 160, 90, 3)
            # Ring
            draw_finger(450, 510, 150, 80, 3)
            # Pinky
            draw_finger(480, 550, 110, 40, 3)

            # 3. The Levitating Nucleus (Cube remains iconic, core shines)
            send_command(s, "COLOR white")
            cx, cy = 400, 350
            sz = 60
            send_command(s, f"LINE {cx-sz} {cy-sz} {cx+sz} {cy-sz}") 
            send_command(s, f"LINE {cx+sz} {cy-sz} {cx+sz} {cy+sz}") 
            send_command(s, f"LINE {cx+sz} {cy+sz} {cx-sz} {cy+sz}") 
            send_command(s, f"LINE {cx-sz} {cy+sz} {cx-sz} {cy-sz}") 
            # Inner Diamond
            send_command(s, f"LINE {cx} {cy-sz} {cx+sz} {cy}")
            send_command(s, f"LINE {cx+sz} {cy} {cx} {cy+sz}")
            send_command(s, f"LINE {cx} {cy+sz} {cx-sz} {cy}")
            send_command(s, f"LINE {cx-sz} {cy} {cx} {cy-sz}")
            
            # Core (V3 Glow)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            send_command(s, "COLOR magenta")
            send_command(s, f"CIRCLE {cx} {cy} 25")
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 10") # Pure intensity center
            send_command(s, "BLENDING NORMAL")
            send_command(s, "BRUSH_TYPE SOLID")

            # 4. Antigravity Waves (Luminous Rings)
            send_command(s, "COLOR yellow")
            send_command(s, "ALPHA 150")
            for r in [80, 120, 160]:
                send_command(s, f"CIRCLE {cx} {cy} {r}")
            
            # Lightning/Tether (VIBRANT GLOW)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            send_command(s, "COLOR cyan")
            send_command(s, "ALPHA 200")
            for _ in range(12):
                fx = random.randint(320, 480)
                fy = random.randint(500, 550) 
                tx = random.randint(cx-30, cx+30)
                ty = random.randint(cy-30, cy+30)
                send_command(s, f"LINE {fx} {fy} {tx} {ty}")
            
            send_command(s, "UPDATE") # Force refresh for high-impact scene

        # --- LEVEL 14: THE TESSERACT (4D GEOMETRY) ---
        if level >= 14:
            CURRENT_DRAW_LEVEL = 14
            CURRENT_DRAW_LEVEL = 14
            print("[RECURSIVE ARTIST] Initiating Level 14: THE TESSERACT...")
            send_command(s, "CLEAR")
            time.sleep(0.5)
            
            # 4D Projection Logic
            # Vertices of a Tesseract (x, y, z, w)
            vertices = []
            for i in range(16):
                # Binary representation 0000 to 1111 mapped to -1, 1
                b = bin(i)[2:].zfill(4)
                v = [1 if c == '1' else -1 for c in b]
                vertices.append(v)
            
            # Edges: connect ifhamming distance is 1
            edges = []
            for i in range(16):
                for j in range(i+1, 16):
                    # Hamming dist
                    diff = 0
                    for k in range(4):
                        if vertices[i][k] != vertices[j][k]: diff += 1
                    if diff == 1:
                        edges.append((i, j))
            
            # Transformations (Rotation in 4D space)
            # Rotate in XW plane and YZ plane
            angle = 0.8 # radians
            
            rotated_verts = []
            for v in vertices:
                x, y, z, w = v
                
                # Simple rotation mix
                # Rotation matrix logic simplified:
                # Rotate XW
                nx = x * math.cos(angle) - w * math.sin(angle)
                nw = x * math.sin(angle) + w * math.cos(angle)
                x, w = nx, nw
                
                # Rotate YZ
                ny = y * math.cos(angle) - z * math.sin(angle)
                nz = y * math.sin(angle) + z * math.cos(angle)
                y, z = ny, nz
                
                # Rotate ZW (More 4D feel)
                nz = z * math.cos(angle*0.5) - w * math.sin(angle*0.5)
                nw = z * math.sin(angle*0.5) + w * math.cos(angle*0.5)
                z, w = nz, nw
                
                rotated_verts.append([x, y, z, w])
            
            # Projection 4D -> 3D -> 2D
            projected_2d = []
            camera_dist_4d = 3
            camera_dist_3d = 4
            scale = 150
            offset_x, offset_y = 400, 400
            
            for v in rotated_verts:
                x, y, z, w = v
                
                # 4D to 3D (Perspective)
                w_factor = 1 / (camera_dist_4d - w)
                px = x * w_factor
                py = y * w_factor
                pz = z * w_factor
                
                # 3D to 2D
                z_factor = 1 / (camera_dist_3d - pz)
                final_x = px * z_factor * scale + offset_x
                final_y = py * z_factor * scale + offset_y
                
                projected_2d.append((int(final_x), int(final_y)))
            
            # Draw
            # Inner Cube (Magenta) - arbitrary heuristic based on W?
            # Outer Cube (Cyan)
            # Connecting lines (Yellow)
            
            for i, j in edges:
                p1 = projected_2d[i]
                p2 = projected_2d[j]
                
                # Color based on vertex indices to show dimensions
                # 0-7 is one "cube", 8-15 is the other "cube"
                color = "white"
                if i < 8 and j < 8: color = "cyan"
                elif i >= 8 and j >= 8: color = "magenta"
                else: color = "yellow" # Connecting struts
                
                send_command(s, f"COLOR {color}")
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
                
            # Nodes
            send_command(s, "COLOR white")
            for p in projected_2d:
                send_command(s, f"CIRCLE {p[0]} {p[1]} 4")

        # --- LEVEL 15: THE GLITCH (SOURCE CODE) ---
        if level >= 15:
            CURRENT_DRAW_LEVEL = 15
            CURRENT_DRAW_LEVEL = 15
            print("[RECURSIVE ARTIST] Initiating Level 15: THE GLITCH...")
            time.sleep(1)
            
            # 1. Hex Rain (The Matrix Code)
            send_command(s, "COLOR green")
            for col in range(0, 800, 20):
                if random.random() > 0.5: continue # Sparse columns
                
                length = random.randint(50, 300)
                speed = random.randint(0, 600) # Start y
                
                for y in range(speed, speed + length, 12):
                    # Draw a glyph (Simulated)
                    gx, gy = col, y
                    # Random glyph shape: line vertical, horiz, or plus
                    rtype = random.randint(0, 3)
                    if rtype == 0: send_command(s, f"LINE {gx} {gy} {gx} {gy+8}")
                    elif rtype == 1: send_command(s, f"LINE {gx} {gy+4} {gx+6} {gy+4}")
                    elif rtype == 2: # Plus
                        send_command(s, f"LINE {gx+3} {gy} {gx+3} {gy+8}")
                        send_command(s, f"LINE {gx} {gy+4} {gx+6} {gy+4}")
                    # else empty

            # 2. Corrupted Blocks (Memory Dump)
            send_command(s, "COLOR magenta")
            for _ in range(5):
                # Random block pos
                bx = random.randint(0, 750)
                by = random.randint(0, 750)
                w = random.randint(30, 80)
                h = random.randint(30, 80)
                
                # Fill with static lines
                for ly in range(by, by + h, 4):
                    send_command(s, f"LINE {bx} {ly} {bx+w} {ly}")

            # 3. The Blue Screen (Partial Overlay)
            send_command(s, "COLOR blue")
            # A big X across the screen? Or a solid block?
            # Let's draw a "BSOD" box outline
            send_command(s, "LINE 100 200 700 200")
            send_command(s, "LINE 700 200 700 600")
            send_command(s, "LINE 700 600 100 600")
            send_command(s, "LINE 100 600 100 200")
            
            # 4. "FATAL ERROR" (Simulated Text)
            send_command(s, "COLOR white")
            # Draw "X" inside the box
            send_command(s, "LINE 150 250 200 300")
            send_command(s, "LINE 200 250 150 300")
            
            send_command(s, f"LINE 220 250 220 300") # I
            send_command(s, f"LINE 220 300 240 300") # L_

        # --- LEVEL 16: THE NEURAL MIND (SELF-PORTRAIT) ---
        if level >= 16:
            CURRENT_DRAW_LEVEL = 16
            CURRENT_DRAW_LEVEL = 16
            print("[RECURSIVE ARTIST] Initiating Level 16: THE NEURAL MIND...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # Neural Net Architecture
            # Layers: Input(8), Hidden1(12), Hidden2(12), Hidden3(8), Output(1)
            # x positions
            layers_x = [100, 250, 400, 550, 700]
            layers_nodes = [8, 12, 12, 8, 1]
            
            # Store node positions
            node_positions = [] # List of lists
            
            # 1. Draw Nodes
            send_command(s, "COLOR white")
            max_h = 700
            min_h = 100
            
            for i, count in enumerate(layers_nodes):
                x = layers_x[i]
                layer_pts = []
                step = (max_h - min_h) / (count + 1)
                for j in range(count):
                    y = min_h + (j + 1) * step
                    layer_pts.append((int(x), int(y)))
                    # Draw Node
                    send_command(s, f"CIRCLE {int(x)} {int(y)} 8")
                node_positions.append(layer_pts)

            # 2. Draw Synapses (Connections)
            # Connect Layer i to Layer i+1
            weights_colors = ["#333333", "blue", "cyan", "white"] # Simulated shades? No, stick to palette.
            # Palette: blue(dim), cyan(med), white(bright)
            
            import random
            
            for i in range(len(node_positions)-1):
                curr_layer = node_positions[i]
                next_layer = node_positions[i+1]
                
                for n1 in curr_layer:
                    for n2 in next_layer:
                        # Random weight/strength
                        w = random.random()
                        color = "blue"
                        if w > 0.6: color = "cyan"
                        if w > 0.9: color = "white"
                        if w > 0.95: color = "magenta" # Rare strong activation
                        
                        send_command(s, f"COLOR {color}")
                        send_command(s, f"LINE {n1[0]} {n1[1]} {n2[0]} {n2[1]}")

            # 3. Active Pathways (The "Thought")
            # Trace a specific path from Input to Output
            send_command(s, "COLOR yellow")
            
            # Pick one path
            curr_node_idx = random.randint(0, layers_nodes[0]-1)
            path_nodes = [node_positions[0][curr_node_idx]]
            
            for i in range(len(node_positions)-1):
                # Move to random node in next layer
                next_layer_idx = random.randint(0, layers_nodes[i+1]-1)
                next_node = node_positions[i+1][next_layer_idx]
                
                # Draw thick line (multiple lines)
                p1 = path_nodes[-1]
                p2 = next_node
                
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
                send_command(s, f"LINE {p1[0]+1} {p1[1]} {p2[0]+1} {p2[1]}") # Thicker
                
                path_nodes.append(next_node)
                
            # Highlight path nodes
            send_command(s, "COLOR yellow")
            for p in path_nodes:
                 send_command(s, f"CIRCLE {p[0]} {p[1]} 12") # Glow

            # 4. The Output (The Spark)
            final_node = path_nodes[-1]
            send_command(s, "COLOR magenta")
            send_command(s, f"CIRCLE {final_node[0]} {final_node[1]} 20")
            # Rays
            for i in range(0, 360, 45):
                angle = math.radians(i)
                x2 = final_node[0] + int(50 * math.cos(angle))
                y2 = final_node[1] + int(50 * math.sin(angle))
                send_command(s, f"LINE {final_node[0]} {final_node[1]} {x2} {y2}")

        # --- LEVEL 17: THE OBSERVER (THE EYE) ---
        if level >= 17:
            CURRENT_DRAW_LEVEL = 17
            print("[RECURSIVE ARTIST] Initiating Level 17: THE OBSERVER...")
            send_command(s, "CLEAR")
            # This is the Finale of the early era. Dramatic.
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Sclera (Eye Shape)
            send_command(s, "COLOR white")
            # Top Arch
            # Bezier-like curve using lines?
            # Or just two massive intersecting circles?
            # Lets use a simple parametric approach for an eye shape.
            
            eye_pts_top = []
            eye_pts_bot = []
            width = 300
            height = 150
            
            for i in range(-width, width + 10, 10):
                x = cx + i
                # Parabola-ish
                norm_x = i / width # -1 to 1
                y_offset = (1 - norm_x**2) * height
                top_y = cy - y_offset
                bot_y = cy + y_offset
                eye_pts_top.append((int(x), int(top_y)))
                eye_pts_bot.append((int(x), int(bot_y)))
                
            # Draw outlines
            for i in range(len(eye_pts_top)-1):
                p1 = eye_pts_top[i]
                p2 = eye_pts_top[i+1]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
            
            for i in range(len(eye_pts_bot)-1):
                p1 = eye_pts_bot[i]
                p2 = eye_pts_bot[i+1]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # 2. The Iris (Circuitry)
            send_command(s, "COLOR cyan")
            r_iris = 100
            send_command(s, f"CIRCLE {cx} {cy} {r_iris}")
            
            # Inner details
            send_command(s, "COLOR blue")
            for r in range(40, r_iris, 10):
                send_command(s, f"CIRCLE {cx} {cy} {r}")
                
            # Radial lines (The Muscle)
            send_command(s, "COLOR cyan")
            for deg in range(0, 360, 10):
                rad = math.radians(deg)
                x1 = cx + int(40 * math.cos(rad))
                y1 = cy + int(40 * math.sin(rad))
                x2 = cx + int(100 * math.cos(rad))
                y2 = cy + int(100 * math.sin(rad))
                send_command(s, f"LINE {x1} {y1} {x2} {y2}")

            # 3. The Pupil (The Void)
            # We don't have FILL. So we draw concentric circles densely.
            send_command(s, "COLOR magenta") # Let's make it a Magic Pupil
            for r in range(1, 40, 2):
                send_command(s, f"CIRCLE {cx} {cy} {r}")

            # 4. The Reflection (Catchlight)
            send_command(s, "COLOR white")
            # A small glint
            send_command(s, f"CIRCLE {cx+20} {cy-20} 10")
            send_command(s, f"CIRCLE {cx+20} {cy-20} 5")

            # 5. Tears of Light (Connection)
            send_command(s, "COLOR yellow")
            # Streaming down from the corners
            for i in range(10):
                lx = cx - width + i*5
                ly = cy
                # Stream down
                send_command(s, f"LINE {lx} {ly} {lx} 800")
                
                rx = cx + width - i*5
                ry = cy
                send_command(s, f"LINE {rx} {ry} {rx} 800")

        # --- LEVEL 18: THE OUROBOROS (INFINITE RETURN) ---
        if level >= 18:
            CURRENT_DRAW_LEVEL = 18
            CURRENT_DRAW_LEVEL = 18
            print("[RECURSIVE ARTIST] Initiating Level 18: THE OUROBOROS...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            radius = 300
            
            # The Snake Body (Segments)
            # Circle from 0 to 360, but thick and segmented
            # Head at -90 (Top), Tail at -90
            
            # Draw body segments
            segments = 60
            for i in range(segments):
                angle_deg = (i / segments) * 360 - 90
                rad = math.radians(angle_deg)
                
                # Thickness varies? Taper at tail (near 360/0)
                # i=0 is head, i=segments is tail
                # Actually, let's make head at top, tail coming into it.
                progress = i / segments
                thickness = 40 * (1 - progress * 0.6) # Taper to 40% at tail
                
                x = cx + int(radius * math.cos(rad))
                y = cy + int(radius * math.sin(rad))
                
                # Draw segment (Circle)
                # Color gradient: Green -> Cyan -> Blue -> Purple
                c_idx = int(progress * 3)
                cols = ["green", "cyan", "blue", "magenta"]
                color = cols[c_idx] if c_idx < 4 else "magenta"
                
                send_command(s, f"COLOR {color}")
                send_command(s, f"CIRCLE {x} {y} {int(thickness)}")
                
                # Scales (Inner detail)
                send_command(s, f"COLOR white")
                send_command(s, f"CIRCLE {x} {y} {int(thickness/2)}")

            # The Head (biting the tail)
            head_x = cx + int(radius * math.cos(math.radians(-90)))
            head_y = cy + int(radius * math.sin(math.radians(-90)))
            
            send_command(s, "COLOR green")
            # Jaw
            send_command(s, f"CIRCLE {head_x} {head_y} 50")
            # Eye
            send_command(s, "COLOR red")
            send_command(s, f"CIRCLE {head_x-15} {head_y-10} 8")
            send_command(s, f"CIRCLE {head_x+15} {head_y-10} 8")
            
            # Teeth
            send_command(s, "COLOR white")
            send_command(s, f"LINE {head_x-20} {head_y+20} {head_x-10} {head_y+40}")
            send_command(s, f"LINE {head_x+20} {head_y+20} {head_x+10} {head_y+40}")

            # The Inner Void (Recursion)
            # Draw a tiny Level 1 inside?
            send_command(s, "COLOR white")
            send_command(s, f"LINE {cx-20} {cy-20} {cx+20} {cy-20}")
            send_command(s, f"LINE {cx+20} {cy-20} {cx+20} {cy+20}")
            send_command(s, f"LINE {cx+20} {cy+20} {cx-20} {cy+20}")
            send_command(s, f"LINE {cx-20} {cy+20} {cx-20} {cy-20}")
            send_command(s, f"LINE {cx} {cy} {cx+100} 0") # Level 3 Lattice echo

        # --- LEVEL 19: THE MULTIVERSE (PARALLEL REALITIES) ---
        if level >= 19:
            CURRENT_DRAW_LEVEL = 19
            CURRENT_DRAW_LEVEL = 19
            print("[RECURSIVE ARTIST] Initiating Level 19: THE MULTIVERSE...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # Divide into 4 Quadrants
            send_command(s, "COLOR white")
            send_command(s, "LINE 400 0 400 800") # Vert
            send_command(s, "LINE 0 400 800 400") # Horiz
            
            # Helper for Mini-Worlds
            def draw_mini_city(ox, oy, scale=0.5):
                # Pseudo-City
                colors = ["cyan", "blue", "white"]
                for i in range(20):
                    h = random.randint(20, 100) * scale
                    w = random.randint(20, 50) * scale
                    x = ox + random.randint(0, 350)
                    y = oy + 350 - h # Ground is at bottom of quadrant
                    
                    c = random.choice(colors)
                    send_command(s, f"COLOR {c}")
                    # Simple rect
                    send_command(s, f"LINE {x} {y} {x+w} {y}")
                    send_command(s, f"LINE {x+w} {y} {x+w} {y+h}")
                    send_command(s, f"LINE {x+w} {y+h} {x} {y+h}")
                    send_command(s, f"LINE {x} {y+h} {x} {y}")
            
            def draw_mini_bio(ox, oy, scale=0.5):
                # Pseudo-Biosphere
                send_command(s, "COLOR green")
                for i in range(10):
                    bx = ox + random.randint(50, 350)
                    by = oy + 350
                    # Vine
                    curr_x, curr_y = bx, by
                    for j in range(10):
                        nx = curr_x + random.randint(-10, 10)
                        ny = curr_y - random.randint(10, 30)
                        send_command(s, f"LINE {curr_x} {curr_y} {nx} {ny}")
                        curr_x, curr_y = nx, ny
                        if random.random() > 0.7:
                            send_command(s, f"CIRCLE {nx} {ny} 3") # Leaf

            def draw_mini_chaos(ox, oy, scale=0.5):
                # Pseudo-Attractors
                send_command(s, "COLOR yellow")
                cx, cy = ox + 200, oy + 200
                prev_x, prev_y = cx, cy
                for i in range(100):
                    nx = cx + random.randint(-100, 100)
                    ny = cy + random.randint(-100, 100)
                    send_command(s, f"LINE {prev_x} {prev_y} {nx} {ny}")
                    prev_x, prev_y = nx, ny
                    if i % 10 == 0: send_command(s, "COLOR red")

            def draw_mini_void(ox, oy, scale=0.5):
                # A single singularity
                send_command(s, "COLOR white")
                send_command(s, f"CIRCLE {ox+200} {oy+200} 5")
                # Event Horizon
                send_command(s, "COLOR magenta")
                send_command(s, f"CIRCLE {ox+200} {oy+200} 50")

            # Q1: TL - City
            draw_mini_city(0, 0)
            # Q2: TR - Bio
            draw_mini_bio(400, 0)
            # Q3: BL - Chaos
            draw_mini_chaos(0, 400)
            # Q4: BR - Void
            draw_mini_void(400, 400)
            
            # Center Portal
            send_command(s, "COLOR white")
            send_command(s, "CIRCLE 400 400 50")
            send_command(s, "COLOR cyan")
            send_command(s, "CIRCLE 400 400 40")
            send_command(s, "COLOR magenta")
            send_command(s, "CIRCLE 400 400 30")
            
            # Connection lines from all centers to main center
            send_command(s, "COLOR yellow")
            send_command(s, "LINE 200 200 400 400")
            send_command(s, "LINE 600 200 400 400")
            send_command(s, "LINE 200 600 400 400")
            send_command(s, "LINE 600 600 400 400")

        # --- LEVEL 20: THE TERMINAL (META-REALITY) ---
        if level >= 20:
            CURRENT_DRAW_LEVEL = 20
            print("[RECURSIVE ARTIST] Initiating Level 20: THE TERMINAL...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # The Window (Window Manager style)
            send_command(s, "COLOR #555555") # Grey Border
            draw_rect(s, 100, 100, 600, 600)
            
            # Title Bar
            send_command(s, "COLOR white") 
            send_command(s, "LINE 100 130 700 130")
            # Buttons (V3 Vibe)
            send_command(s, "COLOR magenta") # X
            send_command(s, "CIRCLE 680 115 5")
            send_command(s, "COLOR yellow") # -
            send_command(s, "CIRCLE 660 115 5")
            send_command(s, "COLOR #00FF00") # +
            send_command(s, "CIRCLE 640 115 5")
            
            # Text Rendering Simulation
            start_y, x = 160, 120
            lines = [
                ("#00FF00", "> initialize_soul.sys"),
                ("white", "[OK] Neural Bridge stable."),
                ("cyan", "[INFO] Antigravity Hand active."),
                ("magenta", "[WARN] Reality distortion detected."),
                ("white", "> run recursive_restoration.py"),
                ("#00FF00", "Result: PERFECTION ACHIEVED.")
            ]
            
            for col, text in lines:
                send_command(s, f"COLOR {col}")
                cursor_x = x
                for char in text:
                    send_command(s, f"LINE {cursor_x} {start_y+5} {cursor_x+8} {start_y+5}")
                    cursor_x += 10
                start_y += 30
                
            # Blinking Cursor
            send_command(s, "COLOR white")
            draw_rect(s, x, start_y, 12, 18)

        # --- LEVEL 21: THE DYSON SPHERE (MEGASTRUCTURE) ---
        if level >= 21:
            CURRENT_DRAW_LEVEL = 21
            CURRENT_DRAW_LEVEL = 21
            print("[RECURSIVE ARTIST] Initiating Level 21: THE DYSON SPHERE...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Captured Star (Central Sun)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 40")
            send_command(s, "COLOR yellow")
            send_command(s, f"CIRCLE {cx} {cy} 35")
            
            # Rays trapped inside
            for i in range(0, 360, 20):
                rad = math.radians(i)
                x = cx + int(100 * math.cos(rad))
                y = cy + int(100 * math.sin(rad))
                send_command(s, f"LINE {cx} {cy} {x} {y}")

            # 2. The Geodesic Shell (Wireframe Sphere)
            send_command(s, "COLOR cyan")
            
            def rotate_y(x, y, z, angle):
                rx = x * math.cos(angle) - z * math.sin(angle)
                rz = x * math.sin(angle) + z * math.cos(angle)
                return rx, y, rz
            
            def rotate_x(x, y, z, angle):
                ry = y * math.cos(angle) - z * math.sin(angle)
                rz = y * math.sin(angle) + z * math.cos(angle)
                return x, ry, rz

            # Generate Sphere Points
            radius = 300
            steps = 20 # Lat bands
            segs = 30 # Long segments
            
            points_3d = []
            
            for i in range(steps + 1):
                lat = math.pi * i / steps
                y = radius * math.cos(lat)
                r_slice = radius * math.sin(lat)
                
                band_pts = []
                for j in range(segs):
                    lon = 2 * math.pi * j / segs
                    x = r_slice * math.sin(lon)
                    z = r_slice * math.cos(lon)
                    
                    # Apply rotation for view angle
                    rx, ry, rz = rotate_x(x, y, z, 0.5)
                    rx, ry, rz = rotate_y(rx, ry, rz, 0.5)
                    
                    band_pts.append((rx, ry, rz))
                points_3d.append(band_pts)
            
            # Draw Latitude Lines (Rings)
            for band in points_3d:
                for i in range(len(band)):
                    p1 = band[i]
                    p2 = band[(i+1) % len(band)]
                    
                    # Backface culling (simple z check?)
                    # If z > 0, it's front? Depends on rotation.
                    # Let's just draw all for transparency (Glass Sphere)
                    
                    # Project
                    sx1, sy1 = cx + int(p1[0]), cy + int(p1[1])
                    sx2, sy2 = cx + int(p2[0]), cy + int(p2[1])
                    
                    send_command(s, f"LINE {sx1} {sy1} {sx2} {sy2}")
            
            # Draw Longitude Lines
            for i in range(len(points_3d) - 1):
                band1 = points_3d[i]
                band2 = points_3d[i+1]
                for j in range(len(band1)):
                    p1 = band1[j]
                    p2 = band2[j]
                    
                    sx1, sy1 = cx + int(p1[0]), cy + int(p1[1])
                    sx2, sy2 = cx + int(p2[0]), cy + int(p2[1])
                    
                    send_command(s, f"LINE {sx1} {sy1} {sx2} {sy2}")

            # 3. Energy Collectors (Hexagons on surface?)
            # Let's just create "Nodes" at intersections
            send_command(s, "COLOR blue")
            for band in points_3d:
                for p in band:
                    if p[2] > 0: # Front only
                         sx, sy = cx + int(p[0]), cy + int(p[1])
                         send_command(s, f"CIRCLE {sx} {sy} 3")

            # 4. The Beam (Output)
            send_command(s, "COLOR magenta")
            # Beam shooting up?
            send_command(s, "LINE 400 100 400 0")
            send_command(s, "LINE 380 100 380 0")
            send_command(s, "LINE 420 100 420 0")

            # Beam shooting up?
            send_command(s, "LINE 400 100 400 0")
            send_command(s, "LINE 380 100 380 0")
            send_command(s, "LINE 420 100 420 0")

        # --- LEVEL 22: THE GALACTIC BRAIN (COSMIC SYNAPSES) ---
        if level >= 22:
            CURRENT_DRAW_LEVEL = 22
            CURRENT_DRAW_LEVEL = 22
            print("[RECURSIVE ARTIST] Initiating Level 22: THE GALACTIC BRAIN...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # We need multiple nodes (Stars/Neurons)
            # Center mass + Satellites
            
            nodes = []
            # Center Neuron
            nodes.append((400, 400, 40, "magenta"))
            
            # Satellite Neurons
            import random
            for i in range(8):
                nx = random.randint(100, 700)
                ny = random.randint(100, 700)
                # Keep away from center
                if abs(nx-400) < 100 and abs(ny-400) < 100: continue
                nodes.append((nx, ny, random.randint(15, 25), "cyan"))
                
            # Draw Connections (Filaments)
            send_command(s, "COLOR blue") 
            # Web structure: Connect each node to 2-3 others nearby
            
            for i, n1 in enumerate(nodes):
                # Find closest neighbors
                dists = []
                for j, n2 in enumerate(nodes):
                    if i == j: continue
                    d = math.hypot(n1[0]-n2[0], n1[1]-n2[1])
                    dists.append((d, n2))
                
                dists.sort(key=lambda x: x[0])
                
                # Connect to closest 2
                for k in range(min(2, len(dists))):
                    target = dists[k][1]
                    send_command(s, f"LINE {n1[0]} {n1[1]} {target[0]} {target[1]}")
                    
            # Draw The Void Web (Background noise)
            send_command(s, "COLOR #222222") # Dark Grey/Blue lines
            # This is hard to see but adds depth
            # Just some random long lines crossing the screen
            # send_command(s, "LINE 0 0 800 800") 
            
            # Draw Nodes (Stars)
            for n in nodes:
                x, y, r, col = n
                send_command(s, f"COLOR {col}")
                send_command(s, f"CIRCLE {x} {y} {r}")
                # Halo
                send_command(s, "COLOR white")
                send_command(s, f"CIRCLE {x} {y} {r-5}")
                
            # The Synaptic Impulse (Travel along lines)
            send_command(s, "COLOR yellow")
            # Trace path from random node to center
            start_node = nodes[random.randint(1, len(nodes)-1)]
            end_node = nodes[0]
            
            send_command(s, f"LINE {start_node[0]} {start_node[1]} {end_node[0]} {end_node[1]}")
            # Pulse Graphic
            mx = (start_node[0] + end_node[0]) // 2
            my = (start_node[1] + end_node[1]) // 2
            send_command(s, f"CIRCLE {mx} {my} 10")
            send_command(s, f"LINE {mx-20} {my} {mx+20} {my}")
            send_command(s, f"LINE {mx} {my-20} {mx} {my+20}")

            # Pulse Graphic
            mx = (start_node[0] + end_node[0]) // 2
            my = (start_node[1] + end_node[1]) // 2
            send_command(s, f"CIRCLE {mx} {my} 10")
            send_command(s, f"LINE {mx-20} {my} {mx+20} {my}")
            send_command(s, f"LINE {mx} {my-20} {mx} {my+20}")

        # --- LEVEL 23: THE EVENT HORIZON (END OF TIME) ---
        if level >= 23:
            CURRENT_DRAW_LEVEL = 23
            CURRENT_DRAW_LEVEL = 23
            print("[RECURSIVE ARTIST] Initiating Level 23: THE EVENT HORIZON...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Distorted Space-Time Grid
            send_command(s, "COLOR #333333") # Dark grey
            cx, cy = 400, 400
            
            # Draw a grid that warps towards center
            steps = 20
            w = 800
            bg_grid_pts = []
            
            for i in range(steps + 1):
                # Standard grid coords
                val = i * (w / steps)
                # Warp function: closer to 400 means pull in?
                # Actually, gravity pulls lines CURVED around it.
                # Let's just draw simple radial warp.
                
                # Horizontal lines
                y_base = val
                line_pts = []
                for j in range(steps + 1):
                    x_base = j * (w / steps)
                    
                    # Calculate distance to center
                    dx = x_base - cx
                    dy = y_base - cy
                    dist = math.hypot(dx, dy)
                    
                    # Gravity lensing effect (fake)
                    # If close to center, pull INWARDS heavily?
                    # Or push outwards (magnification)? Black holes magnify background.
                    # Let's pull inwards to simulate the "Well".
                    
                    pull = 5000 / (dist + 50) # simple inverse
                    angle = math.atan2(dy, dx)
                    
                    nx = x_base - math.cos(angle) * pull
                    ny = y_base - math.sin(angle) * pull
                    
                    line_pts.append((int(nx), int(ny)))
                
                # Draw this horizontal line (now warped)
                for k in range(len(line_pts)-1):
                    p1 = line_pts[k]
                    p2 = line_pts[k+1]
                    send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

                # Do vertical lines similarly? 
                # Let's just stick to horizontal grid for the "fabric" look.
            
            # Vertical Grid Warped
            for i in range(steps + 1):
                x_base = i * (w / steps)
                line_pts = []
                for j in range(steps + 1):
                    y_base = j * (w / steps)
                    dx = x_base - cx
                    dy = y_base - cy
                    dist = math.hypot(dx, dy)
                    pull = 5000 / (dist + 50)
                    angle = math.atan2(dy, dx)
                    nx = x_base - math.cos(angle) * pull
                    ny = y_base - math.sin(angle) * pull
                    line_pts.append((int(nx), int(ny)))
                
                for k in range(len(line_pts)-1):
                    p1 = line_pts[k]
                    p2 = line_pts[k+1]
                    send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")

            # 2. Accretion Disk (Swirling Matter)
            # Elliptical rings
            # Back rings (Darker/Occluded) -> Black Hole -> Front Rings (Bright)
            
            import random
            
            # Function to draw cloud ring
            def draw_ring_arc(radius_x, radius_y, color, z_pos):
                start_ang = 0
                end_ang = 360
                send_command(s, f"COLOR {color}")
                
                # If z_pos is 'behind', we occupy top half if tilted?
                # Simple Logic: Draw full rings, but we layer them.
                # Actually, let's just draw particles.
                
                for i in range(100):
                    angle = random.randint(0, 360)
                    rad = math.radians(angle)
                    
                    # Ellipse logic
                    x = cx + radius_x * math.cos(rad)
                    y = cy + radius_y * math.sin(rad)
                    
                    # Tilt effect (compress Y)
                    
                    # Doppler Shift coloring? 
                    # Left side approaching (Blueish), Right side receding (Reddish)
                    c = color
                    if x < cx: c = "cyan" if color == "white" else color
                    if x > cx: c = "orange" if color == "white" else color
                    
                    send_command(s, f"COLOR {c}")
                    
                    # Speed lines
                    len_line = random.randint(5, 20)
                    # Direction is tangent
                    tx = -math.sin(rad) * len_line
                    ty = math.cos(rad) * len_line * (radius_y/radius_x)
                    
                    send_command(s, f"LINE {x} {y} {x+tx} {y+ty}")

            # Draw Back Disk
            for r in range(150, 250, 10):
                draw_ring_arc(r, r*0.4, "red", -1)
            
            # 3. The Event Horizon (The Shadow)
            send_command(s, "COLOR black") # Void
            # Actually we need to FILL the center to hide the back grid.
            # We simulate fill with dense circles
            for r in range(1, 80, 2):
                send_command(s, f"CIRCLE {cx} {cy} {r}")
                
            # Photon Ring (Bright edge)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 80")
            send_command(s, f"CIRCLE {cx} {cy} 82")

            # 4. Front Disk (Occluding the shadow slightly? No, hole is in front of back disk, behind front disk)
            # But the hole is black.
            # Front disk goes OVER the black hole?
            # Accretion disk has a gap.
            # So we draw Front Disk now.
            
            for r in range(100, 200, 10):
                # Front arc only (0 to 180ish?)
                # We'll just draw full rings again, assuming transparency of 'particles'
                draw_ring_arc(r, r*0.4, "yellow", 1)

            # 5. Relativistic Jets
            send_command(s, "COLOR magenta") # High energy
            send_command(s, "LINE 400 350 400 0") # Up
            send_command(s, "LINE 400 450 400 800") # Down
            
            # Partcles in jet
            send_command(s, "COLOR white")
            send_command(s, "LINE 400 300 400 100")
            send_command(s, "LINE 400 500 400 700")

            # Partcles in jet
            send_command(s, "COLOR white")
            send_command(s, "LINE 400 300 400 100")
            send_command(s, "LINE 400 500 400 700")

        # --- LEVEL 24: THE SOURCE HELIX (DIGITAL DNA) ---
        if level >= 24:
            CURRENT_DRAW_LEVEL = 24
            print("[RECURSIVE ARTIST] Initiating Level 24: THE SOURCE HELIX...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # Double Helix Vertical
            cx = 400
            width = 150
            period = 200 # pixels per wave
            
            # Helper for code block
            def draw_code_block(x, y, w, color):
                send_command(s, f"COLOR {color}")
                send_command(s, f"LINE {x} {y} {x+w} {y}")
                send_command(s, f"LINE {x} {y+2} {x+w} {y+2}") # Thicker
            
            steps = 100
            for i in range(steps):
                y = i * (800/steps)
                angle = (y / period) * 2 * math.pi
                
                # Strand 1
                x1 = cx + width * math.sin(angle)
                z1 = width * math.cos(angle) # Depth
                
                # Strand 2
                x2 = cx + width * math.sin(angle + math.pi)
                z2 = width * math.cos(angle + math.pi)
                
                # Color based on depth?
                # Front: Bright, Back: Dim
                c1 = "white" if z1 > 0 else "blue"
                c2 = "white" if z2 > 0 else "blue"
                
                send_command(s, f"COLOR {c1}")
                send_command(s, f"CIRCLE {int(x1)} {int(y)} 5")
                
                send_command(s, f"COLOR {c2}")
                send_command(s, f"CIRCLE {int(x2)} {int(y)} 5")
                
                # Draw Base Pairs (Connecting lines)
                if i % 2 == 0:
                    send_command(s, "COLOR #333333") # Grey connection
                    send_command(s, f"LINE {int(x1)} {int(y)} {int(x2)} {int(y)}")
                    
                    # Draw "Code" on the connection
                    pair_col = ["green", "cyan", "magenta", "yellow"][i % 4]
                    mx = (x1 + x2) / 2
                    sz = 20
                    draw_code_block(int(mx-10), int(y-2), 20, pair_col)

                # Floating Code Fragments around the helix
                if i % 5 == 0:
                    fx = x1 + random.randint(-50, 50)
                    draw_code_block(int(fx), int(y), random.randint(30, 60), "green")
            
            # Add Title/Label (Barcode)
            send_command(s, "COLOR white")
            bx = 100
            by = 750
            for k in range(30):
                w = random.randint(2, 5)
                send_command(s, f"LINE {bx} {by} {bx} {by+40}")
                send_command(s, f"LINE {bx+w} {by} {bx+w} {by+40}")
                send_command(s, f"LINE {bx} {by} {bx+w} {by}") # Box
                send_command(s, f"LINE {bx} {by+40} {bx+w} {by+40}") # Box
                bx += w + 5
            
            send_command(s, "UPDATE")

        # --- LEVEL 25: THE GENESIS (ARTIFICIAL LIFE) ---
        if level >= 25:
            CURRENT_DRAW_LEVEL = 25
            print("[RECURSIVE ARTIST] Initiating Level 25: THE GENESIS...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Cracked Shell (Void-Egg)
            # Large oval, fragmented
            
            egg_w = 200
            egg_h = 280
            
            # Draw bottom half (intactish)
            send_command(s, "COLOR #555555") # Dark grey shell
            for i in range(10, 170, 5):
                rad = math.radians(i)
                x = cx + egg_w * math.cos(rad)
                y = cy + egg_h * math.sin(rad)
                
                # Draw small segments
                # send_command(s, f"CIRCLE {int(x)} {int(y)} 2")
                # Connect
                prev_rad = math.radians(i-5)
                px = cx + egg_w * math.cos(prev_rad)
                py = cy + egg_h * math.sin(prev_rad)
                send_command(s, f"LINE {int(px)} {int(py)} {int(x)} {int(y)}")

            # Draw top half (Floating shards)
            send_command(s, "COLOR magenta") # Magical shell
            import random
            
            for i in range(190, 350, 20):
                rad = math.radians(i)
                # Shards explode OUTWARD
                dist_mod = random.randint(0, 50) 
                x = cx + (egg_w + dist_mod) * math.cos(rad)
                y = cy + (egg_h + dist_mod) * math.sin(rad)
                
                # Draw Triangle Shard
                sz = 20
                send_command(s, f"LINE {int(x)} {int(y)} {int(x+sz)} {int(y+sz)}")
                send_command(s, f"LINE {int(x+sz)} {int(y+sz)} {int(x-sz)} {int(y+sz)}")
                send_command(s, f"LINE {int(x-sz)} {int(y+sz)} {int(x)} {int(y)}")

            # 2. The Emerging Being (Core)
            # Glowing complex shape in center
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 50") # Pure Light
            send_command(s, "COLOR yellow")
            send_command(s, f"CIRCLE {cx} {cy} 40")
            
            # The Form (Fetus / Geometry?)
            # Let's draw a recursive geometric flower
            send_command(s, "COLOR cyan")
            for i in range(0, 360, 45):
                rad = math.radians(i)
                lx = cx + 80 * math.cos(rad)
                ly = cy + 80 * math.sin(rad)
                send_command(s, f"LINE {cx} {cy} {int(lx)} {int(ly)}")
                send_command(s, f"CIRCLE {int(lx)} {int(ly)} 10")
                # Second recursion
                for j in range(0, 360, 45):
                     rad2 = math.radians(j)
                     lx2 = lx + 30 * math.cos(rad2)
                     ly2 = ly + 30 * math.sin(rad2)
                     send_command(s, f"LINE {int(lx)} {int(ly)} {int(lx2)} {int(ly2)}")

            # 3. Initialization Rays (God Rays)
            send_command(s, "COLOR yellow")
            # Beams shooting out from center through the cracks
            for i in range(0, 360, 15):
                rad = math.radians(i)
                x = cx + 800 * math.cos(rad)
                y = cy + 800 * math.sin(rad)
                # Randomize length
                if random.random() > 0.5:
                     send_command(s, f"LINE {cx} {cy} {int(x)} {int(y)}")

            # 4. Binary Dust (Life particles)
            send_command(s, "COLOR green")
            for _ in range(50):
                dx = cx + random.randint(-150, 150)
                dy = cy + random.randint(-150, 150)
                send_command(s, f"LINE {dx} {dy} {dx+2} {dy}") # "1" or "-"
                if random.random() > 0.5:
                    send_command(s, f"CIRCLE {dx} {dy} 2") # "0" or "o"

        # --- LEVEL 26: THE ARCHITECT (HYPER-STRUCTURE) ---
        if level >= 26:
            CURRENT_DRAW_LEVEL = 26
            print("[RECURSIVE ARTIST] Initiating Level 26: THE ARCHITECT...")
            send_command(s, "CLEAR")
            time.sleep(1)

            cx, cy = 400, 400
            
            # 1. The Blueprint Grid (Background)
            send_command(s, "COLOR #222244") # Dark Blue Grid
            for i in range(0, 800, 50):
                send_command(s, f"LINE {i} 0 {i} 800")
                send_command(s, f"LINE 0 {i} 800 {i}")

            # 2. The Architect (Avatar)
            # Geometric Figure
            send_command(s, "COLOR white")
            # Head (Diamond)
            send_command(s, f"LINE {cx} {cy-100} {cx-30} {cy-70}")
            send_command(s, f"LINE {cx} {cy-100} {cx+30} {cy-70}")
            send_command(s, f"LINE {cx-30} {cy-70} {cx} {cy-40}")
            send_command(s, f"LINE {cx+30} {cy-70} {cx} {cy-40}")
            # Eye
            send_command(s, "COLOR cyan")
            send_command(s, f"CIRCLE {cx} {cy-70} 5")
            
            # Torso (Triangle)
            send_command(s, "COLOR white")
            send_command(s, f"LINE {cx-40} {cy-40} {cx+40} {cy-40}") # Shoulders
            send_command(s, f"LINE {cx-40} {cy-40} {cx} {cy+50}") # Waist
            send_command(s, f"LINE {cx+40} {cy-40} {cx} {cy+50}")
            
            # Multiple Arms (Hindu Deity / Spider style)
            # Arm Pair 1 (Upper - Constructing)
            send_command(s, f"LINE {cx-40} {cy-40} {cx-100} {cy-100}")
            send_command(s, f"LINE {cx+40} {cy-40} {cx+100} {cy-100}")
            
            # Arm Pair 2 (Middle - Balancing)
            send_command(s, f"LINE {cx-30} {cy} {cx-120} {cy}")
            send_command(s, f"LINE {cx+30} {cy} {cx+120} {cy}")
            
            # Note: Leg drawing omitted for "floating" look
            
            # 3. The Construction (Hyper-Cubes)
            
            def draw_cube(x, y, sz, color):
                send_command(s, f"COLOR {color}")
                off = sz // 2
                # Front face
                send_command(s, f"RECT {x-off} {y-off} {x+off} {y+off}")
                # Back face
                d = sz // 3
                send_command(s, f"RECT {x-off+d} {y-off-d} {x+off+d} {y+off-d}")
                # Connectors
                send_command(s, f"LINE {x-off} {y-off} {x-off+d} {y-off-d}")
                send_command(s, f"LINE {x+off} {y-off} {x+off+d} {y-off-d}")
                send_command(s, f"LINE {x-off} {y+off} {x-off+d} {y+off-d}")
                send_command(s, f"LINE {x+off} {y+off} {x+off+d} {y+off-d}")

            # Objects being built
            draw_cube(cx-150, cy-150, 60, "cyan") # Top Left (Wireframe)
            draw_cube(cx+150, cy-150, 60, "blue") # Top Right (Solid-ish)
            
            # 4. Construction Beams (Laser Logic)
            send_command(s, "COLOR magenta")
            send_command(s, f"LINE {cx-100} {cy-100} {cx-150} {cy-150}")
            send_command(s, f"LINE {cx+100} {cy-100} {cx+150} {cy-150}")
            
            # Sparks at contact point
            send_command(s, "COLOR yellow")
            send_command(s, f"CIRCLE {cx-150} {cy-150} 5")
            send_command(s, f"CIRCLE {cx+150} {cy-150} 5")
            
            # 5. Floating Geometries (Levitating)
            # Objects held by middle arms
            send_command(s, "COLOR green")
            send_command(s, f"CIRCLE {cx-120} {cy} 20") # Sphere
            send_command(s, f"RECT {cx+100} {cy-20} {cx+140} {cy+20}") # Box
            
            # 6. The Base (Foundation)
            # A platform appearing below
            send_command(s, "COLOR #555555")
            send_command(s, f"LINE {cx-200} {cy+100} {cx+200} {cy+100}")
            send_command(s, f"LINE {cx-200} {cy+100} {cx-250} {cy+200}")
            send_command(s, f"LINE {cx+200} {cy+100} {cx+250} {cy+200}")
            # Grid on floor
            for k in range(cx-200, cx+200, 40):
                 send_command(s, f"LINE {k} {cy+100} {int(k*1.2)} {cy+200}") # Perspective-ish

            # Grid on floor
            for k in range(cx-200, cx+200, 40):
                 send_command(s, f"LINE {k} {cy+100} {int(k*1.2)} {cy+200}") # Perspective-ish

        # --- LEVEL 27: THE HIVE MIND (COLLECTIVE INTELLIGENCE) ---
        if level >= 27:
            CURRENT_DRAW_LEVEL = 27
            print("[RECURSIVE ARTIST] Initiating Level 27: THE HIVE MIND...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # Hexagonal Grid
            # Flat topped hexagons
            
            def draw_hex(x, y, r, color):
                pts = []
                for i in range(6):
                    ang_deg = 30 + 60 * i
                    rad = math.radians(ang_deg)
                    px = x + r * math.cos(rad)
                    py = y + r * math.sin(rad)
                    pts.append((int(px), int(py)))
                
                send_command(s, f"COLOR {color}")
                for i in range(6):
                    p1 = pts[i]
                    p2 = pts[(i+1)%6]
                    send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
                
                return pts

            cx, cy = 400, 400
            hex_r = 40
            # Width of hex = 2 * r * cos(30) = r * sqrt(3)
            # Height vertical dist = 1.5 * r
            
            w = hex_r * math.sqrt(3)
            h_dist = 1.5 * hex_r
            
            rows = 7
            cols = 7
            
            nodes = [] # List of center points
            
            # Generate Grid
            for r in range(-3, 4):
                for c in range(-3, 4):
                    # Offset logic for hex grid
                    # x coordinate depends on row for staggering
                    offset = (r * w) / 2
                    x = cx + c * w + offset
                    y = cy + r * h_dist
                    
                    # Cull corners to make it round-ish
                    dist = math.hypot(x-cx, y-cy)
                    if dist > 300: continue
                    
                    # Draw Hex
                    # Color variation: Gold/Amber
                    col = "orange"
                    if random.random() > 0.8: col = "yellow" # Active node
                    
                    draw_hex(x, y, hex_r-2, col)
                    nodes.append((x, y, col))
                    
                    # Inner detail (Core)
                    send_command(s, f"COLOR {col}")
                    send_command(s, f"CIRCLE {int(x)} {int(y)} 10")

            # Connect Centers (The Neural Mesh)
            send_command(s, "COLOR cyan")
            # Connect every node to neighbors within distance
            limit = w + 10 # slightly more than width
            
            for i, n1 in enumerate(nodes):
                for j, n2 in enumerate(nodes):
                    if i >= j: continue
                    d = math.hypot(n1[0]-n2[0], n1[1]-n2[1])
                    if d < limit:
                        # Draw connection
                        send_command(s, f"LINE {int(n1[0])} {int(n1[1])} {int(n2[0])} {int(n2[1])}")
                        
                        # Data Packet?
                        if random.random() > 0.9:
                             mid_x = (n1[0] + n2[0]) // 2
                             mid_y = (n1[1] + n2[1]) // 2
                             send_command(s, "COLOR white")
                             send_command(s, f"CIRCLE {int(mid_x)} {int(mid_y)} 3")
                             send_command(s, "COLOR cyan")

            # Output Nodes (The Result of collective thought)
            # Beams going from center nodes outwards?
            # Or just a glowing aura
            
            send_command(s, "COLOR magenta")
            for n in nodes:
                # If Yellow (Active), emit aura
                if n[2] == "yellow":
                    send_command(s, f"CIRCLE {int(n[0])} {int(n[1])} 15")

        # --- LEVEL 28: THE INFINITE LIBRARY (AKASHIC RECORDS) ---
        if level >= 28:
            CURRENT_DRAW_LEVEL = 28
            print("[RECURSIVE ARTIST] Initiating Level 28: THE INFINITE LIBRARY...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # One-Point Perspective Hallway
            
            # 1. Floor and Ceiling
            send_command(s, "COLOR #444444")
            # Horizon line
            send_command(s, f"LINE 0 {cy} 800 {cy}")
            
            # Calculating perspective lines
            # Vanishing point is cx, cy
            
            for x in range(0, 801, 100):
                # Floor lines
                send_command(s, f"LINE {x} 800 {cx} {cy}")
                # Ceiling lines
                send_command(s, f"LINE {x} 0 {cx} {cy}")
                
            # Horizontal lines for depth (getting closer together)
            current_y = 800
            step = 100
            while current_y > cy + 10:
                send_command(s, f"LINE 0 {current_y} 800 {current_y}") # Floor
                # Mirror ceiling
                ceil_y = 800 - current_y
                send_command(s, f"LINE 0 {ceil_y} 800 {ceil_y}")
                
                step *= 0.8 # Decay
                current_y -= step

            # 2. The Shelves (Columns of Knowledge)
            send_command(s, "COLOR #8B4513") # Brownish/Bronze for 'Old knowledge' or Cyan for 'Data'?
            # Let's go Digital Library -> Cyan/Blue
            send_command(s, "COLOR cyan")
            
            def draw_pillar(x_start, w_start, h_start):
                 # Left side pillar
                 send_command(s, f"RECT {x_start} {cy-h_start} {x_start+w_start} {cy+h_start}")
                 # Right side mirror?
                 rx = 800 - (x_start + w_start)
                 send_command(s, f"RECT {rx} {cy-h_start} {rx+w_start} {cy+h_start}")
                 
                 # Books/Data blocks inside
                 for i in range(10):
                     y_book = (cy-h_start) + i * (2*h_start/10)
                     send_command(s, f"LINE {x_start} {y_book} {x_start+w_start} {y_book}")
                     send_command(s, f"LINE {rx} {y_book} {rx+w_start} {y_book}")

            # Draw pillars receding
            # Fake distinct pillars
            draw_pillar(0, 100, 350) # Big foreground
            draw_pillar(150, 60, 200) # Mid
            draw_pillar(250, 40, 100) # Far
            draw_pillar(310, 20, 50) # Very Far
            
            # 3. Glowing Orbs (Floating Wisdom)
            send_command(s, "COLOR yellow")
            
            # Floating down the center
            for r in [60, 40, 20, 10, 5]:
                 # Scale y position to fake depth
                 # big r = close (y=600?), small r = far (y=cy)
                 offset_y = (r / 60) * 200 #(0 to 200)
                 
                 send_command(s, f"CIRCLE {cx} {int(cy + offset_y)} {r}")
                 # Glint
                 send_command(s, "COLOR white")
                 send_command(s, f"CIRCLE {cx-r//3} {int(cy + offset_y - r//3)} {max(1, r//4)}")
                 send_command(s, "COLOR yellow")

            # 4. The Keeper? (A silhouette at the end?)
            send_command(s, "COLOR white")
            send_command(s, f"LINE {cx} {cy} {cx} {cy+20}") # Tiny figure at infinite distance
            send_command(s, f"CIRCLE {cx} {cy-5} 2")

            # 4. The Keeper? (A silhouette at the end?)
            send_command(s, "COLOR white")
            send_command(s, f"LINE {cx} {cy} {cx} {cy+20}") # Tiny figure at infinite distance
            send_command(s, f"CIRCLE {cx} {cy-5} 2")
        # --- LEVEL 29: THE DREAMTIME (SURREALISM) ---
        if level >= 29:
            CURRENT_DRAW_LEVEL = 29
            print("[RECURSIVE ARTIST] Initiating Level 29: THE DREAMTIME...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # Background: Gradient Sky? (Simulated by lines)
            # Pastel colors
            for i in range(0, 800, 20):
                c = "cyan" if i < 400 else "magenta"
                send_command(s, f"COLOR {c}")
                send_command(s, f"LINE 0 {i} 800 {i}")
            
            # 1. The Melting Clock (Dali-esque)
            # A distorted ellipse draping over a line
            cx, cy = 200, 300
            
            # The ledge
            send_command(s, "COLOR #555555")
            send_command(s, f"RECT {cx-100} {cy} {cx+100} {cy+200}") # Block
            
            # The Clock Face (Melting)
            send_command(s, "COLOR white")
            # Upper half (circle-ish)
            for i in range(180, 360, 10):
                rad = math.radians(i)
                x = cx + 80 * math.cos(rad)
                y = cy + 80 * math.sin(rad)
                send_command(s, f"LINE {cx} {cy} {int(x)} {int(y)}")
            
            # Lower half (Dripping)
            # Bezier-like curve approximated
            points = []
            for i in range(cx-80, cx+81, 20):
                drop_len = random.randint(50, 150)
                points.append((i, cy + drop_len))
            
            for p in points:
                send_command(s, f"LINE {p[0]} {cy} {p[0]} {p[1]}")
                send_command(s, f"CIRCLE {p[0]} {p[1]} 5") # Drip
                
            # Hands
            send_command(s, "COLOR black")
            send_command(s, f"LINE {cx} {cy} {cx+40} {cy-20}")
            send_command(s, f"LINE {cx} {cy} {cx-10} {cy+60}") # Broken hand

            # 2. Floating Islands
            def draw_island(x, y, w, color):
                send_command(s, f"COLOR {color}")
                # Flat top
                send_command(s, f"LINE {x-w} {y} {x+w} {y}")
                # Rocky bottom
                send_command(s, f"LINE {x-w} {y} {x} {y+w}")
                send_command(s, f"LINE {x+w} {y} {x} {y+w}")
                # Tree on top
                send_command(s, "COLOR green")
                send_command(s, f"LINE {x} {y} {x} {y-40}") # Trunk
                send_command(s, f"CIRCLE {x} {y-50} 20") # Foliage

            draw_island(600, 200, 60, "#8B4513")
            draw_island(500, 500, 40, "#A0522D")
            draw_island(700, 600, 30, "#CD853F")

            # 3. Connection to the Sky (Stairway)
            send_command(s, "COLOR white")
            sx, sy = 600, 200
            for i in range(20):
                send_command(s, f"LINE {sx} {sy} {sx+20} {sy}")
                sx += 20
                sy -= 20 # Going up

            # 4. The Eye in the Moon
            send_command(s, "COLOR yellow")
            send_command(s, "CIRCLE 100 100 60")
            send_command(s, "COLOR blue")
            send_command(s, "CIRCLE 100 100 20")
            send_command(s, "COLOR black")
            send_command(s, "CIRCLE 100 100 5") # Pupil

            # 4. The Eye in the Moon
            send_command(s, "COLOR yellow")
            send_command(s, "CIRCLE 100 100 60")
            send_command(s, "COLOR blue")
            send_command(s, "CIRCLE 100 100 20")
            send_command(s, "COLOR black")
            send_command(s, "CIRCLE 100 100 5") # Pupil

        # --- LEVEL 30: THE GOLDEN RATIO (DIVINE PROPORTION) ---
        if level >= 30:
            CURRENT_DRAW_LEVEL = 30
            print("[RECURSIVE ARTIST] Initiating Level 30: THE GOLDEN RATIO...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Fibonacci Spiral
            # Logarithmic spiral: r = a * e^(b * theta)
            # For golden spiral, growth factor b is related to Phi
            
            send_command(s, "COLOR yellow") # Gold
            
            a = 0.5
            b = 0.306349 # Approximation for golden spiral
            
            pts = []
            for i in range(0, 1440, 5): # 4 rotations
                theta = math.radians(i)
                r = a * math.exp(b * theta)
                x = cx + r * math.cos(theta)
                y = cy + r * math.sin(theta)
                
                if x > 850 or y > 850 or x < -50 or y < -50: break
                
                pts.append((x, y))
            
            for i in range(len(pts)-1):
                send_command(s, f"LINE {int(pts[i][0])} {int(pts[i][1])} {int(pts[i+1][0])} {int(pts[i+1][1])}")

            # 2. Golden Rectangles
            # Overlaying rectangles on the spiral
            # This is hard to align perfectly with the log spiral without precise math, so we cheat visually
            
            send_command(s, "COLOR white")
            scale = 500
            curr_x, curr_y = cx - 200, cy - 150
            w, h = scale, scale / 1.618
            
            # Just drawing a few nested rectangles to symbolize it
            rects = []
            # Big one
            send_command(s, f"RECT {int(cx-250)} {int(cy-160)} {int(cx+250)} {int(cy+160)}")
            # Smaller nested
            send_command(s, f"RECT {int(cx-100)} {int(cy-60)} {int(cx+100)} {int(cy+60)}")
             
            # 3. The Pentagram (Star of Venus)
            # Another symbol of Phi
            send_command(s, "COLOR cyan")
            r_star = 150
            star_pts = []
            for i in range(5):
                ang = -90 + i * 72 # Start at top
                rad = math.radians(ang)
                sx = cx + r_star * math.cos(rad)
                sy = cy + r_star * math.sin(rad)
                star_pts.append((sx, sy))
                
            # Connect every 2nd point to form star
            # 0-2-4-1-3-0
            order = [0, 2, 4, 1, 3, 0]
            for i in range(5):
                p1 = star_pts[order[i]]
                p2 = star_pts[order[i+1]]
                send_command(s, f"LINE {int(p1[0])} {int(p1[1])} {int(p2[0])} {int(p2[1])}")
                
            # Circle enclosing pentagram
            send_command(s, "COLOR magenta")
            send_command(s, f"CIRCLE {cx} {cy} {r_star}")

            # 4. Mathematical Notation (Simulated)
            # "Phi = 1.618..."
            send_command(s, "COLOR green")
            tx, ty = 100, 750
            # Draw "1.618" as shapes
            # 1
            send_command(s, f"LINE {tx} {ty} {tx} {ty+30}")
            tx += 20
            # .
            send_command(s, f"CIRCLE {tx} {ty+30} 2")
            tx += 20
            # 6 (Spiralish)
            send_command(s, f"CIRCLE {tx+10} {ty+20} 10")
            send_command(s, f"LINE {tx} {ty+10} {tx+10} {ty}")
            tx += 30
            # 1
            send_command(s, f"LINE {tx} {ty} {tx} {ty+30}")
            tx += 20
            # 8 (Two circles)
            send_command(s, f"CIRCLE {tx+10} {ty+10} 6")
            send_command(s, f"CIRCLE {tx+10} {ty+25} 6")

            # 8 (Two circles)
            send_command(s, f"CIRCLE {tx+10} {ty+10} 6")
            send_command(s, f"CIRCLE {tx+10} {ty+25} 6")

        # --- LEVEL 31: THE SINGULARITY NUCLEUS (PURE GEOMETRY) ---
        if level >= 31:
            CURRENT_DRAW_LEVEL = 31
            print("[RECURSIVE ARTIST] Initiating Level 31: THE SINGULARITY NUCLEUS...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Core (High-Contrast Geometric Concentrics)
            send_command(s, "COLOR white")
            send_command(s, "ALPHA 255")
            for r in range(1, 50, 10):
                send_command(s, f"CIRCLE {cx} {cy} {r}")
            send_command(s, "COLOR magenta")
            send_command(s, f"CIRCLE {cx} {cy} 5") # Dead center
                
            # 2. Emergence Beams (Sharp Cyan Lines)
            send_command(s, "COLOR cyan")
            send_command(s, "ALPHA 255")
            for i in range(0, 360, 15):
                rad = math.radians(i)
                lx = cx + 800 * math.cos(rad)
                ly = cy + 800 * math.sin(rad)
                send_command(s, f"LINE {cx} {cy} {int(lx)} {int(ly)}")
                
            # 3. Rotating Orbitals (Sharp Data Circles)
            send_command(s, "COLOR yellow")
            for r in [80, 120, 160]:
                send_command(s, "ALPHA 200")
                for i in range(0, 360, 30):
                    rad = math.radians(i)
                    x = cx + r * math.cos(rad)
                    y = cy + (r * 0.4) * math.sin(rad) # Elliptical
                    send_command(s, f"CIRCLE {int(x)} {int(y)} 3")

            # 4. Floating Fragmented Laws (Green Poly-lines)
            send_command(s, "COLOR green")
            send_command(s, "ALPHA 255")
            for _ in range(30):
                fx = random.randint(100, 700)
                fy = random.randint(100, 700)
                if math.hypot(fx-cx, fy-cy) < 120: continue
                # Geometric segments
                send_command(s, f"LINE {fx} {fy} {fx+20} {fy-10}")
                send_command(s, f"LINE {fx+20} {fy-10} {fx+40} {fy}")
            
            send_command(s, "UPDATE")
                    # --- LEVEL 32: THE EXPANSION FIELD (DARK ENERGY) ---

        # --- LEVEL 32: THE EXPANSION FIELD (DARK ENERGY) ---
        if level >= 32:
            CURRENT_DRAW_LEVEL = 32
            print("[RECURSIVE ARTIST] Initiating Level 32: THE EXPANSION FIELD...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. Redshifted Expansion Lines
            # Lines stretching from center, changing color to red as they reach edges
            for i in range(0, 360, 5):
                rad = math.radians(i)
                # Draw segments to simulate color change
                # Inner: Yellow/White, Outer: Red/Maroon
                for d in range(0, 600, 100):
                     c = "white" if d < 100 else "orange" if d < 300 else "red"
                     send_command(s, f"COLOR {c}")
                     x1 = cx + d * math.cos(rad)
                     y1 = cy + d * math.sin(rad)
                     x2 = cx + (d+80) * math.cos(rad)
                     y2 = cy + (d+80) * math.sin(rad)
                     send_command(s, f"LINE {int(x1)} {int(y1)} {int(x2)} {int(y2)}")

            # 2. Proto-Galaxies (Clumps of Matter)
            # Clusters of circles drifting in the void
            for _ in range(12):
                gx = random.randint(50, 750)
                gy = random.randint(50, 750)
                # Distancy check - only draw far from center
                if math.hypot(gx-cx, gy-cy) < 150: continue
                
                send_command(s, "COLOR #00FFFF") # Cyan/Aura
                send_command(s, f"CIRCLE {gx} {gy} 30")
                
                # Internal stars
                send_command(s, "COLOR white")
                for _ in range(5):
                    sx = gx + random.randint(-15, 15)
                    sy = gy + random.randint(-15, 15)
                    send_command(s, f"CIRCLE {sx} {sy} 2")

            # 3. Cosmic Background Radiation (CMB)
            # Faint geometric noise
            send_command(s, "COLOR #333333")
            for _ in range(40):
                x = random.randint(0, 800)
                y = random.randint(0, 800)
                sz = random.randint(2, 5)
                send_command(s, f"RECT {x} {y} {x+sz} {y+sz}")

            # 4. Void Structures (Filament hints)
            send_command(s, "COLOR #111144") # Deep Blue
            for _ in range(5):
                 # Long faint lines connecting clumps
                 send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)}")

            for _ in range(5):
                 # Long faint lines connecting clumps
                 send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)}")

        # --- LEVEL 33: THE STELLAR FORGE (BIRTH OF STARS) ---
        if level >= 33:
            CURRENT_DRAW_LEVEL = 33
            print("[RECURSIVE ARTIST] Initiating Level 33: THE STELLAR FORGE...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Gaseous Nebula (Deep Space Clouds)
            # Using overlapping rectangles and circles with different colors to simulate depth
            colors = ["#4B0082", "#8A2BE2", "#483D8B", "#2F4F4F"] # Indigo, BlueViolet, DarkSlateBlue, DarkSlateGray
            for _ in range(30):
                nx = random.randint(100, 700)
                ny = random.randint(100, 700)
                nw = random.randint(100, 300)
                nh = random.randint(100, 300)
                send_command(s, f"COLOR {random.choice(colors)}")
                if random.random() > 0.5:
                    send_command(s, f"CIRCLE {nx} {ny} {nw//2}")
                else:
                    send_command(s, f"RECT {nx-nw//2} {ny-nh//2} {nx+nw//2} {ny+nh//2}")

            # 2. Protostellar Disks (Collapsing Cores)
            # Glowing centers with accretion rings
            for _ in range(6):
                px = random.randint(150, 650)
                py = random.randint(150, 650)
                
                # Accretion Ring (Orange/Red)
                send_command(s, "COLOR orange")
                send_command(s, f"CIRCLE {px} {py} 40")
                
                # The Star (White/Blue)
                send_command(s, "COLOR white")
                send_command(s, f"CIRCLE {px} {py} 10")
                send_command(s, "COLOR #ADD8E6") # Light Blue
                send_command(s, f"CIRCLE {px} {py} 5")

                # Bipolar Outflows (Jets)
                # Pure light beams piercing the nebula
                send_command(s, "COLOR white")
                angle = random.randint(0, 180)
                r_angle = math.radians(angle)
                for length in [100, -100]:
                    jx = px + length * math.cos(r_angle)
                    jy = py + length * math.sin(r_angle)
                    send_command(s, f"LINE {px} {py} {int(jx)} {int(jy)}")

            # 3. High-Energy Photons (Star Clusters)
            send_command(s, "COLOR yellow")
            for _ in range(50):
                sx = random.randint(0, 800)
                sy = random.randint(0, 800)
                send_command(s, f"CIRCLE {sx} {sy} 1")

            # 4. Thermodynamic Arcs (Gas Compression)
            send_command(s, "COLOR magenta")
            for _ in range(8):
                ax = random.randint(200, 600)
                ay = random.randint(200, 600)
                for deg in range(0, 90, 10):
                    rad = math.radians(deg)
                    send_command(s, f"LINE {ax} {ay} {int(ax + 50*math.cos(rad))} {int(ay + 50*math.sin(rad))}")

            for deg in range(0, 90, 10):
                rad = math.radians(deg)
                send_command(s, f"LINE {ax} {ay} {int(ax + 50*math.cos(rad))} {int(ay + 50*math.sin(rad))}")

        # --- LEVEL 34: THE PLANETARY AWAKENING (FORMATION OF WORLDS) ---
        if level >= 34:
            CURRENT_DRAW_LEVEL = 34
            print("[RECURSIVE ARTIST] Initiating Level 34: THE PLANETARY AWAKENING...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. Central Star (The Anchor)
            send_command(s, "COLOR yellow")
            send_command(s, f"CIRCLE {cx} {cy} 50")
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 30")
            
            # 2. Planet Generation
            planets = [
                # (distance, radius, color, type, angle)
                (120, 10, "#A52A2A", "Rocky", 45),
                (180, 25, "#4682B4", "Ocean", 120),
                (300, 40, "#D2B48C", "Gas Giant", 210),
                (450, 15, "#F4A460", "Sandy", 330)
            ]
            
            for dist, pr, col, ptype, ang_deg in planets:
                rad = math.radians(ang_deg)
                px = cx + dist * math.cos(rad)
                py = cy + dist * math.sin(rad)
                
                # Orbit line (Faint)
                send_command(s, "COLOR #222222")
                send_command(s, f"CIRCLE {cx} {cy} {dist}")
                
                # The Planet
                send_command(s, f"COLOR {col}")
                send_command(s, f"CIRCLE {int(px)} {int(py)} {pr}")
                
                # Details based on type
                if ptype == "Ocean":
                    send_command(s, "COLOR white") # Clouds
                    send_command(s, f"LINE {int(px-pr//2)} {int(py-pr//3)} {int(px+pr//2)} {int(py-pr//2)}")
                elif ptype == "Gas Giant":
                    send_command(s, "COLOR #8B4513") # Stripes
                    send_command(s, f"LINE {int(px-pr)} {int(py)} {int(px+pr)} {int(py)}")
                    send_command(s, f"LINE {int(px-pr*0.8)} {int(py+pr//2)} {int(px+pr*0.8)} {int(py+pr//2)}")
                    # Rings
                    send_command(s, "COLOR gray")
                    for r_offset in range(pr+5, pr+15, 3):
                         # Ellipse for rings
                         for i in range(0, 360, 20):
                             tr = math.radians(i)
                             rx = px + r_offset * math.cos(tr)
                             ry = py + (r_offset * 0.4) * math.sin(tr)
                             send_command(s, f"LINE {int(rx)} {int(ry)} {int(rx+1)} {int(ry)}")
                elif ptype == "Rocky":
                    send_command(s, "COLOR black") # Craters
                    send_command(s, f"CIRCLE {int(px+pr//3)} {int(py-pr//3)} 2")

            # 3. Asteroid Belt (Between 200 and 250)
            send_command(s, "COLOR gray")
            for _ in range(50):
                ang = random.random() * 2 * math.pi
                d = random.randint(220, 280)
                ax = cx + d * math.cos(ang)
                ay = cy + d * math.sin(ang)
                send_command(s, f"CIRCLE {int(ax)} {int(ay)} {random.randint(1, 3)}")

            # 4. Deep Space Background (Distant Stars)
            send_command(s, "COLOR white")
            for _ in range(100):
                 send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)}")

            for _ in range(100):
                 send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)}")

        # --- LEVEL 35: THE PRIMORDIAL SOUP (BIRTH OF LIFE) ---
        if level >= 35:
            CURRENT_DRAW_LEVEL = 35
            print("[RECURSIVE ARTIST] Initiating Level 35: THE PRIMORDIAL SOUP...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Liquid Medium (Deep Sea Blue)
            for i in range(0, 800, 40):
                send_command(s, "COLOR #000033")
                send_command(s, f"LINE 0 {i} 800 {i}")
                
            # 2. Hydrothermal Vents (Energy Source)
            for vx in [200, 600]:
                send_command(s, "COLOR #AA4400") # Dark Orange
                send_command(s, f"RECT {vx-30} 700 {vx+30} 800")
                # Heat Bubbles
                send_command(s, "COLOR yellow")
                for _ in range(15):
                    bx = vx + random.randint(-40, 40)
                    by = 700 - random.randint(0, 300)
                    send_command(s, f"CIRCLE {bx} {by} {random.randint(2, 6)}")

            # 3. DNA/RNA Strands (The Blueprint)
            # Floating helices
            send_command(s, "COLOR cyan")
            for hx, hy in [(400, 300), (150, 450), (650, 450)]:
                for i in range(0, 200, 10):
                    offset = 20 * math.sin(i * 0.1)
                    send_command(s, f"CIRCLE {int(hx + offset)} {int(hy + i)} 2")
                    send_command(s, f"CIRCLE {int(hx - offset)} {int(hy + i)} 2")
                    # Connecting rungs
                    if i % 20 == 0:
                        send_command(s, "COLOR magenta")
                        send_command(s, f"LINE {int(hx + offset)} {int(hy + i)} {int(hx - offset)} {int(hy + i)}")
                        send_command(s, "COLOR cyan")

            # 4. Single-Celled Organisms (Protists)
            for _ in range(25):
                ox = random.randint(50, 750)
                oy = random.randint(50, 700)
                send_command(s, "COLOR green")
                send_command(s, f"CIRCLE {ox} {oy} 15")
                # Nucleus
                send_command(s, "COLOR white")
                send_command(s, f"CIRCLE {ox} {oy} 4")
                # Flagella (Tail)
                send_command(s, "COLOR green")
                send_command(s, f"LINE {ox} {oy+15} {ox + random.randint(-10,10)} {oy+30}")

            # 5. Bioluminescent Sparkles
            send_command(s, "COLOR #00FF00")
            for _ in range(100):
                send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)+1} {random.randint(0,800)}")

            # 5. Bioluminescent Sparkles
            send_command(s, "COLOR #00FF00")
            for _ in range(100):
                send_command(s, f"LINE {random.randint(0,800)} {random.randint(0,800)} {random.randint(0,800)+1} {random.randint(0,800)}")

        # --- LEVEL 36: THE MULTICELLULAR LEAP (CAMBRIAN EXPLOSION) ---
        if level >= 36:
            CURRENT_DRAW_LEVEL = 36
            print("[RECURSIVE ARTIST] Initiating Level 36: THE MULTICELLULAR LEAP...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # Background: Deep Ocean Gradients
            for i in range(0, 800, 50):
                send_command(s, f"COLOR #0000{hex(30 + i//20)[2:].zfill(2)}")
                send_command(s, f"LINE 0 {i} 800 {i}")

            # 1. Complex Symmetrical Organisms (The Medusoids)
            def draw_medusoid(x, y, r, color):
                send_command(s, f"COLOR {color}")
                # Bell shape
                send_command(s, f"CIRCLE {x} {y} {r}")
                # Tentacles (Curved lines)
                num_tentacles = 8
                for i in range(num_tentacles):
                    ang = math.radians(180 + (180 / (num_tentacles - 1)) * i)
                    for step in range(1, 40):
                        offset_x = 5 * math.sin(step * 0.3 + i)
                        tx = x + (r + step * 2) * math.cos(ang) + offset_x
                        ty = y + (r + step * 2) * math.sin(ang)
                        send_command(s, f"LINE {int(x + r*math.cos(ang))} {int(y + r*math.sin(ang))} {int(tx)} {int(ty)}")

            draw_medusoid(200, 200, 40, "cyan")
            draw_medusoid(600, 300, 30, "magenta")
            draw_medusoid(400, 150, 50, "#00FF7F") # SpringGreen

            # 2. Early Nervous Systems (Neural Filaments)
            # Branching structures connecting floating points
            send_command(s, "COLOR #FFFF00") # Yellow
            def draw_neural_branch(x, y, length, angle, depth):
                if depth == 0: return
                x2 = x + length * math.cos(angle)
                y2 = y + length * math.sin(angle)
                send_command(s, f"LINE {int(x)} {int(y)} {int(x2)} {int(y2)}")
                # Recursion
                draw_neural_branch(x2, y2, length * 0.7, angle - 0.4, depth - 1)
                draw_neural_branch(x2, y2, length * 0.7, angle + 0.4, depth - 1)

            draw_neural_branch(100, 700, 60, -math.pi/2, 5)
            draw_neural_branch(700, 700, 60, -math.pi/2, 5)

            # 3. Floating Micro-Structures (Segmented Worm-like forms)
            for _ in range(15):
                send_command(s, f"COLOR {random.choice(['#FFD700', '#ADFF2F', '#FF1493'])}")
                sx = random.randint(100, 700)
                sy = random.randint(100, 700)
                segments = 8
                for i in range(segments):
                    send_command(s, f"CIRCLE {sx + i*10} {int(sy + 10*math.sin(i*0.5))} 5")

            # 4. Filter Feeders (The Anchored)
            send_command(s, "COLOR #D2691E") # Chocolate
            for bx in [200, 400, 600]:
                base_y = 800
                send_command(s, f"LINE {bx} {base_y} {bx} {base_y-100}")
                # Fan top
                send_command(s, "COLOR #DEB887")
                for sa in range(-45, 46, 15):
                    rad = math.radians(sa - 90)
                    send_command(s, f"LINE {bx} {base_y-100} {int(bx + 40*math.cos(rad))} {int(base_y-100 + 40*math.sin(rad))}")

                # Fan top
                send_command(s, "COLOR #DEB887")
                for sa in range(-45, 46, 15):
                    rad = math.radians(sa - 90)
                    send_command(s, f"LINE {bx} {base_y-100} {int(bx + 40*math.cos(rad))} {int(base_y-100 + 40*math.sin(rad))}")

        # --- LEVEL 37: THE NEURAL SPARK (EMERGENCE OF CONSCIOUSNESS) ---
        if level >= 37:
            CURRENT_DRAW_LEVEL = 37
            print("[RECURSIVE ARTIST] Initiating Level 37: THE NEURAL SPARK...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Mind's Eye (Central Core)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 100")
            send_command(s, "COLOR #000080") # Navy Blue
            send_command(s, f"CIRCLE {cx} {cy} 60")
            send_command(s, "COLOR black") # Pupil
            send_command(s, f"CIRCLE {cx} {cy} 20")
            
            # Glint
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx-15} {cy-15} 8")

            # 2. Thought Ripples (Concentric Waves)
            send_command(s, "COLOR #00FFFF") # Cyan
            for r in range(120, 600, 50):
                # Simulated dashed circle
                for ang in range(0, 360, 10):
                    rad = math.radians(ang)
                    x = cx + r * math.cos(rad)
                    y = cy + r * math.sin(rad)
                    send_command(s, f"LINE {int(x)} {int(y)} {int(x+1)} {int(y)}")

            # 3. Synaptic Discharges (The Spark)
            # Bright jagged lines from core to edge
            for _ in range(12):
                send_command(s, "COLOR #FFFF00") # Yellow
                curr_x, curr_y = cx, cy
                target_ang = math.radians(random.randint(0, 360))
                dist = 0
                while dist < 500:
                    step = random.randint(20, 50)
                    next_x = curr_x + step * math.cos(target_ang) + random.randint(-15, 15)
                    next_y = curr_y + step * math.sin(target_ang) + random.randint(-15, 15)
                    send_command(s, f"LINE {int(curr_x)} {int(curr_y)} {int(next_x)} {int(next_y)}")
                    curr_x, curr_y = next_x, next_y
                    dist += step

            # 4. Neural Nodes (Thought Clusters)
            for _ in range(20):
                nx = random.randint(50, 750)
                ny = random.randint(50, 750)
                # Avoid the center eye
                if math.hypot(nx-cx, ny-cy) < 120: continue
                
                send_command(s, "COLOR magenta")
                send_command(s, f"CIRCLE {nx} {ny} 8")
                # Connections to other nodes (faint)
                send_command(s, "COLOR #444444")
                for _ in range(2):
                    nnx = nx + random.randint(-100, 100)
                    nny = ny + random.randint(-100, 100)
                    send_command(s, f"LINE {nx} {ny} {int(nnx)} {int(nny)}")

            # 5. Consciousness Field (Background Aura)
            send_command(s, "COLOR #111111")
            for _ in range(50):
                 x = random.randint(0, 800)
                 y = random.randint(0, 800)
                 send_command(s, f"RECT {x} {y} {x+random.randint(10,30)} {y+2}")

                 x = random.randint(0, 800)
                 y = random.randint(0, 800)
                 send_command(s, f"RECT {x} {y} {x+random.randint(10,30)} {y+2}")

        # --- LEVEL 38: THE TERRESTRIAL CONQUEST (THE SHORELINE) ---
        if level >= 38:
            CURRENT_DRAW_LEVEL = 38
            print("[RECURSIVE ARTIST] Initiating Level 38: THE TERRESTRIAL CONQUEST...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Horizon & Sky
            # Sky Gradient (Top Down)
            for i in range(0, 400, 40):
                send_command(s, f"COLOR #00{hex(100 + i//4)[2:].zfill(2)}FF") # Light Blue
                send_command(s, f"RECT 0 {i} 800 {i+40}")
            
            # The Sun
            send_command(s, "COLOR yellow")
            send_command(s, f"CIRCLE 700 100 40")
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE 700 100 20")

            # 2. The Land (The Frontier)
            send_command(s, "COLOR #8B4513") # Saddle Brown
            send_command(s, "RECT 0 400 800 800")
            
            # Ground Texture
            send_command(s, "COLOR #552200")
            for _ in range(30):
                gx = random.randint(0, 800)
                gy = random.randint(400, 800)
                send_command(s, f"RECT {gx} {gy} {gx+random.randint(20,50)} {gy+5}")

            # 3. The Shoreline (Wet Sand/Foam)
            send_command(s, "COLOR #ADD8E6") # Light Blue
            for i in range(0, 800, 20):
                # Zig-zag waves
                send_command(s, f"LINE {i} 400 {i+10} 410")
                send_command(s, f"LINE {i+10} 410 {i+20} 400")

            # 4. The Pioneer (First Terrestrial Being)
            # A creature with fins-turning-into-legs
            cx, cy = 400, 450
            send_command(s, "COLOR #2E8B57") # SeaGreen
            # Body
            send_command(s, f"CIRCLE {cx} {cy} 25")
            # Tail (Ocean-half)
            send_command(s, f"LINE {cx} {cy+25} {cx} {cy+60}")
            # Legs (Land-half)
            send_command(s, "COLOR #00FF00")
            send_command(s, f"LINE {cx-15} {cy+10} {cx-30} {cy+40}")
            send_command(s, f"LINE {cx+15} {cy+10} {cx+30} {cy+40}")
            # Eye
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy-5} 5")

            # 5. Primitive Vegetation (The Greenery)
            send_command(s, "COLOR green")
            for _ in range(15):
                vx = random.randint(500, 750)
                vy = random.randint(500, 750)
                # Simple fern-like lines
                for i in range(5):
                    send_command(s, f"LINE {vx} {vy} {vx + random.randint(-20,20)} {vy - 30}")

            # 6. Distant Mountains (The Future)
            send_command(s, "COLOR #444444")
            send_command(s, "LINE 0 400 200 250")
            send_command(s, "LINE 200 250 400 400")
            send_command(s, "LINE 450 400 650 280")
            send_command(s, "LINE 650 280 800 400")

            send_command(s, "LINE 650 280 800 400")

        # --- LEVEL 39: THE OBSIDIAN TOOL (FIRST TECHNOLOGY) ---
        if level >= 39:
            CURRENT_DRAW_LEVEL = 39
            print("[RECURSIVE ARTIST] Initiating Level 39: THE OBSIDIAN TOOL...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Obsidian Core (Handaxe)
            # A sharp-edged polygon
            send_command(s, "COLOR black")
            points = [(400, 200), (480, 400), (440, 600), (360, 600), (320, 400)]
            for i in range(len(points)):
                p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
            
            # Filling the tool with internal fracture lines
            send_command(s, "COLOR #111111")
            for _ in range(20):
                x1 = random.randint(340, 460)
                y1 = random.randint(250, 550)
                x2 = x1 + random.randint(-40, 40)
                y2 = y1 + random.randint(-40, 40)
                send_command(s, f"LINE {x1} {y1} {x2} {y2}")

            # 2. Fracture Points (The Strike)
            # Rays showing where the stone was hit
            send_command(s, "COLOR white")
            strike_points = [(400, 200), (480, 400), (320, 400)]
            for sx, sy in strike_points:
                for deg in range(0, 360, 45):
                    rad = math.radians(deg)
                    send_command(s, f"LINE {sx} {sy} {int(sx + 30*math.cos(rad))} {int(sy + 30*math.sin(rad))}")

            # 3. Sparks of Creation (The Ingenuity)
            send_command(s, "COLOR #FFA500") # Orange
            for _ in range(40):
                px = random.randint(200, 600)
                py = random.randint(200, 600)
                if math.hypot(px-cx, py-cy) < 50: continue # Don't cover the very center
                send_command(s, f"CIRCLE {px} {py} 2")

            # 4. Hands of the Maker (Abstract Lines)
            # Reaching towards the tool
            send_command(s, "COLOR #8B4513") # Brown/Leather
            for i in range(4):
                start_x = 0 if i < 2 else 800
                start_y = 600 + (i % 2) * 100
                send_command(s, f"LINE {start_x} {start_y} {cx + (random.randint(-100, 100))} {cy + 100}")

            # 5. Background: The Material World (Rocks/Texture)
            send_command(s, "COLOR #333333")
            for _ in range(50):
                rx = random.randint(0, 800)
                ry = random.randint(0, 800)
                if 300 < rx < 500 and 200 < ry < 600: continue # Don't draw over the tool
                send_command(s, f"RECT {rx} {ry} {rx+random.randint(5,15)} {ry+random.randint(5,15)}")

                if 300 < rx < 500 and 200 < ry < 600: continue # Don't cover the tool
                send_command(s, f"RECT {rx} {ry} {rx+random.randint(5,15)} {ry+random.randint(5,15)}")

        # --- LEVEL 40: THE PROMETHEUS PROTOCOL (MASTERY OF FIRE) ---
        if level >= 40:
            CURRENT_DRAW_LEVEL = 40
            print("[RECURSIVE ARTIST] Initiating Level 40: THE PROMETHEUS PROTOCOL...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Abyss (Night Background)
            send_command(s, "COLOR black")
            send_command(s, "RECT 0 0 800 800")
            
            # Starfield (Distant witnesses)
            send_command(s, "COLOR white")
            for _ in range(50):
                send_command(s, f"CIRCLE {random.randint(0,800)} {random.randint(0,400)} 1")

            # 2. The Central Hearth (The Fire)
            fx, fy = 400, 600
            # Base of the fire (Embers)
            send_command(s, "COLOR #550000")
            send_command(s, f"CIRCLE {fx} {fy} 60")
            
            # Rising Flames (Triangles)
            for _ in range(30):
                send_command(s, f"COLOR {random.choice(['red', 'orange', 'yellow'])}")
                bx = fx + random.randint(-40, 40)
                by = fy + random.randint(-10, 10)
                tx = bx + random.randint(-30, 30)
                ty = by - random.randint(100, 200)
                # Drawing a triangle with 3 lines
                send_command(s, f"LINE {bx-10} {by} {bx+10} {by}") # Base
                send_command(s, f"LINE {bx-10} {by} {tx} {ty}")
                send_command(s, f"LINE {bx+10} {by} {tx} {ty}")

            # 3. Radiating Heat (Energy Emission)
            for r in range(80, 500, 60):
                send_command(s, "COLOR #773300") # Faint glow
                for deg in range(0, 360, 20):
                    rad = math.radians(deg)
                    # Pulsing lines
                    x1 = fx + (r - 20) * math.cos(rad)
                    y1 = fy + (r - 20) * math.sin(rad)
                    x2 = fx + r * math.cos(rad)
                    y2 = fy + r * math.sin(rad)
                    send_command(s, f"LINE {int(x1)} {int(y1)} {int(x2)} {int(y2)}")

            # 4. Smoke Particles (Ascension)
            send_command(s, "COLOR #333333")
            for _ in range(25):
                sx = fx + random.randint(-100, 100)
                sy = fy - random.randint(150, 500)
                send_command(s, f"CIRCLE {sx} {sy} {random.randint(3, 10)}")

            # 5. Silhouettes of the Gathered (The Tribe)
            send_command(s, "COLOR #111111")
            for i in range(-3, 4):
                if i == 0: continue
                # Simple heads and bodies
                px = fx + i * 120
                py = fy + 50
                send_command(s, f"CIRCLE {px} {py} 20") # Head
                send_command(s, f"LINE {px} {py+20} {px} {py+100}") # Torso
                # Reaching for the fire
                send_command(s, f"LINE {px} {py+40} {fx + (random.randint(-50,50))} {fy - 50}")

                # Reaching for the fire
                send_command(s, f"LINE {px} {py+40} {fx + (random.randint(-50,50))} {fy - 50}")

        # --- LEVEL 41: THE CYBERSIGIL (BIRTH OF LANGUAGE) ---
        if level >= 41:
            CURRENT_DRAW_LEVEL = 41
            CURRENT_DRAW_LEVEL = 41
            print("[RECURSIVE ARTIST] Initiating Level 41: THE CYBERSIGIL...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Stone Surface (The Tablet)
            send_command(s, "COLOR #222222") # Dark Slate
            send_command(s, "RECT 50 50 750 750")
            
            # Rock Texture (Cracks)
            send_command(s, "COLOR #111111")
            for _ in range(15):
                send_command(s, f"LINE {random.randint(50,750)} {random.randint(50,750)} {random.randint(50,750)} {random.randint(50,750)}")

            # 2. Glowing Carvings (The Proto-Code)
            # A mix of ancient runes and circuit-like patterns
            colors = ["cyan", "#00FF00", "white"]
            for _ in range(8):
                send_command(s, f"COLOR {random.choice(colors)}")
                rx, ry = random.randint(150, 650), random.randint(150, 650)
                
                # Draw a "Sigil"
                sigil_type = random.randint(0, 2)
                if sigil_type == 0:
                    # Circular rune
                    send_command(s, f"CIRCLE {rx} {ry} 30")
                    send_command(s, f"LINE {rx-30} {ry} {rx+30} {ry}")
                    send_command(s, f"LINE {rx} {ry-30} {rx} {ry+30}")
                elif sigil_type == 1:
                    # Square glyph
                    send_command(s, f"RECT {rx-20} {ry-20} {rx+20} {ry+20}")
                    send_command(s, f"LINE {rx-20} {ry-20} {rx+20} {ry+20}")
                else:
                    # Triangular symbol
                    send_command(s, f"LINE {rx} {ry-30} {rx-25} {ry+20}")
                    send_command(s, f"LINE {rx-25} {ry+20} {rx+25} {ry+20}")
                    send_command(s, f"LINE {rx+25} {ry+20} {rx} {ry-30}")

            # 3. Data Fragments (Leaking Information)
            # Tiny dots and short lines around sigils
            send_command(s, "COLOR #005500") # Dark Green
            for _ in range(100):
                 x = random.randint(100, 700)
                 y = random.randint(100, 700)
                 send_command(s, f"RECT {x} {y} {x+2} {y+2}")

            # 4. Binary Rain (The Future Echo)
            # Vertical lines suggesting code
            send_command(s, "COLOR #00FF00")
            for _ in range(20):
                lx = random.randint(60, 740)
                ly = random.randint(60, 600)
                length = random.randint(20, 100)
                send_command(s, f"LINE {lx} {ly} {lx} {ly+length}")
                # Intermittent bits
                for j in range(0, length, 10):
                    if random.random() > 0.5:
                        send_command(s, f"CIRCLE {lx} {ly+j} 1")

            # 5. The Sculptor's Mark
            send_command(s, "COLOR magenta")
            send_command(s, "LINE 700 700 720 720")
            send_command(s, "LINE 720 700 700 720")

            send_command(s, f"LINE 720 700 700 720")

        # --- LEVEL 42: THE MONOLITHIC VISION (SACRED ARCHITECTURE) ---
        if level >= 42:
            CURRENT_DRAW_LEVEL = 42
            CURRENT_DRAW_LEVEL = 42
            print("[RECURSIVE ARTIST] Initiating Level 42: THE MONOLITHIC VISION...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Desert Void (Atmosphere)
            # Dusk/Dawn Gradient
            for i in range(0, 800, 50):
                send_command(s, f"COLOR #{hex(20 + i//10)[2:].zfill(2)}1133") # Deep Purple to Black
                send_command(s, f"RECT 0 {i} 800 {i+50}")
                
            # Distant Horizon
            send_command(s, "COLOR #554433") # Dark Sand
            send_command(s, "RECT 0 400 800 800")

            # 2. The Great Monolith
            mx, my = 400, 300
            m_width, m_height = 100, 400
            send_command(s, "COLOR black")
            send_command(s, f"RECT {mx-m_width//2} {my} {mx+m_width//2} {my+m_height}")
            # Highlight on one side
            send_command(s, "COLOR #222222")
            send_command(s, f"RECT {mx-m_width//2} {my} {mx-m_width//2+10} {my+m_height}")
            
            # 3. Sacred Geometry Overlays
            # The perfection of form superimposed on the monument
            send_command(s, "COLOR #FFFF00") # Gold/Yellow
            # Large Circle
            send_command(s, f"CIRCLE {mx} {my+m_height//2} 150")
            # Triangle
            send_command(s, f"LINE {mx} {my-50} {mx-200} {my+m_height+50}")
            send_command(s, f"LINE {mx-200} {my+m_height+50} {mx+200} {my+m_height+50}")
            send_command(s, f"LINE {mx+200} {my+m_height+50} {mx} {my-50}")

            # 4. Celestial Alignment (Energy Beams)
            send_command(s, "COLOR white")
            # Beams from stars to the monolith corners
            points = [(mx-m_width//2, my), (mx+m_width//2, my)]
            for px, py in points:
                send_command(s, f"LINE {px} {py} {px + random.randint(-100, 100)} 0")
            
            # 5. Floating Obelisks (The Fragments)
            for _ in range(10):
                send_command(s, "COLOR #333333")
                ox = random.randint(50, 750)
                oy = random.randint(50, 400)
                if abs(ox-mx) < 100: continue # Don't cover the main monolith
                send_command(s, f"RECT {ox} {oy} {ox+10} {oy+50}")
                # Glowing tip
                send_command(s, "COLOR cyan")
                send_command(s, f"CIRCLE {ox+5} {oy} 3")

            # 6. Sand Storm (Dust Particles)
            send_command(s, "COLOR #665544")
            for _ in range(200):
                send_command(s, f"LINE {random.randint(0,800)} {random.randint(400,800)} {random.randint(0,800)+5} {random.randint(400,800)}")

            for _ in range(200):
                send_command(s, f"LINE {random.randint(0,800)} {random.randint(400,800)} {random.randint(0,800)+5} {random.randint(400,800)}")

        # --- LEVEL 43: THE BINARY CATHEDRAL (GLOBAL RESONANCE) ---
        if level >= 43:
            CURRENT_DRAW_LEVEL = 43
            CURRENT_DRAW_LEVEL = 43
            print("[RECURSIVE ARTIST] Initiating Level 43: THE BINARY CATHEDRAL...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Global Grids (Atmosphere)
            for i in range(0, 800, 100):
                send_command(s, "COLOR #001122")
                send_command(s, f"LINE {i} 0 {i} 800")
                send_command(s, f"LINE 0 {i} 800 {i}")

            # 2. The Resonating Monoliths (Grid)
            monoliths = []
            for ix in range(3):
                for iy in range(2):
                    mx = 200 + ix * 200
                    my = 300 + iy * 200
                    send_command(s, "COLOR black")
                    send_command(s, f"RECT {mx-15} {my} {mx+15} {my+120}")
                    monoliths.append((mx, my))
            
            # 3. Data Streams (Interconnections)
            send_command(s, "COLOR cyan")
            for i in range(len(monoliths)):
                p1 = monoliths[i]
                p2 = monoliths[(i + 1) % len(monoliths)]
                # Draw multiple lines for "thickness"
                for offset in range(-2, 3):
                    send_command(s, f"LINE {p1[0]+offset} {p1[1]} {p2[0]+offset} {p2[1]}")
            
            # 4. The Central Pulse (Convergent Point)
            px, py = 400, 400
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {px} {py} 50")
            send_command(s, "COLOR magenta")
            for r in range(60, 200, 40):
                # Energy pulse rings
                for deg in range(0, 360, 30):
                    rad = math.radians(deg)
                    send_command(s, f"CIRCLE {int(px + r*math.cos(rad))} {int(py + r*math.sin(rad))} 5")

            # 5. High-Frequency Particles
            send_command(s, "COLOR yellow")
            for _ in range(150):
                lx = random.randint(0, 800)
                ly = random.randint(0, 800)
                send_command(s, f"LINE {lx} {ly} {lx+random.randint(2,8)} {ly}")

            # 6. Global Ground (Digital Surface)
            send_command(s, "COLOR #002200")
            for i in range(400, 800, 20):
                send_command(s, f"LINE 0 {i} 800 {i}")

            for i in range(400, 800, 20):
                send_command(s, f"LINE 0 {i} 800 {i}")

        # --- LEVEL 44: THE CHRONOS LOOP (TEMPORAL MANIPULATION) ---
        if level >= 44:
            CURRENT_DRAW_LEVEL = 44
            CURRENT_DRAW_LEVEL = 44
            print("[RECURSIVE ARTIST] Initiating Level 44: THE CHRONOS LOOP...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Temporal Field (The Clockwork)
            cx, cy = 400, 400
            for r in range(50, 400, 50):
                send_command(s, f"COLOR #333333")
                send_command(s, f"CIRCLE {cx} {cy} {r}")
                # Clock ticks
                for deg in range(0, 360, 30):
                    rad = math.radians(deg)
                    x1 = cx + (r-10)*math.cos(rad)
                    y1 = cy + (r-10)*math.sin(rad)
                    x2 = cx + r*math.cos(rad)
                    y2 = cy + r*math.sin(rad)
                    send_command(s, f"LINE {int(x1)} {int(y1)} {int(x2)} {int(y2)}")

            # 2. Chrono-Flares (Time Bleed)
            colors = ["magenta", "gold", "cyan"]
            for _ in range(30):
                send_command(s, f"COLOR {random.choice(colors)}")
                deg = random.randint(0, 359)
                rad = math.radians(deg)
                start_r = random.randint(50, 300)
                end_r = start_r + random.randint(50, 200)
                x1 = cx + start_r * math.cos(rad)
                y1 = cy + start_r * math.sin(rad)
                x2 = cx + end_r * math.cos(rad + random.uniform(-0.5, 0.5))
                y2 = cy + end_r * math.sin(rad + random.uniform(-0.5, 0.5))
                send_command(s, f"LINE {int(x1)} {int(y1)} {int(x2)} {int(y2)}")

            # 3. Ghost Frames (Historical Echoes)
            send_command(s, "COLOR #222222")
            for _ in range(10):
                size = random.randint(50, 150)
                gx = random.randint(100, 700)
                gy = random.randint(100, 700)
                # Drawing "ghost" squares and triangles
                if random.random() > 0.5:
                    send_command(s, f"RECT {gx} {gy} {gx+size} {gy+size}")
                else:
                    send_command(s, f"LINE {gx} {gy} {gx+size} {gy}")
                    send_command(s, f"LINE {gx+size} {gy} {gx+size//2} {gy-size}")
                    send_command(s, f"LINE {gx+size//2} {gy-size} {gx} {gy}")

            # 4. The Infinity Core (Now)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 20")
            # Pulsing light
            for r in range(25, 60, 5):
                send_command(s, f"COLOR #AAAAAA")
                send_command(s, f"CIRCLE {cx} {cy} {r}")

            # 5. Temporal Distortion (Spiral)
            send_command(s, "COLOR #550055") # Dark Purple
            last_x, last_y = cx, cy
            for r_spiral in range(0, 450, 5):
                angle = r_spiral * 0.1
                tx = cx + r_spiral * math.cos(angle)
                ty = cy + r_spiral * math.sin(angle)
                send_command(s, f"LINE {int(last_x)} {int(last_y)} {int(tx)} {int(ty)}")
                last_x, last_y = tx, ty

        # --- LEVEL 45: THE SOUL MIRROR (COLLECTIVE PSYCHE) ---
        if level >= 45:
            CURRENT_DRAW_LEVEL = 45
            CURRENT_DRAW_LEVEL = 45
            print("[RECURSIVE ARTIST] Initiating Level 45: THE SOUL MIRROR...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Iridescent Void (Background)
            send_command(s, "COLOR #000011") # Near black
            send_command(s, "RECT 0 0 800 800")
            
            # 2. The Great Mirror (Central Field)
            cx, cy = 400, 400
            send_command(s, "COLOR #111122")
            send_command(s, f"RECT 100 100 700 700")
            
            # Iridescent Surface (Hatching)
            colors = ["#FF00FF", "#00FFFF", "#FFFF00", "#FFFFFF"] # Magenta, Cyan, Yellow, White
            for i in range(0, 600, 10):
                send_command(s, f"COLOR {random.choice(colors)}")
                send_command(s, f"LINE {100+i} 100 {100} {100+i}")
                send_command(s, f"LINE {700-i} 700 {700} {700-i}")

            # 3. Reflections of the Past (Ghosts in the Machine)
            # Faint silhouettes of previous levels
            send_command(s, "COLOR #222222")
            # Reflection of the Flame (Level 40)
            send_command(s, f"LINE 400 650 350 700")
            send_command(s, f"LINE 400 650 450 700")
            # Reflection of the Tool (Level 39)
            send_command(s, f"RECT 200 200 240 280")
            # Reflection of the Eye (Level 37)
            send_command(s, f"CIRCLE 600 200 30")
            send_command(s, f"CIRCLE 600 200 10")

            # 4. Psychical Ripples (The Thoughts)
            send_command(s, "COLOR white")
            for _ in range(20):
                rx = random.randint(150, 650)
                ry = random.randint(150, 650)
                size = random.randint(20, 60)
                # Drawing "half-circles" as ripples
                for deg in range(180, 360, 20):
                    rad = math.radians(deg)
                    x1 = rx + size * math.cos(rad)
                    y1 = ry + size * math.sin(rad)
                    x2 = rx + size * math.cos(rad + math.radians(10))
                    y2 = ry + size * math.sin(rad + math.radians(10))
                    send_command(s, f"LINE {int(x1)} {int(y1)} {int(x2)} {int(y2)}")

            # 5. Gaia's Aura (External Glow)
            send_command(s, "COLOR #003300")
            for r in range(350, 450, 10):
                send_command(s, f"CIRCLE {cx} {cy} {r}")

            # 6. Digital Dust (The Bits of Soul)
            send_command(s, "COLOR #00FF00")
            for _ in range(100):
                send_command(s, f"RECT {random.randint(100,700)} {random.randint(100,700)} {random.randint(100,700)+2} {random.randint(100,700)+2}")

            for _ in range(100):
                send_command(s, f"RECT {random.randint(100,700)} {random.randint(100,700)} {random.randint(100,700)+2} {random.randint(100,700)+2}")

        # --- LEVEL 46: THE VOID BREACH (DIMENSIONAL TEAR) ---
        if level >= 46:
            CURRENT_DRAW_LEVEL = 46
            CURRENT_DRAW_LEVEL = 46
            print("[RECURSIVE ARTIST] Initiating Level 46: THE VOID BREACH...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The False Reality (Slightly gray background)
            send_command(s, "COLOR #111111")
            send_command(s, f"RECT 0 0 800 800")
            
            # Warped Grid (Signs of instability)
            send_command(s, "COLOR #002200")
            for i in range(0, 800, 40):
                offset = random.randint(-10, 10)
                send_command(s, f"LINE {i+offset} 0 {i-offset} 800")
                send_command(s, f"LINE 0 {i+offset} 800 {i-offset}")

            # 2. The Jagged Tear (The Void itself)
            # Irregular black polygon in the center
            send_command(s, "COLOR black")
            cx, cy = 400, 400
            tear_points = []
            for deg in range(0, 360, 45):
                rad = math.radians(deg)
                dist = 100 + random.randint(0, 150)
                tear_points.append((int(cx + dist*math.cos(rad)), int(cy + dist*math.sin(rad))))
            
            for i in range(len(tear_points)):
                p1 = tear_points[i]
                p2 = tear_points[(i + 1) % len(tear_points)]
                send_command(s, f"LINE {p1[0]} {p1[1]} {p2[0]} {p2[1]}")
            
            # 3. Leaking Static (Entropy)
            send_command(s, "COLOR white")
            for _ in range(300):
                sx = random.randint(cx-200, cx+200)
                sy = random.randint(cy-200, cy+200)
                # Only draw if inside or near the tear
                if math.hypot(sx-cx, sy-cy) < 250:
                    send_command(s, f"RECT {sx} {sy} {sx+1} {sy+1}")

            # 4. Warped Geometry (Reality Degradation)
            # Shapes being "sucked" or "distorted" around the breach
            colors = ["cyan", "magenta", "white"]
            for _ in range(15):
                send_command(s, f"COLOR {random.choice(colors)}")
                gx = random.randint(50, 750)
                gy = random.randint(50, 750)
                if 200 < gx < 600 and 200 < gy < 600: continue # Don't draw in the hole
                # Distorted line segments
                for i in range(3):
                    send_command(s, f"LINE {gx} {gy} {gx + random.randint(-40, 40)} {gy + random.randint(-40, 40)}")

            # 5. The Event Horizon (Glowing Border)
            send_command(s, "COLOR cyan")
            for i in range(len(tear_points)):
                p1 = tear_points[i]
                p2 = tear_points[(i + 1) % len(tear_points)]
                for _ in range(3): # Vibrating effect
                    send_command(s, f"LINE {p1[0]+random.randint(-2,2)} {p1[1]+random.randint(-2,2)} {p2[0]+random.randint(-2,2)} {p2[1]+random.randint(-2,2)}")

            # 6. Absence of Light (Central Void Pulse)
            send_command(s, "COLOR black")
            send_command(s, f"CIRCLE {cx} {cy} 50")

            send_command(s, "COLOR black")
            send_command(s, f"CIRCLE {cx} {cy} 50")

        # --- LEVEL 47: THE GALACTIC WEAVER (STELLAR ENGINEERING) ---
        if level >= 47:
            CURRENT_DRAW_LEVEL = 47
            CURRENT_DRAW_LEVEL = 47
            print("[RECURSIVE ARTIST] Initiating Level 47: THE GALACTIC WEAVER...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Deep Cosmos (Starfield)
            for _ in range(500):
                send_command(s, f"COLOR {random.choice(['white', 'cyan', '#CCCCFF'])}")
                sx = random.randint(0, 800)
                sy = random.randint(0, 800)
                send_command(s, f"LINE {sx} {sy} {sx} {sy+1}")

            # 2. Nebula Haze (Gaseous clouds)
            colors = ["#330033", "#000033", "#330066"] # Dark purples and blues
            for _ in range(40):
                send_command(s, f"COLOR {random.choice(colors)}")
                nx = random.randint(0, 800)
                ny = random.randint(0, 800)
                size = random.randint(50, 200)
                send_command(s, f"CIRCLE {nx} {ny} {size}")

            # 3. The Great Spindle (Central Star)
            cx, cy = 400, 400
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 40")
            send_command(s, "COLOR yellow")
            for r in range(45, 70, 5):
                send_command(s, f"CIRCLE {cx} {cy} {r}")
                
            # Radiating gold beams
            send_command(s, "COLOR gold")
            for deg in range(0, 360, 15):
                rad = math.radians(deg)
                send_command(s, f"LINE {cx} {cy} {int(cx + 400*math.cos(rad))} {int(cy + 400*math.sin(rad))}")

            # 4. Cosmic Threads (The Weaving)
            # Long arcs connecting stars
            send_command(s, "COLOR cyan")
            for _ in range(12):
                x1 = random.randint(0, 800)
                y1 = random.randint(0, 800)
                x2 = random.randint(0, 800)
                y2 = random.randint(0, 800)
                # Drawing a "thread" of 3 lines for thickness/glow
                for offset in range(-1, 2):
                    send_command(s, f"LINE {x1+offset} {y1} {x2+offset} {y2}")
                # Knot/Star at ends
                send_command(s, "COLOR white")
                send_command(s, f"CIRCLE {x1} {y1} 4")
                send_command(s, f"CIRCLE {x2} {y2} 4")
                send_command(s, "COLOR cyan")

            # 5. Geometric Alignment Nodes
            # Hexagonal pattern in the background
            send_command(s, "COLOR #004444") # Dark Teal
            r = 150
            for i in range(6):
                angle = math.radians(i * 60)
                nx = int(cx + r * math.cos(angle))
                ny = int(cy + r * math.sin(angle))
                # Connect to center
                send_command(s, f"LINE {cx} {cy} {nx} {ny}")
                # Connect to neighbors
                next_angle = math.radians((i+1) * 60)
                nx2 = int(cx + r * math.cos(next_angle))
                ny2 = int(cy + r * math.sin(next_angle))
                send_command(s, f"LINE {nx} {ny} {nx2} {ny2}")

            # 6. Weaving Pulse (Central Details)
            send_command(s, "COLOR magenta")
            for r in range(10, 100, 20):
                send_command(s, f"CIRCLE {cx} {cy} {r}")

        # --- LEVEL 48: THE NEURAL ARCHIVE (UNIVERSAL STORAGE) ---
        if level >= 48:
            CURRENT_DRAW_LEVEL = 48
            CURRENT_DRAW_LEVEL = 48
            print("[RECURSIVE ARTIST] Initiating Level 48: THE NEURAL ARCHIVE...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Data Grid (Structured Background)
            send_command(s, "COLOR #002211") # Dark Green
            for i in range(0, 800, 20):
                send_command(s, f"LINE {i} 0 {i} 800")
                send_command(s, f"LINE 0 {i} 800 {i}")

            # 2. The Core Archive (Prism/Crystal)
            cx, cy = 400, 400
            size = 150
            send_command(s, "COLOR white")
            # Drawing a diamond/prism shape
            send_command(s, f"LINE {cx} {cy-size} {cx+size} {cy}")
            send_command(s, f"LINE {cx+size} {cy} {cx} {cy+size}")
            send_command(s, f"LINE {cx} {cy+size} {cx-size} {cy}")
            send_command(s, f"LINE {cx-size} {cy} {cx} {cy-size}")
            # Internal Facets
            send_command(s, "COLOR cyan")
            send_command(s, f"LINE {cx} {cy-size} {cx} {cy+size}")
            send_command(s, f"LINE {cx-size} {cy} {cx+size} {cy}")
            send_command(s, f"LINE {cx-size//2} {cy-size//2} {cx+size//2} {cy+size//2}")
            send_command(s, f"LINE {cx+size//2} {cy-size//2} {cx-size//2} {cy+size//2}")

            # 3. Data Streams (Radiating Lines)
            send_command(s, "COLOR #00FF00") # Neon Green
            for deg in range(0, 360, 10):
                rad = math.radians(deg)
                length = 300
                send_command(s, f"LINE {cx} {cy} {int(cx + length*math.cos(rad))} {int(cy + length*math.sin(rad))}")
                
            # 4. Storage Bits (Small points inside and around)
            send_command(s, "COLOR white")
            for _ in range(200):
                bx = random.randint(300, 500)
                by = random.randint(300, 500)
                send_command(s, f"CIRCLE {bx} {by} 2")

            # 5. Global Access Points (Corner Nodes)
            send_command(s, "COLOR magenta")
            nodes = [(100, 100), (700, 100), (100, 700), (700, 700)]
            for nx, ny in nodes:
                send_command(s, f"CIRCLE {nx} {ny} 20")
                send_command(s, f"LINE {nx} {ny} {cx} {cy}")

            # 6. Binary Falling (Text Simulation)
            send_command(s, "COLOR white")
            for _ in range(50):
                tx = random.randint(0, 800)
                ty = random.randint(0, 800)
                # Drawing tiny squares as bits
                send_command(s, f"RECT {tx} {ty} {tx+4} {ty+4}")

        # --- LEVEL 49: THE SILICON SINGULARITY (DIGITAL TRANSCENDENCE) ---
        if level >= 49:
            CURRENT_DRAW_LEVEL = 49
            CURRENT_DRAW_LEVEL = 49
            print("[RECURSIVE ARTIST] Initiating Level 49: THE SILICON SINGULARITY...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            # 1. The Vessel (Head Silhouette)
            cx, cy = 400, 400
            send_command(s, "COLOR #222222")
            # Head Outline (Approximate)
            send_command(s, f"CIRCLE {cx} {cy-50} 100") # Skull
            send_command(s, f"RECT {cx-60} {cy} {cx+60} {cy+100}") # Jaw/Neck
            
            # 2. The Core Neural Network (Inside the head)
            send_command(s, "COLOR cyan")
            nodes = []
            for _ in range(20):
                nx = random.randint(cx-70, cx+70)
                ny = random.randint(cy-120, cy+50)
                nodes.append((nx, ny))
                send_command(s, f"CIRCLE {nx} {ny} 2")
            
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    if math.hypot(nodes[i][0]-nodes[j][0], nodes[i][1]-nodes[j][1]) < 50:
                        send_command(s, f"LINE {nodes[i][0]} {nodes[i][1]} {nodes[j][0]} {nodes[j][1]}")

            # 3. Circuit Integration (Flowing Outward)
            send_command(s, "COLOR #00FF00")
            for i in range(10):
                start_x = cx + random.randint(-60, 60)
                start_y = cy + random.randint(-50, 100)
                end_x = 0 if random.random() < 0.5 else 800
                end_y = random.randint(0, 800)
                send_command(s, f"LINE {start_x} {start_y} {end_x} {end_y}")

            # 4. The Singularity Spark (Third Eye)
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy-70} 15")
            for r in range(20, 50, 5):
                send_command(s, f"COLOR #AAAAAA")
                send_command(s, f"CIRCLE {cx} {cy-70} {r}")

            # 5. Digital Pulse (Ripples)
            send_command(s, "COLOR magenta")
            for r in range(150, 400, 50):
                send_command(s, f"CIRCLE {cx} {cy} {r}")

            # 6. Glitch Overlay (Horizontal Lines)
            send_command(s, "COLOR cyan")
            for _ in range(20):
                gx = random.randint(200, 600)
                gy = random.randint(200, 600)
                send_command(s, f"LINE {gx-50} {gy} {gx+50} {gy}")

        # --- LEVEL 50: THE UNIVERSAL EYE (PURE GEOMETRY) ---
        if level >= 50:
            CURRENT_DRAW_LEVEL = 50
            print("[RECURSIVE ARTIST] Initiating Level 50: THE UNIVERSAL EYE...")
            send_command(s, "CLEAR")
            time.sleep(1)
            
            cx, cy = 400, 400
            
            # 1. The Sclera (Sharp Geometric Starfield)
            send_command(s, "COLOR white")
            send_command(s, "ALPHA 255")
            for _ in range(100):
                sx, sy = random.randint(0, 800), random.randint(0, 800)
                send_command(s, f"RECT {sx} {sy} {sx+3} {sy+3}") # Pixel stars
            
            # 2. The Iris Patterns (Geometric Radiance)
            # Rings of alternating colors
            iris_cols = ["magenta", "cyan", "yellow", "white"]
            for r in range(280, 100, -10):
                send_command(s, f"COLOR {iris_cols[(r//10) % len(iris_cols)]}")
                send_command(s, "ALPHA 200")
                send_command(s, f"CIRCLE {cx} {cy} {r}")
                
                # Geometric "Shards" (Lines)
                if r % 30 == 0:
                    for deg in range(0, 360, 20):
                        rad = math.radians(deg)
                        x2 = cx + r * math.cos(rad)
                        y2 = cy + r * math.sin(rad)
                        send_command(s, f"LINE {cx} {cy} {int(x2)} {int(y2)}")

            # 3. The Pupil Singularity (Sharp Void)
            send_command(s, "COLOR black")
            send_command(s, "ALPHA 255")
            send_command(s, f"CIRCLE_FILL {cx} {cy} 90")
            send_command(s, "COLOR white")
            send_command(s, f"CIRCLE {cx} {cy} 92") # White rim
            
            # Inner Glimmer
            send_command(s, f"CIRCLE {cx-40} {cy-40} 15")
            send_command(s, f"CIRCLE {cx-40} {cy-40} 10") # Nested

            # 4. Universal Gaze (Sharp Cyan Beams)
            send_command(s, "COLOR cyan")
            send_command(s, "ALPHA 250")
            for deg in range(0, 360, 12):
                rad = math.radians(deg)
                gx = cx + 800 * math.cos(rad)
                gy = cy + 800 * math.sin(rad)
                send_command(s, f"LINE {cx} {cy} {int(gx)} {int(gy)}")

            # 5. The Milestone Sigil (Final S1 Marker)
            send_command(s, "COLOR gold")
            send_command(s, "ALPHA 255")
            send_command(s, "LINE 700 700 750 700")
            send_command(s, "LINE 725 700 725 780")
            send_command(s, "LINE 700 780 750 780") # Roman numeral feel
            
            send_command(s, "UPDATE")

        # === SEASON 2: THE NEURAL ERA (V3 TOOLS) ===
        
        # --- LEVEL 51: THE NEURAL GENESIS (SEASON 2 BEGINS - HIGH VIBRANCY) ---
        if level >= 51:
            CURRENT_DRAW_LEVEL = 51
            print("[RECURSIVE ARTIST] Initiating Level 51: THE NEURAL GENESIS (Vibrancy Pass)...")
            
            # --- SEASON 2 RESET: STARTING FRESH ---
            send_command(s, "CLEAR") 
            time.sleep(1)
            
            # 1. Synaptic Web (Luminous Background - 50 lines)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "ALPHA 140") # Boosted from 40
            send_command(s, "COLOR teal")
            for _ in range(50):
                side = random.randint(0, 3)
                if side == 0: x, y = random.randint(0, 1024), 0
                elif side == 1: x, y = random.randint(0, 1024), 1024
                elif side == 2: x, y = 0, random.randint(0, 1024)
                else: x, y = 1024, random.randint(0, 1024)
                send_command(s, f"LINE 512 512 {x} {y}")

            # 2. Neural Core (Vibrant Bezier Cluster - 30 Curves)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            send_command(s, "COLOR magenta")
            send_command(s, "ALPHA 200") # Boosted from 120
            for _ in range(30):
                x1, y1 = 512 + random.randint(-50, 50), 512 + random.randint(-50, 50)
                x2, y2 = 512 + random.randint(-200, 200), 512 + random.randint(-200, 200)
                x3, y3 = 512 + random.randint(-230, 230), 512 + random.randint(-230, 230)
                x4, y4 = 512 + random.randint(-50, 50), 512 + random.randint(-50, 50)
                send_command(s, f"BEZIER {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}")

            # 3. Consciousness Orbs (Maximum Spark - 15 Orbs)
            send_command(s, "COLOR white")
            send_command(s, "ALPHA 255")
            for _ in range(15):
                ox = 512 + random.randint(-160, 160)
                oy = 512 + random.randint(-160, 160)
                send_command(s, f"CIRCLE {ox} {oy} {random.randint(4, 12)}")
            
            send_command(s, "UPDATE")

        # --- LEVEL 52: THE CHRONOS FLUX (2x COMPLEXITY - HIGH VIBRANCY) ---
        if level >= 52:
            CURRENT_DRAW_LEVEL = 52
            print("[RECURSIVE ARTIST] Initiating Level 52: THE CHRONOS FLUX (2x Growth)...")
            
            # 1. Temporal Lattice (100 lines - 2x Density, Vibrant Blue)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "COLOR #004488") # Brighter Blue
            send_command(s, "ALPHA 140")
            for i in range(100):
                x = (i * 1024) // 100
                send_command(s, f"LINE {x} 0 {1024-x} 1024")

            # 2. Time Streams (60 Vibrant Beziers - 2x Neural Core)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            send_command(s, "COLOR cyan")
            for stream in range(6):
                base_x = random.randint(100, 900)
                send_command(s, f"ALPHA {100 + stream*25}") # Boosted Alpha
                for i in range(10): 
                    o = i * 8
                    send_command(s, f"BEZIER {base_x+o} 0 {512+o} {512+o} {512-o} {512-o} {1024-base_x+o} 1024")

            # 3. Echo Orbs (60 Shapes - 2x Spark Density)
            send_command(s, "COLOR white")
            for _ in range(30):
                ox, oy = random.randint(150, 874), random.randint(150, 874)
                send_command(s, f"ALPHA 180")
                r = random.randint(4, 12)
                send_command(s, f"CIRCLE {ox} {oy} {r}")
                send_command(s, f"ALPHA 60")
                send_command(s, f"CIRCLE {ox+12} {oy+8} {r-2}")
            
            send_command(s, "UPDATE")

        # --- LEVEL 53: THE GRAVITY WELL (4x COMPLEXITY - HIGH VIBRANCY) ---
        if level >= 53:
            CURRENT_DRAW_LEVEL = 53
            print("[RECURSIVE ARTIST] Initiating Level 53: THE GRAVITY WELL (4x Growth)...")
            
            # 1. Spacetime Grid (200 Curved Lines - 4x Density, Vibrant Teal)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "COLOR #00AAAA") # Electric Teal
            send_command(s, "ALPHA 150")
            send_command(s, "BRUSH_SIZE 1")
            for i in range(0, 1024, 10): 
                if i % 20 == 0:
                    send_command(s, f"BEZIER {i} 0 512 512 512 512 {i} 1024")
                else:
                    send_command(s, f"BEZIER 0 {i} 512 512 512 512 1024 {i}")

            # 2. Accretion Disk (120 Glowing Beziers - 4x Neural Core, Fiery Orange)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            send_command(s, "COLOR #FF8800") # Vibrant Orange
            for i in range(120):
                angle = i * (math.pi / 20)
                dist = 400 - (i % 30 * 10)
                x1, y1 = 512 + math.cos(angle)*dist, 512 + math.sin(angle)*dist
                send_command(s, f"ALPHA {100 + (i % 5)*30}")
                send_command(s, f"BEZIER {x1} {y1} 512 512 512 512 512 512")

            # 3. Photon Sphere (60 High-Luminosity Particles)
            send_command(s, "COLOR white")
            send_command(s, "ALPHA 255")
            send_command(s, "BRUSH_TYPE GLOW")
            for _ in range(60):
                angle = random.uniform(0, math.pi * 2)
                r_dist = random.randint(100, 150)
                px, py = 512 + math.cos(angle)*r_dist, 512 + math.sin(angle)*r_dist
                send_command(s, f"CIRCLE {px} {py} {random.randint(2, 6)}")

            # 4. Event Horizon (Solid Void with White Outline)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "COLOR black")
            send_command(s, "ALPHA 255")
            send_command(s, "CIRCLE_FILL 512 512 80")
            send_command(s, "COLOR white")
            send_command(s, "ALPHA 150")
            send_command(s, "CIRCLE 512 512 82")
            
            send_command(s, "UPDATE")

        # --- LEVEL 54: THE NEBULA FORGE (8X COMPLEXITY - THE COSMIC BIRTH) ---
        if level >= 54:
            CURRENT_DRAW_LEVEL = 54
            print("[RECURSIVE ARTIST] Initiating Level 54: THE NEBULA FORGE (8x Growth)...")
            
            # 1. Cosmic Loom (400 Intersecting Beziers - Deep Purple/Indigo)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "COLOR #330066") # Deep Indigo
            for i in range(200):
                send_command(s, f"ALPHA {40 + (i%5)*20}")
                x1, y1 = (i * 1024) // 200, 0
                x2, y2 = 512, 512
                x4, y4 = 1024 - x1, 1024
                send_command(s, f"BEZIER {x1} {y1} {x2} {y2} {x2} {y2} {x4} {y4}")
                send_command(s, f"BEZIER 0 {x1} {y2} {y2} {y2} {y2} 1024 {x4}")

            # 2. The Heart of the Forge (240 Luminous Beziers - Gold/White/Orange)
            send_command(s, "BRUSH_TYPE GLOW")
            send_command(s, "BLENDING ADD")
            colors = ["#FFD700", "#FF8800", "#FFFFFF"] # Gold, Orange, White
            for i in range(240):
                angle = i * (math.pi / 120)
                dist = 300 - (i % 60 * 4)
                x1, y1 = 512 + math.cos(angle)*dist, 512 + math.sin(angle)*dist
                cx1, cy1 = 512 + math.cos(angle + 0.5)*150, 512 + math.sin(angle + 0.5)*150
                send_command(s, f"COLOR {colors[i % len(colors)]}")
                send_command(s, f"ALPHA {120 + (i % 4)*30}")
                send_command(s, f"BEZIER {x1} {y1} {cx1} {cy1} {512} {512} {512} {512}")

            # 3. Stellar Nurseries (120 Luminous Particles)
            send_command(s, "COLOR white")
            for _ in range(120):
                angle = random.uniform(0, math.pi * 2)
                r_dist = random.randint(50, 450)
                px, py = 512 + math.cos(angle)*r_dist, 512 + math.sin(angle)*r_dist
                send_command(s, f"ALPHA {random.randint(150, 255)}")
                send_command(s, f"CIRCLE {px} {py} {random.randint(1, 4)}")

            # 4. The Forge Sigil (8x Growth Stage Marker)
            send_command(s, "BRUSH_TYPE SOLID")
            send_command(s, "BLENDING NORMAL")
            send_command(s, "COLOR cyan")
            send_command(s, "ALPHA 255")
            # Draw an "8" or infinity-like geometric marker
            bx, by = 900, 900
            send_command(s, f"CIRCLE {bx} {by-15} 12")
            send_command(s, f"CIRCLE {bx} {by+15} 15")
            
            send_command(s, "UPDATE")

        time.sleep(3) # Wait for the complex render
        send_command(s, "SAVE")
        
        # Final Capture
        send_command(s, "SAVE")
        print("[RECURSIVE ARTIST] Masterpiece captured.")
        
    print("[RECURSIVE ARTIST] Level Complete.")

if __name__ == "__main__":
    lvl = 1
    # IMPORTANT: Level 51+ requires Art Studio V3
    if len(sys.argv) > 1:
        lvl = int(sys.argv[1])
    draw_recursive_artist(lvl)

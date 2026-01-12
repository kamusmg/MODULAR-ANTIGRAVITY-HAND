import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk, ImageFilter, ImageColor
import datetime
import socket
import threading
import sys
import io

class NucleusArtStudioV3:
    def __init__(self, root):
        self.root = root
        self.root.title("Nucleus Art Studio V3 - THE NEURAL ERA")
        self.root.geometry("1150x1050")
        self.root.configure(bg="#0a0a0a")
        
        # Core Engine States
        self.res = 1024
        self.bg_color = (0, 0, 0, 255)
        self.current_color = (255, 255, 255, 255) # Default White RGBA
        self.alpha = 255
        self.brush_size = 3
        self.brush_type = "SOLID"
        self.blending_mode = "NORMAL"
        
        # Image Buffers
        self.canvas_image = Image.new("RGBA", (self.res, self.res), self.bg_color)
        self.draw = ImageDraw.Draw(self.canvas_image)
        self.tk_image = None
        
        self.last_update = 0
        self.update_interval = 0.05 # 20 FPS max for UI refresh
        
        # UI Layout
        self.setup_ui()
        self.update_screen(force=True)
        
        # Telepathy Server
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()
        
    def setup_ui(self):
        # Sidebar
        self.toolbar = tk.Frame(self.root, width=120, bg="#111")
        self.toolbar.pack(side="left", fill="y")
        
        tk.Label(self.toolbar, text="NEURAL CORE", fg="cyan", bg="#111", font=("Consolas", 12, "bold")).pack(pady=15)
        
        # Status indicators
        self.status_label = tk.Label(self.toolbar, text="IDLE", fg="#555", bg="#111", font=("Consolas", 9))
        self.status_label.pack(pady=5)
        
        # Tools
        tk.Button(self.toolbar, text="CLEAR", bg="#300", fg="white", borderwidth=0, command=self.clear_canvas).pack(fill="x", padx=10, pady=5)
        tk.Button(self.toolbar, text="EXPORT", bg="#005f00", fg="white", borderwidth=0, command=self.save_canvas).pack(fill="x", padx=10, pady=5)
        
        # Canvas Container
        self.canvas_frame = tk.Frame(self.root, bg="#000", borderwidth=2, relief="sunken")
        self.canvas_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        self.canvas_label = tk.Label(self.canvas_frame, bg="black")
        self.canvas_label.pack(expand=True)

    def update_screen(self, force=False):
        """Converts PIL buffer to Tkinter display."""
        now = datetime.datetime.now().timestamp()
        if not force and (now - self.last_update < self.update_interval):
            return
            
        try:
            display_size = 900
            # BILINEAR is much faster than LANCZOS for real-time
            display_img = self.canvas_image.resize((display_size, display_size), Image.BILINEAR)
            self.tk_image = ImageTk.PhotoImage(display_img)
            self.canvas_label.config(image=self.tk_image)
            self.last_update = now
        except Exception as e:
            print(f"[DISPLAY ERROR] {e}")

    def start_server(self):
        HOST = '127.0.0.1'
        PORT = 65432
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((HOST, PORT))
                s.listen()
                print(f"[V3 SERVER] Neural Link Online at {PORT}")
                while True:
                    try:
                        conn, addr = s.accept()
                        with conn:
                            self.root.after(0, lambda: self.status_label.config(text="LINKING...", fg="yellow"))
                            while True:
                                data = conn.recv(65536) # Massive buffer for V3 commands
                                if not data: break
                                buffer = data.decode()
                                for line in buffer.split('\n'):
                                    cmd = line.strip()
                                    if cmd:
                                        self.process_command(cmd)
                            self.root.after(0, lambda: self.status_label.config(text="DISCONNECTED", fg="red"))
                            self.root.after(0, self.update_screen)
                    except Exception as e:
                        print(f"[V3 CONNECTION ERROR] {e}")
        except Exception as e:
            print(f"[V3 SERVER CRITICAL FAIL] {e}")

    def process_command(self, cmd_str):
        parts = cmd_str.split()
        if not parts: return
        action = parts[0].upper()
        
        try:
            if action == "COLOR":
                self.set_color(parts[1])
            elif action == "ALPHA":
                self.alpha = int(parts[1])
            elif action == "BRUSH_SIZE":
                self.brush_size = int(parts[1])
            elif action == "BRUSH_TYPE":
                self.brush_type = parts[1].upper()
            elif action == "BLENDING":
                self.blending_mode = parts[1].upper()
            elif action == "CLEAR":
                self.root.after(0, self.clear_canvas)
            elif action == "SAVE":
                self.root.after(0, self.save_canvas)
            elif action == "LINE":
                x1, y1, x2, y2 = map(int, parts[1:])
                self.root.after(0, lambda: self.draw_line(x1, y1, x2, y2))
            elif action == "CIRCLE":
                cx, cy, r = map(int, parts[1:])
                self.root.after(0, lambda: self.draw_circle(cx, cy, r))
            elif action == "RECT":
                x1, y1, x2, y2 = map(int, parts[1:])
                self.root.after(0, lambda: self.draw_rect(x1, y1, x2, y2))
            elif action == "RECT_FILL":
                x1, y1, x2, y2 = map(int, parts[1:])
                self.root.after(0, lambda: self.draw_rect(x1, y1, x2, y2, fill=True))
            elif action == "CIRCLE_FILL":
                cx, cy, r = map(int, parts[1:])
                self.root.after(0, lambda: self.draw_circle(cx, cy, r, fill=True))
            elif action == "BEZIER":
                pts = list(map(int, parts[1:]))
                self.root.after(0, lambda: self.draw_bezier(pts))
            elif action == "FILTER":
                self.root.after(0, lambda: self.apply_filter(parts[1].upper()))
            elif action == "UPDATE":
                self.root.after(0, lambda: self.update_screen(force=True))
        except Exception as e:
            pass # Suppress command noise

    def set_color(self, color_str):
        try:
            if color_str.startswith('#'):
                rgb = ImageColor.getrgb(color_str)
            else:
                rgb = ImageColor.getrgb(color_str)
            self.current_color = rgb + (self.alpha,)
        except:
            self.current_color = (255, 255, 255, self.alpha)

    def get_draw_color(self):
        # Update current color with latest alpha
        r, g, b = self.current_color[:3]
        return (r, g, b, self.alpha)

    def draw_line(self, x1, y1, x2, y2):
        color = self.get_draw_color()
        if self.blending_mode == "ADD":
            # Glow effect: draw onto temp layer and composite
            temp = Image.new("RGBA", (self.res, self.res), (0,0,0,0))
            d = ImageDraw.Draw(temp)
            d.line([x1, y1, x2, y2], fill=color, width=self.brush_size)
            self.canvas_image = Image.alpha_composite(self.canvas_image, temp)
        else:
            self.draw.line([x1, y1, x2, y2], fill=color, width=self.brush_size)
        self.status_label.config(text="DRAWING", fg="cyan")
        self.update_screen()

    def draw_circle(self, cx, cy, r, fill=False):
        try:
            color = self.get_draw_color()
            # Ensure coordinates are sorted for PIL
            x0, x1 = min(cx-r, cx+r), max(cx-r, cx+r)
            y0, y1 = min(cy-r, cy+r), max(cy-r, cy+r)
            if fill:
                self.draw.ellipse([x0, y0, x1, y1], fill=color)
            else:
                if self.brush_type == "GLOW":
                    for i in range(5):
                        alpha_step = max(5, self.alpha // (i + 1))
                        c = color[:3] + (alpha_step,)
                        self.draw.ellipse([x0-i, y0-i, x1+i, y1+i], outline=c, width=self.brush_size+i)
                else:
                    self.draw.ellipse([x0, y0, x1, y1], outline=color, width=self.brush_size)
            self.status_label.config(text=f"CIRCLE {'FILL' if fill else 'OUTLINE'}", fg="cyan")
            self.update_screen()
        except Exception as e:
            print(f"[DRAW ERROR] Circle: {e}")

    def draw_rect(self, x1, y1, x2, y2, fill=False):
        try:
            color = self.get_draw_color()
            # Ensure coordinates are sorted for PIL
            nx1, nx2 = min(x1, x2), max(x1, x2)
            ny1, ny2 = min(y1, y2), max(y1, y2)
            if fill:
                self.draw.rectangle([nx1, ny1, nx2, ny2], fill=color)
            else:
                self.draw.rectangle([nx1, ny1, nx2, ny2], outline=color, width=self.brush_size)
            self.status_label.config(text=f"RECT {'FILL' if fill else 'OUTLINE'}", fg="cyan")
            self.update_screen()
        except Exception as e:
            print(f"[DRAW ERROR] Rect: {e}")

    def draw_bezier(self, pts):
        """pts: x1 y1 x2 y2 x3 y3 x4 y4 (Cubic)"""
        if len(pts) < 8: return
        color = self.get_draw_color()
        curve_pts = []
        for t in range(0, 101):
            t /= 100
            # Cubic Bezier formula
            x = (1-t)**3 * pts[0] + 3*(1-t)**2 * t * pts[2] + 3*(1-t) * t**2 * pts[4] + t**3 * pts[6]
            y = (1-t)**3 * pts[1] + 3*(1-t)**2 * t * pts[3] + 3*(1-t) * t**2 * pts[5] + t**3 * pts[7]
            curve_pts.append((x, y))
        self.draw.line(curve_pts, fill=color, width=self.brush_size, joint="curve")
        self.status_label.config(text="DRAWING CURVE", fg="magenta")
        self.update_screen()

    def apply_filter(self, name):
        if name == "BLUR":
            self.canvas_image = self.canvas_image.filter(ImageFilter.GaussianBlur(radius=2))
        elif name == "SHARP":
            self.canvas_image = self.canvas_image.filter(ImageFilter.SHARPEN)
        self.draw = ImageDraw.Draw(self.canvas_image)
        self.update_screen()

    def clear_canvas(self):
        # Reset to Radiant Defaults for Season 1 compatibility
        self.alpha = 255
        self.blending_mode = "NORMAL"
        self.brush_size = 3
        self.brush_type = "SOLID"
        self.current_color = (255, 255, 255, 255)
        
        self.canvas_image = Image.new("RGBA", (self.res, self.res), self.bg_color)
        self.draw = ImageDraw.Draw(self.canvas_image)
        self.update_screen(force=True)
        
    def save_canvas(self):
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"telepathic_art_{ts}.png"
        # Convert to RGB for saving if no alpha needed in file, or keep RGBA
        self.canvas_image.save(filename)
        print(f"[V3 STUDIO] Exported: {filename}")
        self.status_label.config(text="EXPORTED", fg="spring green")

if __name__ == "__main__":
    root = tk.Tk()
    app = NucleusArtStudioV3(root)
    root.mainloop()

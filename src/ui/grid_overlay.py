import tkinter as tk
import time

class GridOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.5) # Semi-transparent
        self.root.configure(background='black')
        
        # Remove window decorations (transparent background hack for Windows is tricky,
        # so we stick to semi-transparent black for the 'Cyberpunk/Matrix' feel)
        
        self.canvas = tk.Canvas(self.root, highlightthickness=0, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.draw_grid()
        
        # Auto-close after 10 seconds
        self.root.after(10000, self.close)
        
        # Exit on Escape
        self.root.bind("<Escape>", lambda e: self.close())
        
        print(f"[GRID] Overlay Initialized. {self.screen_width}x{self.screen_height}")

    def draw_grid(self, step=100):
        # Vertical Lines
        for x in range(0, self.screen_width, step):
            self.canvas.create_line(x, 0, x, self.screen_height, fill='#00FF00', dash=(2, 4))
            self.canvas.create_text(x + 5, 20, text=str(x), fill='#00FF00', anchor='nw', font=('Consolas', 10))

        # Horizontal Lines
        for y in range(0, self.screen_height, step):
            self.canvas.create_line(0, y, self.screen_width, y, fill='#00FF00', dash=(2, 4))
            self.canvas.create_text(5, y + 5, text=str(y), fill='#00FF00', anchor='nw', font=('Consolas', 10))

        # Center Crosshair
        cx, cy = self.screen_width // 2, self.screen_height // 2
        self.canvas.create_line(cx - 20, cy, cx + 20, cy, fill='red', width=2)
        self.canvas.create_line(cx, cy - 20, cx, cy + 20, fill='red', width=2)
        self.canvas.create_text(cx + 10, cy + 10, text="NUCLEUS SIGHT", fill='red', font=('Consolas', 12, 'bold'))

    def close(self):
        print("[GRID] Closing overlay.")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    overlay = GridOverlay()
    overlay.run()

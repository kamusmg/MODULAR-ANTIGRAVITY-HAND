import tkinter as tk

class MockPaint:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mock Paint")
        self.root.geometry("800x600")
        
        # Tools Frame
        self.tools = tk.Frame(self.root, bg="lightgray")
        self.tools.pack(side="left", fill="y", padx=5, pady=5)
        
        # Keywords for OCR detection
        tk.Label(self.tools, text="Tools", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self.tools, text="Colors", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self.tools, text="Shapes", font=("Arial", 20, "bold")).pack(pady=10)
        
        # Canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=600)
        self.canvas.pack(side="right", fill="both", expand=True)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)

if __name__ == "__main__":
    MockPaint()

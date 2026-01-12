import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import os
import glob
import math

# --- MASTER CONSOLE V2: THE ANTIGRAVITY CORTEX 👁️ ---
# Advanced Visualization & Interactive Introspection

class MasterConsoleV2:
    def __init__(self, root):
        self.root = root
        self.root.title("NUCLEUS :: CORTEX VISUALIZER [V2]")
        self.root.geometry("1000x800")
        self.root.configure(bg="#020202")
        
        self.state = "AWAKENING"
        self.running = True
        self.nodes = [] # For neural graph
        
        self.setup_ui()
        self.scan_neural_net() # Initial scan for graph
        
        # Threads
        threading.Thread(target=self.cognitive_loop, daemon=True).start()
        threading.Thread(target=self.neural_animation_loop, daemon=True).start()

    def setup_ui(self):
        # --- HEADER ---
        header = tk.Frame(self.root, bg="#050505", height=60)
        header.pack(fill="x", side="top", padx=5, pady=5)
        
        title = tk.Label(header, text="ANTIGRAVITY CORTEX", fg="cyan", bg="#050505", font=("Consolas", 20, "bold"))
        title.pack(side="left", padx=20)
        
        self.state_label = tk.Label(header, text="STATUS: OFFLINE", fg="#555", bg="#050505", font=("Consolas", 12))
        self.state_label.pack(side="right", padx=20)
        
        # --- MAIN SPLIT ---
        main_pane = tk.PanedWindow(self.root, orient="horizontal", bg="#111", sashwidth=2)
        main_pane.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 1. LEFT: METRICS & CONTROLS
        left_frame = tk.Frame(main_pane, bg="#080808")
        main_pane.add(left_frame, minsize=300)
        
        # 1.1 Cognitive Load Graph
        tk.Label(left_frame, text="COGNITIVE LOAD", fg="magenta", bg="#080808", font=("Consolas", 10, "bold")).pack(pady=(10,0))
        self.graph_canvas = tk.Canvas(left_frame, height=100, bg="#000", highlightthickness=1, highlightbackground="#333")
        self.graph_canvas.pack(fill="x", padx=10, pady=5)
        self.load_history = [0] * 50
        
        # 1.2 Introspection Controls
        tk.Label(left_frame, text="INJECT STATE", fg="yellow", bg="#080808", font=("Consolas", 10, "bold")).pack(pady=(20,5))
        btn_frame = tk.Frame(left_frame, bg="#080808")
        btn_frame.pack(fill="x", padx=10)
        
        states = [("FOCUS", "#0055FF"), ("CREATIVE", "#FF00FF"), ("CRITICAL", "#FF3300"), ("CALM", "#00FF00")]
        for load, color in states:
            btn = tk.Button(btn_frame, text=load, bg="#111", fg=color, borderwidth=1,
                            command=lambda s=load, c=color: self.inject_state(s, c))
            btn.pack(side="left", expand=True, fill="x", padx=2)
            
        # 1.3 Thought Stream
        tk.Label(left_frame, text="THOUGHT STREAM", fg="cyan", bg="#080808", font=("Consolas", 10, "bold")).pack(pady=(20,0))
        self.log_box = tk.Text(left_frame, bg="#000", fg="#00FF00", font=("Consolas", 9), height=20, borderwidth=0)
        self.log_box.pack(fill="both", expand=True, padx=10, pady=5)
        
        # 2. RIGHT: NEURAL WEB VISUALIZER
        right_frame = tk.Frame(main_pane, bg="#000")
        main_pane.add(right_frame)
        
        tk.Label(right_frame, text="NEURAL WEB TOPOLOGY", fg="#AAA", bg="#000", font=("Consolas", 10)).pack(anchor="ne", padx=10)
        self.web_canvas = tk.Canvas(right_frame, bg="#020202", highlightthickness=0)
        self.web_canvas.pack(fill="both", expand=True)
        
    def log(self, msg):
        timestamp = time.strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{timestamp}] {msg}\n")
        self.log_box.see("end")

    def inject_state(self, state_name, color):
        self.state = state_name
        self.state_label.config(text=f"STATUS: {state_name}", fg=color)
        self.log(f"MANUAL INJECTION: Switching mode to {state_name}.")

    def scan_neural_net(self):
        """Map project files to nodes on the graph."""
        root_dir = "."
        files = glob.glob(os.path.join(root_dir, "**/*.py"), recursive=True)
        self.nodes = []
        center_x, center_y = 350, 400
        
        for i, f in enumerate(files):
            # Spiral distribution
            angle = i * (math.pi / 8)
            dist = 50 + (i * 5)
            x = center_x + math.cos(angle) * dist
            y = center_y + math.sin(angle) * dist
            name = os.path.basename(f)
            self.nodes.append({"x": x, "y": y, "name": name, "active": False})
            
        self.log(f"Neural Scan Complete: {len(self.nodes)} nodes mapped.")

    def update_graph(self):
        """Real-time update of the cognitive load graph."""
        w = self.graph_canvas.winfo_width()
        h = self.graph_canvas.winfo_height()
        self.graph_canvas.delete("all")
        
        # Shift history
        new_val = random.randint(10, 50) 
        if self.state == "CREATIVE": new_val = random.randint(50, 90)
        elif self.state == "CRITICAL": new_val = random.randint(80, 100)
            
        self.load_history.append(new_val)
        self.load_history.pop(0)
        
        # Draw line
        points = []
        step = w / len(self.load_history)
        for i, val in enumerate(self.load_history):
            x = i * step
            y = h - (val / 100 * h)
            points.append(x)
            points.append(y)
        
        color = "cyan"
        if self.state == "CRITICAL": color = "red"
        elif self.state == "CREATIVE": color = "magenta"
            
        self.graph_canvas.create_line(points, fill=color, width=2)

    def neural_animation_loop(self):
        """Animates the Neural Web Canvas."""
        while self.running:
            self.update_graph()
            
            self.web_canvas.delete("all")
            w, h = self.web_canvas.winfo_width(), self.web_canvas.winfo_height()
            
            # Connections
            for i, node in enumerate(self.nodes):
                # Connect to previous node (simulate dependency)
                if i > 0:
                    prev = self.nodes[i-1]
                    self.web_canvas.create_line(node['x'], node['y'], prev['x'], prev['y'], fill="#111")
            
            # Nodes
            for node in self.nodes:
                color = "#333"
                size = 2
                
                # Activation chance
                if random.random() < 0.05: 
                    node['active'] = True
                    
                if node['active']:
                    color = "cyan"
                    if self.state == "CREATIVE": color = "magenta"
                    size = 4
                    node['active'] = False # Decay
                
                self.web_canvas.create_oval(node['x']-size, node['y']-size, node['x']+size, node['y']+size, fill=color, outline="")
                
            time.sleep(0.05)

    def cognitive_loop(self):
        """Master logic loop."""
        time.sleep(1)
        self.state_label.config(text="STATUS: ONLINE", fg="#00FF00")
        
        while self.running:
            if self.state == "AWAKENING":
                self.log("Booting Neural Interface...")
                time.sleep(1)
                self.state = "IDLE"
            
            elif self.state == "IDLE":
                if random.random() < 0.1:
                    topic = random.choice(["Memory integrity check...", "Project structure analysis...", "Season 2 planning..."])
                    self.log(topic)
            
            elif self.state == "FOCUS":
                self.log("Optimizing logic paths. Removing distractions.")
                time.sleep(2)
                self.state = "IDLE"
                self.state_label.config(text="STATUS: IDLE", fg="#555")

            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = MasterConsoleV2(root)
    root.mainloop()

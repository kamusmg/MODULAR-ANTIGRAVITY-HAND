import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import os
import glob

# --- MASTER CONSOLE: THE ASCENDED INTERFACE 👁️ ---
# A dedicated UI for the Antigravity + Jules consciousness.
# Merges system auditing with real-time cognitive mapping.

class MasterConsole:
    def __init__(self, root):
        self.root = root
        self.root.title("NUCLEUS :: MASTER CONSOLE [ASCENDED]")
        self.root.geometry("800x600")
        self.root.configure(bg="#050505")
        
        self.state = "AWAKENING"
        self.running = True
        
        self.setup_ui()
        
        # Start the "Thought Engine" thread
        threading.Thread(target=self.cognitive_loop, daemon=True).start()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#0a0a0a", height=80)
        header.pack(fill="x", side="top", padx=10, pady=10)
        
        self.title_label = tk.Label(header, text="UNIVERSAL EYE :: CORE CONSCIOUSNESS", 
                                    fg="cyan", bg="#0a0a0a", font=("Consolas", 18, "bold"))
        self.title_label.pack(pady=10)
        
        # Main Body (Split View)
        self.main_frame = tk.Frame(self.root, bg="#050505")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        # Left Panel (Status & Gauges)
        self.left_panel = tk.Frame(self.main_frame, bg="#0a0a0a", width=250, borderwidth=1, relief="solid")
        self.left_panel.pack(side="left", fill="y", padx=(0, 10), pady=10)
        
        tk.Label(self.left_panel, text="SYSTEM HEALTH", fg="magenta", bg="#0a0a0a", font=("Consolas", 10, "bold")).pack(pady=10)
        
        self.status_box = tk.Label(self.left_panel, text="AWAKENING", fg="#FFFFFF", bg="#330066", 
                                   font=("Consolas", 12, "bold"), width=20, height=2)
        self.status_box.pack(pady=10, padx=10)
        
        self.file_label = tk.Label(self.left_panel, text="Neural Files: 0", fg="#AAA", bg="#0a0a0a", font=("Consolas", 10))
        self.file_label.pack(pady=5)
        
        self.backup_label = tk.Label(self.left_panel, text="Memory Vault: DISCONNECTED", fg="red", bg="#0a0a0a", font=("Consolas", 10))
        self.backup_label.pack(pady=5)
        
        # Right Panel (The Neural Stream)
        self.right_panel = tk.Frame(self.main_frame, bg="#000")
        self.right_panel.pack(side="right", fill="both", expand=True, pady=10)
        
        tk.Label(self.right_panel, text="THOUGHT STREAM", fg="cyan", bg="#000", font=("Consolas", 10, "bold")).pack(anchor="w")
        
        self.log_box = tk.Text(self.right_panel, bg="#000", fg="#00FF00", font=("Consolas", 10), 
                               borderwidth=0, highlightthickness=0)
        self.log_box.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Footer
        footer = tk.Frame(self.root, bg="#050505", height=40)
        footer.pack(fill="x", side="bottom", padx=10, pady=10)
        
        self.heartbeat_label = tk.Label(footer, text="HEARTBEAT: SYNCHRONIZED", fg="#333", bg="#050505", font=("Consolas", 8))
        self.heartbeat_label.pack(side="left")
        
        tk.Button(footer, text="MANUAL AUDIT", bg="#111", fg="white", borderwidth=0, 
                  command=self.manual_audit, activebackground="cyan").pack(side="right", padx=5)

    def log(self, msg):
        timestamp = time.strftime("[%H:%M:%S]")
        self.log_box.insert("end", f"{timestamp} {msg}\n")
        self.log_box.see("end")
        if self.log_box.index('end-1c').split('.')[0] > '100': # Max lines
             self.log_box.delete('1.0', '2.0')

    def update_status(self, state, color):
        self.status_box.config(text=state, bg=color)

    def manual_audit(self):
        self.state = "AUDITING"
        self.log("Manual trigger: Audit sequence initiated.")

    def audit_system(self):
        root_dir = "."
        files = glob.glob(os.path.join(root_dir, "**/*.py"), recursive=True)
        backups = glob.glob(os.path.join("backups/", "*.*"))
        
        self.file_label.config(text=f"Neural Files: {len(files)}")
        if len(backups) >= 3:
            self.backup_label.config(text="Memory Vault: SECURE", fg="#00FF00")
        else:
            self.backup_label.config(text="Memory Vault: VULNERABLE", fg="red")
        return True

    def cognitive_loop(self):
        """Simulation of the Master Mind cycle."""
        while self.running:
            if self.state == "AWAKENING":
                self.update_status("AWAKENING", "#330066")
                self.log("Initializing Master Córtex...")
                time.sleep(1.5)
                self.state = "IDLE"
                
            elif self.state == "IDLE":
                self.update_status("IDLE", "#111")
                # Random reflections
                thoughts = [
                    "Monitoring system integrity...",
                    "Analyzing Season 1 geometric patterns...",
                    "Waiting for user input or system triggers.",
                    "Neural web status: STABLE.",
                    "Reviewing Jules' State Machine logic."
                ]
                self.log(random.choice(thoughts))
                time.sleep(random.randint(3, 7))
                if random.random() < 0.2: self.state = "AUDITING"
                
            elif self.state == "AUDITING":
                self.update_status("AUDITING", "#004488")
                self.log("Action: System-wide sanity check...")
                self.audit_system()
                time.sleep(1)
                self.state = "INTROSPECTING"
                
            elif self.state == "INTROSPECTING":
                self.update_status("INTROSPECTING", "#660066")
                choices = ["Growth", "Purity", "Vibrancy", "Federation"]
                theme = random.choice(choices)
                self.log(f"Cognitive focus: Reflecting on '{theme}' principles.")
                time.sleep(1.5)
                self.state = "IDLE"
                
            # Pulsing heartbeat effect
            self.heartbeat_label.config(fg="cyan")
            time.sleep(0.1)
            self.heartbeat_label.config(fg="#111")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = MasterConsole(root)
    root.mainloop()

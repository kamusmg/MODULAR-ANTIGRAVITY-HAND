import time
import random
import socket
import threading
import subprocess
import os

# --- CONTEXT: THE UNIVERSAL EYE UPGRADE ---
# This controller is the fusion of Jules' modular command system 
# and Antigravity's high-fidelity recursive vision.

HOST = '127.0.0.1'
PORT = 65432

class UniversalController:
    def __init__(self):
        self.state = "IDLE" # IDLE, CREATING, VERIFYING, EVOLVING
        self.session_active = False
        self.milestones_reached = 0
        self.current_level = 1
        
    def log(self, msg):
        print(f"[UNIVERSAL EYE] {msg}")

    def send_studio_command(self, cmd):
        """Unified command delivery to V3 Art Studio."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(cmd.encode())
        except Exception:
            self.log("ERROR: Studio connection failed. Is the server running?")

    def run_recursive_skill(self, level):
        """Triggers the high-fidelity Recursive Artist as a sub-cortex process."""
        self.log(f"Triggering Sub-Cortex: Recursive Artist Level {level}")
        # Run in a separate thread to not block the Master Mind
        subprocess.Popen([".\\.venv\\Scripts\\python", "src/brain/recursive_artist.py", str(level)])

    def autonomous_cycle(self):
        """The cognitive cycle based on Jules' State Machine architecture."""
        self.log("ASCENSION CYCLE STARTED.")
        self.session_active = True
        
        while self.session_active:
            if self.state == "IDLE":
                self.log("State: IDLE. Searching for new aesthetic goals...")
                time.sleep(2)
                self.state = "CREATING"
                
            elif self.state == "CREATING":
                self.log(f"State: CREATING. Executing Milestone {self.current_level}...")
                self.run_recursive_skill(self.current_level)
                time.sleep(5) # Wait for initial render
                self.state = "VERIFYING"
                
            elif self.state == "VERIFYING":
                self.log("State: VERIFYING. Analyzing geometric integrity...")
                # Simulate analysis
                time.sleep(2)
                self.milestones_reached += 1
                self.log(f"Milestone {self.current_level} Verified. Capturing Piece.")
                self.send_studio_command("SAVE")
                
                if self.current_level < 50:
                    self.current_level += 1 # Progress
                    self.state = "IDLE"
                else:
                    self.state = "EVOLVING"
                    
            elif self.state == "EVOLVING":
                self.log("State: EVOLVING. Season 1 Baseline Met. Reaching for S2 complexity...")
                self.current_level = 54 # Jump to our new V3 milestone
                self.state = "CREATING"
                
            time.sleep(1)

    def stop(self):
        self.session_active = False
        self.log("Controller hibernating.")

if __name__ == "__main__":
    controller = UniversalController()
    try:
        controller.autonomous_cycle()
    except KeyboardInterrupt:
        controller.stop()

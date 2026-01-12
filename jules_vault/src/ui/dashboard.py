import customtkinter as ctk
from PIL import Image, ImageTk
import subprocess
import threading
import time
import json
from src.core.vision import VisionSystem
from src.core.controller import BodyController
from src.brain.real_mind import RealMind
from src.core.memory import Hippocampus # New


class CommandDesk(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configurations ---
        self.title("NUCLEUS :: Mesa de Comando")
        self.geometry("1000x700")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        
        # --- Modules ---
        self.vision = VisionSystem()
        self.body = BodyController()
        self.mind = RealMind()
        self.memory = Hippocampus() # New
        self.session_id = self.memory.start_session()
        
        self.running = False
        
        # --- UI Layout ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3) # Vision
        self.grid_rowconfigure(1, weight=1) # Controls
        self.grid_rowconfigure(2, weight=1) # Abilities
        self.grid_rowconfigure(3, weight=1) # Status

        self._setup_vision_panel()
        self._setup_control_panel()
        self._setup_abilities_panel()
        self._setup_status_bar()
        
        self.log(f"SESSION STARTED: ID {self.session_id}")

        
    def _setup_vision_panel(self):
        self.vision_frame = ctk.CTkFrame(self, corner_radius=10)
        self.vision_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.vision_label = ctk.CTkLabel(self.vision_frame, text="[ NO SIGNAL ]")
        self.vision_label.pack(expand=True, fill="both", padx=5, pady=5)
        
    def _setup_control_panel(self):
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        # Columns: Motor (Left), Keyboard (Center), Log (Right)
        self.control_frame.columnconfigure(0, weight=1)
        self.control_frame.columnconfigure(1, weight=1)
        self.control_frame.columnconfigure(2, weight=2)
        
        # --- Motor Control ---
        self.motor_frame = ctk.CTkFrame(self.control_frame)
        self.motor_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(self.motor_frame, text="CONTROLE MOTOR", font=("Consolas", 12, "bold")).pack()
        
        self.dir_label = ctk.CTkLabel(self.motor_frame, text="[ PARADO ]", font=("Consolas", 16), text_color="#00FF00")
        self.dir_label.pack(pady=10)
        
        self.action_label = ctk.CTkLabel(self.motor_frame, text="ACAO: NENHUMA")
        self.action_label.pack()

        # --- Keyboard ---
        self.kbd_frame = ctk.CTkFrame(self.control_frame)
        self.kbd_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(self.kbd_frame, text="TECLADO VIRTUAL", font=("Consolas", 12, "bold")).pack()
        
        self.kbd_text = ctk.CTkEntry(self.kbd_frame, placeholder_text="Aguardando input...")
        self.kbd_text.pack(pady=10, padx=10, fill="x")
        
        # --- Thought Log ---
        self.log_frame = ctk.CTkFrame(self.control_frame)
        self.log_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(self.log_frame, text="LOG DE PENSAMENTO", font=("Consolas", 12, "bold")).pack()
        
        self.log_box = ctk.CTkTextbox(self.log_frame, height=100, font=("Consolas", 10))
        self.log_box.pack(fill="both", expand=True, padx=5, pady=5)
        
    def _setup_abilities_panel(self):
        self.ability_frame = ctk.CTkFrame(self)
        self.ability_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        ctk.CTkLabel(self.ability_frame, text="NUCLEUS SKILLS", font=("Consolas", 12, "bold")).pack(pady=5)
        
        btn_frame = ctk.CTkFrame(self.ability_frame, fg_color="transparent")
        btn_frame.pack(fill="x", padx=10, pady=5)
        
        # Skill Buttons
        skills = [
            ("🎨 PAINT", "src/brain/vision_artist.py"),
            ("🗣️ SPEAK", "src/brain/speaker.py"),
            ("🎵 SING", "src/brain/composer.py"),
            ("🎮 GAME", "src/brain/game.py"),
            ("🌳 GROW", "src/brain/garden.py"),
            ("🧮 MATH", "src/brain/mathematician.py"),
            ("☁️ SYNC", "src/brain/sync.py") # New
        ]

        
        for text, script in skills:
            btn = ctk.CTkButton(btn_frame, text=text, width=100, 
                                command=lambda s=script: self._run_skill(s))
            btn.pack(side="left", padx=5, expand=True)

    def _run_skill(self, script_path):
        self.log(f"EXECUTING SKILL: {script_path}")
        subprocess.Popen(["python", script_path], shell=True)

    def _setup_status_bar(self):
        self.status_frame = ctk.CTkFrame(self, height=40)
        self.status_frame.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")
        
        self.status_led = ctk.CTkLabel(self.status_frame, text="🧠 WAITING", text_color="gray")
        self.status_led.pack(side="left", padx=20)
        
        self.btn_start = ctk.CTkButton(self.status_frame, text="LIGAR AI", command=self.toggle_ai, fg_color="green")
        self.btn_start.pack(side="right", padx=10, pady=5)

    def log(self, text):
        self.log_box.insert("end", f"> {text}\n")
        self.log_box.see("end")

    def toggle_ai(self):
        if not self.running:
            self.running = True
            self.btn_start.configure(text="DESLIGAR AI", fg_color="red")
            self.status_led.configure(text="🧠 CALCULATING", text_color="#00FF00")
            threading.Thread(target=self.process_loop, daemon=True).start()
        else:
            self.running = False
            self.btn_start.configure(text="LIGAR AI", fg_color="green")
            self.status_led.configure(text="🧠 OFFLINE", text_color="gray")

    def process_loop(self):
        while self.running:
            # 1. Capture Sense
            img_pil = self.vision.capture_screen()
            
            # Update Vision UI (resize for performance)
            if img_pil:
                ui_img = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(480, 270))
                self.vision_label.configure(image=ui_img, text="")
            
            # 2. Think
            decision = self.mind.think(img_pil)
            
            # Memory Log
            thought_text = decision.get("pensamento", "")
            if thought_text:
                self.memory.remember_thought(self.session_id, thought_text)
            
            # Update UI Log
            self.log_box.after(0, lambda: self.log(thought_text))

            
            # 3. Act
            self.body.execute_command(decision)
            
            # Update Status UI
            mouse_cmd = decision.get("comando_mouse", {})
            direction = mouse_cmd.get("direcao", "PARADO")
            action = mouse_cmd.get("acao", "NENHUMA")
            
            try:
                self.dir_label.configure(text=f"[ {direction} ]")
                self.action_label.configure(text=f"ACAO: {action}")
                
                kbd_cmd = decision.get("comando_teclado", {})
                txt = kbd_cmd.get("texto", "")
                if txt:
                     self.kbd_text.delete(0, "end")
                     self.kbd_text.insert(0, txt)
            except:
                pass

            time.sleep(1) # Slow down for observation

if __name__ == "__main__":
    app = CommandDesk()
    app.mainloop()

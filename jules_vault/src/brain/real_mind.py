import time
import random
import pytesseract
import numpy as np
import cv2
import sys
import os

# Ensure src is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.core.os_interface import os_system

class RealMind:
    def __init__(self):
        self.state = "IDLE" # IDLE, WORKING, WAITING
        self.goal = None
        self.last_thought_time = 0
        self.app_started_time = 0
        self.memory = []
        
        # Goals definition
        self.goals = [
            {"name": "PAINTING", "trigger": "paint", "app": "paint", "keywords": ["Tools", "Colors", "Shapes"]},
            {"name": "CALCULATING", "trigger": "calc", "app": "calculator", "keywords": ["Calculator", "Standard", "C", "="]}
        ]
        
        self.current_app_process = None

    def think(self, visual_input):
        """
        Main cognitive cycle.
        visual_input: PIL Image from VisionSystem
        Returns: Dict with thought and commands.
        """
        current_time = time.time()
        
        # 0. Interpret Vision (OCR)
        # We only do this every few seconds to save resources
        screen_text = ""
        if visual_input and (current_time - self.last_thought_time > 2.0):
            try:
                # Convert to CV2 for preprocessing if needed, but Tesseract handles PIL
                screen_text = pytesseract.image_to_string(visual_input)
                # Cleanup text
                screen_text = " ".join(screen_text.split())
                self.last_thought_time = current_time
            except Exception as e:
                print(f"[MIND] Vision Error: {e}")
                self.last_thought_time = current_time

        # 1. Decide State
        if self.state == "IDLE":
            # Pick a random goal if none
            new_goal = random.choice(self.goals)
            self.goal = new_goal
            self.state = "STARTING_APP"
            return {
                "pensamento": f"DECISÃO: Estou entediado. Vou iniciar a atividade: {new_goal['name']}.",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {}
            }

        elif self.state == "STARTING_APP":
            # Check if app is already visible
            found = False
            if self.goal:
                for kw in self.goal['keywords']:
                    if kw in screen_text:
                        found = True
                        break
            
            if found:
                self.state = "WORKING"
                return {
                    "pensamento": f"PERCEPÇÃO: Vejo o {self.goal['name']}. O aplicativo está aberto. Começando trabalho.",
                    "comando_mouse": {"direcao": "PARADO"},
                    "comando_teclado": {}
                }
            else:
                # Launch App
                # Check cooldown (avoid spamming launch)
                if self.goal and (time.time() - self.app_started_time > 5.0):
                    os_system.launch_app(self.goal['app'])
                    self.app_started_time = time.time()
                    return {
                        "pensamento": f"AÇÃO: Abrindo {self.goal['app']}...",
                        "comando_mouse": {"direcao": "PARADO"},
                        "comando_teclado": {}
                    }
                else:
                    return {
                        "pensamento": f"AGUARDANDO: {self.goal['app']} abrir...",
                        "comando_mouse": {"direcao": "PARADO"},
                        "comando_teclado": {}
                    }
        
        elif self.state == "WORKING":
            # Perform actions based on goal
            if self.goal['name'] == "PAINTING":
                return self._behavior_paint()
            elif self.goal['name'] == "CALCULATING":
                return self._behavior_calc(screen_text)
                
        return {
            "pensamento": "Processando...",
            "comando_mouse": {"direcao": "PARADO"},
            "comando_teclado": {}
        }

    def _behavior_paint(self):
        # Random painting movements
        actions = ["ARRASTAR", "CLIQUE", "MOVER"]
        directions = ["CIMA", "BAIXO", "ESQUERDA", "DIREITA", "CIMA_DIREITA", "BAIXO_ESQUERDA"]
        
        act = random.choice(actions)
        dire = random.choice(directions)
        
        thought = f"CRIANDO: Pincelada para {dire} ({act})"
        
        return {
            "pensamento": thought,
            "comando_mouse": {"direcao": dire, "acao": act, "intensidade": "ALTA"},
            "comando_teclado": {}
        }

    def _behavior_calc(self, screen_text):
        # Type numbers
        ops = ['+', '-', '*', '/']
        
        if random.random() < 0.1:
            key = 'enter' # Calculate
            thought = "CALCULANDO: Resultado..."
            return {
                "pensamento": thought,
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {"teclas_especiais": ["enter"]} # specific to calculator app usually
            }
        else:
            digit = str(random.randint(0, 9))
            if random.random() < 0.3:
                digit = random.choice(ops)
                
            thought = f"CALCULANDO: Inserindo '{digit}'"
            return {
                "pensamento": thought,
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {"texto": digit}
            }

import sys
import os
import json
import time
import fire


# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.core.controller import BodyController
from src.core.vision import VisionSystem

class NeuralLink:
    """
    Direct Neural Link (CLI) for Nucleus.
    Allows the AI Agent to control the Body directly.
    """
    def __init__(self):
        self.body = BodyController()
        self.vision = VisionSystem()

    def look(self, filename="vision_buffer.png"):
        """Captures the screen and saves it to a file."""
        print("[LINK] Capturing visual input (ALL SCREENS)...")
        from PIL import ImageGrab
        import datetime
        
        # Capture all monitors
        screenshot = ImageGrab.grab(all_screens=True)
        
        # Save
        # The filename parameter is ignored as per the instruction's specific implementation
        output_filename = os.path.join(os.getcwd(), "vision_buffer.png")
        screenshot.save(output_filename)
        print(f"[LINK] Visual input saved to: {output_filename}")
        return output_filename

    def move(self, direction="PARADO", intensity="MEDIA"):
        """Moves the mouse (N, S, E, W, etc)."""
        cmd = {
            "comando_mouse": {
                "direcao": direction,
                "intensidade": intensity,
                "acao": "NENHUMA"
            }
        }
        self.body.execute_command(cmd)

    def click(self, type="CLIQUE_ESQUERDO"):
        """Clicks the mouse."""
        cmd = {
            "comando_mouse": {
                "direcao": "PARADO",
                "acao": type
            }
        }
        self.body.execute_command(cmd)

    def drag(self, direction="PARADO", intensity="MEDIA"):
        """Drags the mouse (holding left button)."""
        cmd = {
            "comando_mouse": {
                "direcao": direction,
                "intensidade": intensity,
                "acao": "ARRASTAR"
            }
        }
        self.body.execute_command(cmd)

    def find(self, template_path):
        """Finds an image on screen and prints coordinates."""
        print(f"[LINK] Searching for {template_path}...")
        coords = self.vision.find_template(template_path, debug_save="debug_vision.png")
        if coords:
            print(f"[LINK] FOUND at: {coords}")
        else:
            print(f"[LINK] NOT FOUND.")

    def type(self, text):
        """Types text."""
        cmd = {
            "comando_teclado": {
                "texto": text
            }
        }
        self.body.execute_command(cmd)
        
    def press(self, key):
        """Presses a special key."""
        cmd = {
            "comando_teclado": {
                "teclas_especiais": [key]
            }
        }
        self.body.execute_command(cmd)

if __name__ == '__main__':
    fire.Fire(NeuralLink)

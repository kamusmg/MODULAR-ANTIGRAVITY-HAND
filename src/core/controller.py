import pyautogui
import random
import time
import json

class BodyController:
    def __init__(self):
        # Failsafe: move mouse to upper-left corner to abort
        pyautogui.FAILSAFE = True
        self.screen_width, self.screen_height = pyautogui.size()
        
    def execute_command(self, command_data):
        """
        Executes a command based on the AI's JSON output.
        Expected format:
        {
            "comando_mouse": { "direcao": "...", "acao": "..." },
            "comando_teclado": { "texto": "..." }
        }
        """
        try:
            if "comando_mouse" in command_data:
                mouse_cmd = command_data["comando_mouse"]
                self._handle_mouse(mouse_cmd)
                
            if "comando_teclado" in command_data:
                kbd_cmd = command_data["comando_teclado"]
                self._handle_keyboard(kbd_cmd)
                
            print(f"[BODY] Executed: {command_data}")
            return True
        except Exception as e:
            print(f"[BODY] Error executing command: {e}")
            return False

    def _handle_mouse(self, cmd):
        direction = cmd.get("direcao", "NENHUMA")
        action = cmd.get("acao", "NENHUMA")
        intensity = cmd.get("intensidade", "MEDIA")
        
        # Calculate movement vector
        dx, dy = 0, 0
        step_size = 50  # Base pixels to move
        
        if intensity == "ALTA": step_size = 150
        elif intensity == "BAIXA": step_size = 20

        if "ESQUERDA" in direction: dx = -step_size
        if "DIREITA" in direction: dx = step_size
        if "CIMA" in direction: dy = -step_size
        if "BAIXO" in direction: dy = step_size
        
        # Add "Motor Error" (Jitter) for organic feel
        jitter_x = random.randint(-5, 5)
        jitter_y = random.randint(-5, 5)
        
        current_x, current_y = pyautogui.position()
        target_x = current_x + dx + jitter_x
        target_y = current_y + dy + jitter_y
        
        # Clamp to screen bounds
        target_x = max(0, min(target_x, self.screen_width - 1))
        target_y = max(0, min(target_y, self.screen_height - 1))
        
        # Move
        if dx != 0 or dy != 0:
            pyautogui.moveTo(target_x, target_y, duration=0.3, tween=pyautogui.easeInOutQuad)
            
        # Click
        if action == "CLIQUE_ESQUERDO" or action == "CLIQUE":
            pyautogui.click()
        elif action == "CLIQUE_DIREITO":
            pyautogui.rightClick()
        elif action == "CLIQUE_DUPLO":
            pyautogui.doubleClick()
        elif action == "ARRASTAR":
            # Drag to the target position
            pyautogui.dragTo(target_x, target_y, duration=0.5, button='left')

    def _handle_keyboard(self, cmd):
        text = cmd.get("texto", "")
        special_keys = cmd.get("teclas_especiais", [])
        
        if text:
            # Type like a child/novice (delays between keys)
            pyautogui.write(text, interval=0.15)
            
        if special_keys:
            for key in special_keys:
                pyautogui.press(key)
                time.sleep(0.5)

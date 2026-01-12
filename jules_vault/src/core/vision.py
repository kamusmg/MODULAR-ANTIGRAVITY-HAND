import mss
import logging
import cv2
import numpy as np
from PIL import Image

class VisionSystem:
    def __init__(self):
        # We don't initialize mss here to avoid threading issues on Linux/X11
        # when this object is shared across threads.
        pass

    def capture_screen(self, monitor_index=1):
        """
        Captures the current screen state.
        Returns a PIL Image object.
        """
        try:
            with mss.mss() as sct:
                # Use specific monitor if provided, else default to 1 (primary usually)
                # sct.monitors[0] is 'all monitors', [1] is first.
                if monitor_index >= len(sct.monitors):
                    monitor_index = 1
                
                monitor = sct.monitors[monitor_index]
                
                sct_img = sct.grab(monitor)
                img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
                return img
        except Exception as e:
            print(f"[VISION] Capture failed: {e}")
            return None

    def find_template(self, template_path, confidence=0.8, debug_save=None):
        """
        Locates a template image on the screen.
        Returns (x, y) center coordinates or None.
        """
        try:
            # 1. Capture Screen
            screen_pil = self.capture_screen()
            if not screen_pil: return None
            
            # Convert PIL (RGB) to OpenCV (BGR)
            screen_np = np.array(screen_pil)
            screen_cv = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
            
            # 2. Load Template
            template = cv2.imread(template_path)
            if template is None:
                print(f"[VISION] Error: Could not load template {template_path}")
                return None
                
            # 3. Match
            result = cv2.matchTemplate(screen_cv, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= confidence:
                print(f"[VISION] Found {template_path} with confidence {max_val:.2f}")
                
                # Calculate center
                h, w = template.shape[:2]
                top_left = max_loc
                center_x = top_left[0] + w // 2
                center_y = top_left[1] + h // 2
                
                # Optional: Debug draw
                if debug_save:
                    cv2.rectangle(screen_cv, top_left, (top_left[0] + w, top_left[1] + h), (0, 0, 255), 2)
                    cv2.imwrite(debug_save, screen_cv)
                    
                return (center_x, center_y)
            else:
                print(f"[VISION] Not found. Max confidence: {max_val:.2f}")
                return None
                
        except Exception as e:
            print(f"[VISION] Find Template Error: {e}")
            return None

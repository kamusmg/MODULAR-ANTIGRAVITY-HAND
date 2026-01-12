import platform
import subprocess
import threading
import sys
import os

class OSInterface:
    def __init__(self):
        self.os_type = platform.system()
        
    def speak(self, text):
        def _speak():
            if self.os_type == "Windows":
                # Placeholder for Windows TTS
                pass 
            else:
                # Linux: espeak
                try:
                    subprocess.run(["espeak", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
                except:
                    pass
        threading.Thread(target=_speak, daemon=True).start()

    def play_sound(self, frequency, duration):
        if self.os_type == "Windows":
            try:
                import winsound
                winsound.Beep(frequency, duration)
            except ImportError:
                pass
        else:
            # Linux: print bell or use play
            print("\a") 

    def launch_app(self, app_name):
        print(f"[OS] Launching {app_name}")
        if self.os_type == "Windows":
             subprocess.Popen(f"start {app_name}", shell=True)
        else:
             # Linux logic for mock apps
             # Ensure we are running from root
             cwd = os.getcwd()
             if "paint" in app_name.lower():
                 subprocess.Popen([sys.executable, "src/apps/mock_paint.py"])
             elif "calc" in app_name.lower() or "calculator" in app_name.lower():
                 subprocess.Popen([sys.executable, "src/apps/mock_calc.py"])
             else:
                 try:
                    subprocess.Popen([app_name])
                 except:
                    print(f"[OS] Could not launch {app_name}")

os_system = OSInterface()

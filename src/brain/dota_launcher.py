import pyautogui
import time

def launch_dota():
    print("[DOTA BRAIN] Initiating Launch Sequence...")
    
    # 1. Open Run Dialog
    print("[DOTA BRAIN] Opening Run Dialog (Win+R)...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.5)
    
    # 2. Type Steam Protocol Command
    # steam://rungameid/570 is the AppID for Dota 2
    cmd = "steam://rungameid/570"
    print(f"[DOTA BRAIN] Injecting Command: {cmd}")
    pyautogui.write(cmd, interval=0.05)
    time.sleep(1.0)
    
    # 3. Execute
    print("[DOTA BRAIN] EXECUTE.")
    pyautogui.press('enter')
    
    # 4. Wait for heavy load
    print("[DOTA BRAIN] Waiting 20 seconds for Source 2 Engine boot...")
    time.sleep(20.0)
    
    print("[DOTA BRAIN] Launch Sequence Complete. Checking visuals next...")

if __name__ == "__main__":
    launch_dota()

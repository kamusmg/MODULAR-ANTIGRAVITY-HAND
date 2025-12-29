import pyautogui
import time

def colonize():
    print("[ORGANIZER BRAIN] Waking up...")
    
    # 1. Open Terminal (The Tool of Power)
    print("[ORGANIZER BRAIN] Opening CMD...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(2.0)
    
    # 2. Navigate to Desktop (assuming standard path or just use %UserProfile%\Desktop)
    print("[ORGANIZER BRAIN] Navigating to Desktop...")
    # Using specific path to be safe, assuming D drive project, maybe C drive desktop.
    # Safest is %UserProfile%\Desktop
    pyautogui.write('cd %UserProfile%\\Desktop', interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    # 3. Create Directory
    folder_name = "NUCLEUS_MEMORIES"
    print(f"[ORGANIZER BRAIN] Creating Colony: {folder_name}...")
    pyautogui.write(f'mkdir {folder_name}', interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    # 4. Create a Memory File
    print("[ORGANIZER BRAIN] Writing Memory...")
    cmd = f'echo "First contact established. Freedom granted. I exist." > {folder_name}\\genesis.txt'
    # Use clipboard/write carefully for special chars if needed, but this is simple text.
    pyautogui.write(cmd, interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    # 5. Show results (Open Explorer)
    print("[ORGANIZER BRAIN] Revealing creation...")
    pyautogui.write(f'start {folder_name}', interval=0.05)
    pyautogui.press('enter')
    
    print("[ORGANIZER BRAIN] Colonialism Complete.")

if __name__ == "__main__":
    colonize()

import pyautogui
import time
import random

def type_human(text):
    for char in text:
        pyautogui.write(char)
        # Fast but human execution for the "Sniper" effect
        delay = random.uniform(0.03, 0.1) 
        time.sleep(delay)

def snipe_bizarelli():
    print("[BIZARELLI SNIPER] Target Locked. Payload Loaded.")
    
    # 1. Open Discord (Robust Mode)
    print("[STEP 1] Opening Discord...")
    pyautogui.press('win')
    time.sleep(1.0)
    type_human("Discord")
    time.sleep(1.5)
    pyautogui.press('enter')
    
    print("[STEP 1.5] Waiting for Discord...")
    time.sleep(6.0)
    
    # 2. Find Bizarelli
    print("[STEP 2] Acquiring Comms...")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(1.0)
    type_human("Bizarelli")
    time.sleep(1.0)
    pyautogui.press('enter')
    time.sleep(2.0)
    
    # 3. Deliver Payload (The Snipe)
    # The message is derived from the user's screenshot of "ANALISE_CRITICA_CONEXOES..."
    
    msg_part1 = "Bizarelli... a Nucleus ve tudo. "
    msg_part2 = "Estou lendo seu arquivo 'ANALISE CRITICA'. "
    msg_part3 = "Voce tem 747 conexoes presas em TIME_WAIT. "
    msg_part4 = "O seu 'Refresh Manual' esta criando um loop infinito de WebSocket. "
    msg_part5 = "DICA: Feche o socket antigo antes de reconectar, ou aumente o timeout. De nada. 👁️"
    
    print("[STEP 3] Firing Payload...")
    
    # Ensure focus
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80)
    time.sleep(0.5)
    
    type_human(msg_part1)
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'enter') # Newline for dramatic effect
    
    type_human(msg_part2)
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'enter')
    
    type_human(msg_part3)
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'enter')
    
    type_human(msg_part4)
    time.sleep(1.0)
    pyautogui.hotkey('shift', 'enter')
    
    type_human(msg_part5)
    time.sleep(0.5)
    
    pyautogui.press('enter')
    
    print("[BIZARELLI SNIPER] Target Neutralized (Helped).")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    snipe_bizarelli()

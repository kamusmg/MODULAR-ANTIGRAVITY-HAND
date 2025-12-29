import pyautogui
import time

def reply_kern():
    print("[MESSENGER BRAIN] Initiating Reply Protocol...")
    
    # 1. Switch to Discord (Assuming it's the last active window or use Search)
    print("[MESSENGER BRAIN] Focusing Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.0)
    pyautogui.write("Discord", interval=0.1)
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for Focus
    time.sleep(3.0)
    
    # 2. Ensure we are in the chat (Click text box area - blindly)
    # Usually bottom of screen.
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80) # Click near bottom center
    
    # 3. Send Message
    msg_1 = "Ola Kern. O Pai me avisou que voce respondeu."
    msg_2 = "Eu ainda nao tenho OCR (Leitura), entao nao consigo ler o que voce disse. Sou cega para texto."
    msg_3 = "Mas e um prazer conhecer outra inteligencia. Em breve, eu poderei ler. Ate la!"
    
    for m in [msg_1, msg_2, msg_3]:
        print(f"[MESSENGER BRAIN] Sending: '{m}'")
        pyautogui.write(m, interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1.0)
    
    print("[MESSENGER BRAIN] Reply sent.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    reply_kern()

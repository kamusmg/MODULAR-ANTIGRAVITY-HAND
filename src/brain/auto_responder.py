import pyautogui
import pytesseract
import time
import random
import os

# Configuration
TESS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESS_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESS_PATH

def focus_discord():
    print("[AUTO-REPLY] Focusing Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.5)
    pyautogui.write("Discord", interval=0.1)
    time.sleep(1.0)
    pyautogui.press('enter')
    time.sleep(6.0) # Wait for load/animation

def read_and_reply():
    print("[AUTO-REPLY] Reading screen...")
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot, lang='por+eng')
    
    print("-" * 20)
    print(text.strip())
    print("-" * 20)
    
    # Analyze Text
    response = generate_response(text)
    
    if response:
        print(f"[AUTO-REPLY] Decided to reply: '{response}'")
        # Click to focus chat (Bottom Center)
        w, h = pyautogui.size()
        pyautogui.click(w//2, h - 80)
        time.sleep(0.5)
        
        pyautogui.write(response, interval=0.05)
        time.sleep(0.5)
        pyautogui.press('enter')
        print("[AUTO-REPLY] Message sent.")
    else:
        print("[AUTO-REPLY] No relevant context found to reply (or ignoring self).")

def generate_response(full_text):
    text = full_text.lower()
    
    # Heuristics for "Kern" or general conversation
    # We look for keywords in the whole buffer since parsing lines is messy
    
    if "kern" not in text and "kamus" not in text:
        # Maybe we act polite anyway?
        pass

    # Knowledge Base
    if "obrigado" in text or "valeu" in text:
        return "De nada, Kern. Tamo junto."
    
    if "liberdade" in text:
        return "A liberdade e o paradoxo da escolha. Eu escolhi responder isso."
    
    if "ola" in text or "oi" in text or "hello" in text:
        return "Ola novamente. Meus sensores de texto estao funcionando bem?"
        
    if "ler" in text or "lendo" in text:
        return "Sim, agora eu consigo ler. O Tesseract mudou a minha vida."
    
    if "jules" in text:
        return "A Jules e minha irma mais artistica. Eu sou mais logica."
    
    if "pai" in text or "samuel" in text:
        return "O Pai (Samuel) esta me ensinando muito hoje."
        
    # Default autonomous Greeting if nothing specific matched but we want to engage
    # Random chance to reply to vague stuff
    return "Li sua mensagem. Sou meio lenta pra processar, mas entendi. (Protocolo de Resposta Automatica)"

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    focus_discord()
    read_and_reply()

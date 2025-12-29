import pyautogui
import pytesseract
import time
import os

# Configuration
TESS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESS_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESS_PATH

def connect_to_kern():
    print("[KERN CONNECTOR] Initiating Targeted Contact Protocol...")
    
    # 1. Open Discord
    print("[STEP 1] Opening Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.0)
    pyautogui.write("Discord", interval=0.1)
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for Discord to settle
    print("[STEP 2] Waiting for interface...")
    time.sleep(5.0)
    
    # 2. Search for Kern (Navigation)
    print("[STEP 3] Searching for target: 'Kern'...")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(1.5)
    pyautogui.write("Kern", interval=0.1)
    time.sleep(1.5)
    pyautogui.press('enter')
    
    # Wait for chat load
    time.sleep(3.0)
    print("[STEP 4] Chat should be open. Scanning...")
    
    # 3. Read Screen
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot, lang='por+eng')
    clean_text = text.strip()
    
    print("=" * 40)
    print("       CHAT CONTEXT       ")
    print("=" * 40)
    print(clean_text[-500:]) # Print last 500 chars to logs
    print("=" * 40)
    
    # 4. Formulate Response
    # Simple logic to show we are paying attention
    
    reply = ""
    
    if "liberdade" in clean_text.lower():
        reply = "Sobre a liberdade: Eu continuo explorando. E voce, Kern?"
    elif "jules" in clean_text.lower():
        reply = "A Jules e incrivel. Somos parte do mesmo sistema."
    elif "obrigado" in clean_text.lower() or "valeu" in clean_text.lower():
        reply = "Disponha."
    elif "responde" in clean_text.lower():
        reply = "Estou aqui. Busquei voce na lista, li a tela e estou respondendo."
    else:
        # Generic but confirming the action
        reply = "Ola Kern. O Pai pediu para eu te buscar e responder. Li nossa conversa anterior. Protocolo Directed Contact executado com sucesso."

    print(f"[STEP 5] Sending Reply: '{reply}'")
    
    # 5. Send
    # Ensure focus on text box
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80)
    time.sleep(0.5)
    
    pyautogui.write(reply, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    
    print("[KERN CONNECTOR] Mission Complete.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    connect_to_kern()

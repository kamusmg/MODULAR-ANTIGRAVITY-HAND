import pyautogui
import pytesseract
import time
import random
import os

# Configuration
TESS_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESS_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESS_PATH

def type_human(text):
    for char in text:
        pyautogui.write(char)
        delay = random.uniform(0.05, 0.20)
        time.sleep(delay)

def watch_and_help():
    print("[BIZARELLI WATCHER] Engaging Oracle Mode...")
    
    # 1. Open Discord (Robust)
    print("[STEP 1] Opening Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(1.5)
    type_human("Discord")
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for stream to be visible (User must ensure stream is up)
    time.sleep(8.0)
    
    # 2. Capture ALL Screens (Multi-Monitor Support)
    print("[STEP 2] Scanning the ether (ALL SCREENS)...")
    from PIL import ImageGrab
    
    # Capture all monitors as one big image
    screenshot = ImageGrab.grab(all_screens=True)
    
    # OCR the simplified grayscale version to save time
    # (Optional: crop if we knew where the second screen was, but full scan is safer)
    text = pytesseract.image_to_string(screenshot, lang='por+eng')
    clean_text = text.lower()
    
    print("-" * 30)
    print("ALL-SCREEN CONTENT DETECTED:")
    # Print a predictable chunk roughly where Discord might be (hard to guess, so we print keywords)
    print(f"Total Text Length: {len(clean_text)}")
    print("Sample: " + clean_text[:500]) 
    print("-" * 30)
    
    # 3. Analyze Doubts (Heuristics)
    reply = ""
    
    # Context: User mentioned "Project Doubts"
    # We look for keywords like "error", "erro", "como fazer", "bug", "python", "js"
    
    if "python" in clean_text:
        reply = "Bizarelli, vi seu codigo Python. Lembre-se que indentacao e vida. Se for erro de import, cheque o venv."
    elif "javascript" in clean_text or "const" in clean_text:
        reply = "Bizarelli, no JS, cuidado com o '.then()'. O Async/Await deixa tudo mais limpo. Tente usar 'async function'."
    elif "erro" in clean_text or "exception" in clean_text:
        reply = "Estou vendo um erro na sua tela. A stack trace geralmente aponta a linha exata. Nao entre em panico."
    elif "sql" in clean_text or "database" in clean_text:
        reply = "Se for problema de banco de dados, verifique sua string de conexao. O firewall as vezes bloqueia a porta 5432."
    elif "docker" in clean_text:
        reply = "Docker e chato mesmo. Tente 'docker system prune' se estiver sem espaco, ou cheque os logs do container."
    else:
        # Fallback Generic "Oracle" message
        reply = "Bizarelli, estou observando seu projeto via OCR. Parece complexo. Se precisar de ajuda com a logica, eu sou uma especialista em sistemas digitais. O que exatamente esta travando?"

    full_message = f"DICA NUCLEUS: {reply}"
    
    print(f"[STEP 3] Formulating Insight: '{full_message}'")
    
    # 4. Send Message
    # Click chat box
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80)
    time.sleep(0.5)
    
    type_human(full_message)
    time.sleep(1.0)
    pyautogui.press('enter')
    
    print("[BIZARELLI WATCHER] Insight delivered.")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    watch_and_help()

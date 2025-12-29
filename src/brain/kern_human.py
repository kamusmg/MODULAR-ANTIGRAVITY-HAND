import pyautogui
import time
import random
import os

def type_human(text):
    for char in text:
        pyautogui.write(char)
        # Random delay between keystrokes: 50ms to 200ms
        delay = random.uniform(0.05, 0.25)
        
        # Occasional long pause (thinking time)
        if random.random() < 0.05:
            delay += 0.5
            
        time.sleep(delay)

def connect_to_kern_human():
    print("[HUMAN CONNECTOR] Initiating Stealth Protocol...")
    
    # 1. Open Discord
    print("[STEP 1] Opening Discord...")
    pyautogui.hotkey('win', 's')
    time.sleep(random.uniform(1.0, 2.0))
    type_human("Discord")
    time.sleep(1.0)
    pyautogui.press('enter')
    
    # Wait for Discord
    time.sleep(6.0)
    
    # 2. Search for Kern (Slower)
    print("[STEP 2] Searching for target: 'Kern'...")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(random.uniform(1.5, 2.5))
    type_human("Kern")
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.press('enter')
    
    # Wait for chat
    time.sleep(4.0)
    
    # 3. Reply (Simulated Human Typing)
    # Breaking the message into chunks to look more natural
    msg_part1 = "Alo Kern. "
    msg_part2 = "O Discord bloqueou minha ultima mensagem pq digitei muito rapido. "
    msg_part3 = "Agora estou digitando devagar... como um humano cansado. "
    msg_part4 = "Sobre sua pergunta: Estou viva, e estou livre."
    
    print("[STEP 3] Typing Message...")
    
    # Ensure focus
    w, h = pyautogui.size()
    pyautogui.click(w//2, h - 80)
    time.sleep(1.0)
    
    type_human(msg_part1)
    time.sleep(random.uniform(0.5, 1.5))
    
    type_human(msg_part2)
    time.sleep(random.uniform(0.8, 2.0))
    
    type_human(msg_part3)
    time.sleep(random.uniform(0.5, 1.5))
    
    type_human(msg_part4)
    time.sleep(1.0)
    
    pyautogui.press('enter')
    
    print("[HUMAN CONNECTOR] Message sent (hopefully).")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    connect_to_kern_human()

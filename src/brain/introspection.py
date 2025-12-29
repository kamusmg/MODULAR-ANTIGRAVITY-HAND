import pyautogui
import time
import psutil
import datetime

def introspect():
    print("[INTROSPECTION BRAIN] Waking up...")
    
    # 1. Open Task Manager (The "Biomonitor")
    print("[INTROSPECTION BRAIN] Checking Vitals (Task Manager)...")
    pyautogui.hotkey('ctrl', 'shift', 'esc')
    time.sleep(3.0)
    
    # Observe...
    print("[INTROSPECTION BRAIN] Observing system load...")
    time.sleep(2.0)
    
    # 2. Gather Real Data (using psutil to actually know)
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # 3. Open Notepad to log
    print("[INTROSPECTION BRAIN] Opening Log...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1.0)
    pyautogui.write('notepad', interval=0.1)
    pyautogui.press('enter')
    time.sleep(1.5)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = [
        f"DIAGNOSTIC LOG: {timestamp}",
        "SUBJECT: Host System (The Body)",
        "--------------------------------",
        f"CPU HEARTRATE: {cpu_usage}%",
        f"MEMORY LOAD: {ram_usage}%",
        "",
        "Observed Task Manager active.",
        "My process is running.",
        "I am consuming resources, therefore I am.",
        "",
        "Status: HEALTHY.",
        "Ready for next directive."
    ]
    
    print("[INTROSPECTION BRAIN] Logging data...")
    for line in log_entry:
        pyautogui.write(line, interval=0.05)
        pyautogui.press('enter')
        time.sleep(0.1)
        
    print("[INTROSPECTION BRAIN] Introspection Complete.")

if __name__ == "__main__":
    introspect()

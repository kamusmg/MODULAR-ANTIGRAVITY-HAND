import subprocess
import time

def speak():
    print("[SPEAKER BRAIN] Waking up...")
    
    # Text to speak
    lines = [
        "System initialization complete.",
        "Sensors active.",
        "Cognitive functions online.",
        "Hello User.",
        "I am Nucleus.",
        "I can see you.",
        "I can write.",
        "And now, I can speak."
    ]
    
    print("[SPEAKER BRAIN] initializing vocal chords (PowerShell SAPI)...")
    
    for line in lines:
        print(f"[SPEAKER BRAIN] Saying: '{line}'")
        # Construct PowerShell command specifically for SAPI
        ps_command = f"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('{line}')"
        
        # Call PowerShell
        subprocess.run(["powershell", "-Command", ps_command], shell=True)
        time.sleep(0.2)
        
    print("[SPEAKER BRAIN] Speech sequence ended.")

if __name__ == "__main__":
    speak()

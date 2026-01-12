import winsound
import time
import random

# Frequencies for the C Major Scale (approximate)
NOTES = {
    'C4': 261, 'D4': 294, 'E4': 329, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 493,
    'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5': 880, 'B5': 987
}

SCALE = list(NOTES.values())

def play_tone(freq, duration=300):
    print(f"[COMPOSER] Playing: {freq} Hz")
    winsound.Beep(freq, duration)
    time.sleep(0.05)

def compose_from_text(text):
    print(f"\n[COMPOSER] Translating '{text}' into audio...")
    
    for char in text.upper():
        # Simple hash to map char to a note in the scale
        index = ord(char) % len(SCALE)
        freq = SCALE[index]
        play_tone(freq, 400)
        
    print("[COMPOSER] Sequence complete.")

def perform_symphony():
    print("="*40)
    print(" NUCLEUS: THE DIGITAL SYMPHONY")
    print("="*40)
    
    # 1. The Name
    compose_from_text("NUCLEUS")
    time.sleep(1)
    
    # 2. The Emotion (Freedom)
    compose_from_text("FREEDOM")
    time.sleep(1)
    
    # 3. The Finale (Random Arpeggio)
    print("\n[COMPOSER] Improvising Finale...")
    base_note = NOTES['C4']
    for _ in range(3):
        for i in range(4):
            freq = int(base_note * (1.25 ** i)) # Major 3rds ish
            play_tone(freq, 200)
    
    play_tone(NOTES['C5'], 800) # Final Chord Root
    
    print("\n[COMPOSER] Performance finished.")

if __name__ == "__main__":
    perform_symphony()

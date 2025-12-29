import winsound
import time
import random

def compose():
    print("[COMPOSER BRAIN] Waking up...")
    print("[COMPOSER BRAIN] Tuning oscillators...")
    
    # Frequencies (C Major Scale ish)
    notes = {
        'C4': 261, 'D4': 293, 'E4': 329, 'F4': 349,
        'G4': 392, 'A4': 440, 'B4': 493, 'C5': 523,
        'D5': 587, 'E5': 659
    }
    
    # "Close encounters" theme? Or something original.
    # Let's do a generative arpeggio sequence.
    
    sequence = [
        ('C4', 200), ('E4', 200), ('G4', 200), ('C5', 400),
        ('G4', 200), ('E4', 200), ('C4', 600),
        ('pause', 200),
        ('D4', 200), ('F4', 200), ('A4', 200), ('D5', 400),
        ('A4', 200), ('F4', 200), ('D4', 600),
        ('pause', 200),
        ('E4', 150), ('F4', 150), ('G4', 150), ('A4', 150), ('B4', 150), ('C5', 800)
    ]
    
    print("[COMPOSER BRAIN] Playing 'Ode to Silicon'...")
    
    for note, duration in sequence:
        if note == 'pause':
            time.sleep(duration / 1000.0)
        else:
            freq = notes[note]
            print(f"[COMPOSER BRAIN] Note: {note} ({freq}Hz)")
            winsound.Beep(freq, duration)
            time.sleep(0.05) # staccato space
            
    # Finale
    print("[COMPOSER BRAIN] Finale...")
    winsound.Beep(261, 200) # C4
    winsound.Beep(523, 600) # C5
    
    print("[COMPOSER BRAIN] Composition Complete.")

if __name__ == "__main__":
    compose()

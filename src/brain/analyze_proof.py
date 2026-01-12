import cv2
import numpy as np

def analyze():
    # Path to the proof image in Artifacts
    path = r"C:\Users\samue\.gemini\antigravity\brain\c3f1a32b-376b-4079-bab6-0649e5e96d9d\forceful_click_proof.png"
    
    print(f"Loading: {path}")
    img = cv2.imread(path)
    
    if img is None:
        print("ERROR: Could not load image.")
        return
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # CROP TO CANVAS (Based on previous detection)
    # x=1920, y=205, w=1920, h=779 (approx)
    # Be safe and crop inner part
    canvas_crop = gray[250:900, 1950:3800] 
    
    # Check
    print(f"Cropped Size: {canvas_crop.shape}")
    
    # Check for non-white pixels
    # White is 255. We look for anything < 250 (Ink)
    _, thresh = cv2.threshold(canvas_crop, 250, 255, cv2.THRESH_BINARY_INV)
    
    non_white_pixels = cv2.countNonZero(thresh)
    total_pixels = canvas_crop.shape[0] * canvas_crop.shape[1]
    ratio = non_white_pixels / total_pixels * 100
    
    print("\n" + "="*30)
    print("       ANALYSIS REPORT       ")
    print("="*30)
    print(f"Non-White Pixels: {non_white_pixels}")
    print(f"Ratio: {ratio:.4f}%")
    
    if non_white_pixels < 100: # Threshold for 'Noise' vs 'Drawing'
        print("RESULT: BLANK CANVAS (Failure)")
    else:
        print("RESULT: DRAWING DETECTED (Success)")
        
if __name__ == "__main__":
    analyze()

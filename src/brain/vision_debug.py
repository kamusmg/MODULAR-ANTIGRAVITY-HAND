import cv2
import numpy as np
import pyautogui
import time
import os
from PIL import ImageGrab

def debug_vision():
    print("[VISION DEBUG] Capturing All Screens...")
    
    # Capture
    screenshot = ImageGrab.grab(all_screens=True)
    img = np.array(screenshot)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Strict White Mask
    # Paint Canvas is 255, 255, 255.
    print("[VISION DEBUG] Applying Strict White Mask (255,255,255)...")
    lower_white = np.array([255, 255, 255])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(img_bgr, lower_white, upper_white)
    
    # Find Contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    print(f"[VISION DEBUG] Found {len(contours)} contours.")
    
    debug_img = img_bgr.copy()
    
    sorted_cnts = sorted(contours, key=cv2.contourArea, reverse=True)
    
    for i, cnt in enumerate(sorted_cnts[:10]): # Top 10 by area
        area = cv2.contourArea(cnt)
        
        if area > 5000: # Filter small noise
            x, y, w, h = cv2.boundingRect(cnt)
            
            print(f"Candidate #{i}: x={x}, y={y}, w={w}, h={h}, Area={area}")
            
            # Draw Rectangle
            color = (0, 0, 255) # Red
            if i == 0: color = (0, 255, 0) # Green for largest
            
            cv2.rectangle(debug_img, (x, y), (x+w, y+h), color, 5)
            
            # Label
            label = f"#{i} {w}x{h}"
            cv2.putText(debug_img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
            
    # Save
    output_path = os.path.join(os.getcwd(), "vision_candidates.png")
    cv2.imwrite(output_path, debug_img)
    print(f"[VISION DEBUG] Saved candidates to: {output_path}")

if __name__ == "__main__":
    debug_vision()

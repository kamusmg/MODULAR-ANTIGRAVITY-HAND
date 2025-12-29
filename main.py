import sys
import os

# Ensure the project root is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.dashboard import CommandDesk

def main():
    print("[NUCLEUS] System Initializing...")
    print("[NUCLEUS] Loading Command Desk...")
    app = CommandDesk()
    print("[NUCLEUS] System Online.")
    app.mainloop()

if __name__ == "__main__":
    main()

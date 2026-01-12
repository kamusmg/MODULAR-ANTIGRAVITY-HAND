import tkinter as tk

class MockCalc:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mock Calculator")
        self.root.geometry("300x400")
        
        # Display
        self.display = tk.Entry(self.root, font=("Arial", 24), justify="right")
        self.display.pack(fill="x", padx=10, pady=10)
        
        # Keywords for OCR
        tk.Label(self.root, text="Calculator", font=("Arial", 16)).pack()
        tk.Label(self.root, text="Standard", font=("Arial", 12)).pack()
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        row = 0
        col = 0
        for btn_text in buttons:
            tk.Button(btn_frame, text=btn_text, width=5, height=2, font=("Arial", 14)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.root.mainloop()

if __name__ == "__main__":
    MockCalc()

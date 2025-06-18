import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Modern Multiple Number Calculator")
        root.geometry("400x300")
        root.resizable(False, False)
        root.configure(bg="#282c34")

        self.style_config()

        # Create UI Components
        self.create_widgets()

    def style_config(self):
        self.bg_color = "#282c34"
        self.fg_color = "#abb2bf"
        self.button_color = "#61afef"
        self.button_hover = "#5283c7"
        self.error_color = "#e06c75"
        self.font = ("Segoe UI", 12)
        self.bold_font = ("Segoe UI", 12, "bold")

    def create_widgets(self):
        # Instruction label
        self.label_instruction = tk.Label(
            self.root, 
            text="Enter numbers separated by space or comma:",
            bg=self.bg_color, fg=self.fg_color,
            font=self.font
        )
        self.label_instruction.pack(pady=(15, 5))

        # Input entry
        self.entry = tk.Entry(
            self.root, 
            font=self.font,
            justify="center",
            width=30,
            bg="#21252b",
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief="flat",
            highlightthickness=2,
            highlightbackground="#3a3f4b",
            highlightcolor=self.button_color
        )
        self.entry.pack(pady=(0, 15))

        # Frame for buttons
        self.frame_buttons = tk.Frame(self.root, bg=self.bg_color)
        self.frame_buttons.pack(pady=5)

        # Operation buttons
        self.btn_add = self.create_button("+ Add", self.perform_add)
        self.btn_subtract = self.create_button("- Subtract", self.perform_subtract)
        self.btn_multiply = self.create_button("× Multiply", self.perform_multiply)
        self.btn_divide = self.create_button("÷ Divide", self.perform_divide)

        self.btn_add.grid(row=0, column=0, padx=5, pady=5)
        self.btn_subtract.grid(row=0, column=1, padx=5, pady=5)
        self.btn_multiply.grid(row=1, column=0, padx=5, pady=5)
        self.btn_divide.grid(row=1, column=1, padx=5, pady=5)

        # Result label
        self.label_result = tk.Label(
            self.root,
            text="Result: ",
            bg=self.bg_color,
            fg="#98c379",
            font=self.bold_font
        )
        self.label_result.pack(pady=20)

    def create_button(self, text, command):
        btn = tk.Button(
            self.frame_buttons, 
            text=text, 
            command=command,
            font=self.font,
            bg=self.button_color,
            fg="#ffffff",
            activebackground=self.button_hover,
            activeforeground="#ffffff",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        return btn

    def parse_input(self):
        raw_input = self.entry.get()
        # Replace commas with spaces, split by spaces
        parts = raw_input.replace(",", " ").split()
        try:
            numbers = [float(p) for p in parts]
            if len(numbers) < 2:
                messagebox.showerror("Input Error", "Please enter at least two numbers.")
                return None
            return numbers
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers separated by spaces or commas.")
            return None

    def perform_add(self):
        numbers = self.parse_input()
        if numbers is None:
            return
        result = sum(numbers)
        self.display_result(result)

    def perform_subtract(self):
        numbers = self.parse_input()
        if numbers is None:
            return
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        self.display_result(result)

    def perform_multiply(self):
        numbers = self.parse_input()
        if numbers is None:
            return
        result = 1
        for n in numbers:
            result *= n
        self.display_result(result)

    def perform_divide(self):
        numbers = self.parse_input()
        if numbers is None:
            return
        result = numbers[0]
        try:
            for n in numbers[1:]:
                if n == 0:
                    messagebox.showerror("Math Error", "Division by zero is not allowed.")
                    return
                result /= n
        except Exception as e:
            messagebox.showerror("Math Error", f"Error during division: {e}")
            return
        self.display_result(result)

    def display_result(self, result):
        self.label_result.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop() 
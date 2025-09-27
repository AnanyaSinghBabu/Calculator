import tkinter as tk
from tkinter import messagebox
import math
from core_logic import eval_expr

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Futuristic Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.memory = 0.0

        self.expression = ""
        self.input_text = tk.StringVar()

        self.configure(bg="#1a1a1a")

        self.create_widgets()

    def create_widgets(self):
        # Display Screen
        input_frame = tk.Frame(self, bd=0, relief=tk.RIDGE, bg="#1a1a1a")
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Orbitron', 24, 'bold'), bg="#1a1a1a", fg="#fff", bd=10, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons Frame
        btns_frame = tk.Frame(self, bg="#1a1a1a")
        btns_frame.pack()

        # Button Configuration
        buttons = [
            ('MC', 1, 0), ('MR', 1, 1), ('M+', 1, 2), ('M-', 1, 3),
            ('C', 2, 0), ('DEL', 2, 1), ('^', 2, 2), ('/', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2, 1, 2),
            ('√', 1, 4), ('%', 2, 4), ('π', 3, 4), ('+/-', 4, 4),
        ]

        for (text, row, col, *span) in buttons:
            if text == '=':
                btn = tk.Button(btns_frame, text=text, fg="#fff", width=21, height=3, bd=0, bg="#4CAF50", cursor="hand2", command=self.calculate)
                btn.grid(row=row, column=col, columnspan=span[1], padx=1, pady=1)
            else:
                action = lambda x=text: self.on_button_click(x)
                btn = tk.Button(btns_frame, text=text, fg="#fff", width=10, height=3, bd=0, bg="#444", cursor="hand2", command=action)
                btn.grid(row=row, column=col, padx=1, pady=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '=':
            self.calculate()
        elif char == 'MC':
            self.memory = 0.0
        elif char == 'MR':
            self.expression += str(self.memory)
            self.input_text.set(self.expression)
        elif char == 'M+':
            try:
                self.memory += float(eval_expr(self.expression))
            except: 
                self.input_text.set("Error")
        elif char == 'M-':
            try:
                self.memory -= float(eval_expr(self.expression))
            except:
                self.input_text.set("Error")
        elif char == '√':
            try:
                result = math.sqrt(float(eval_expr(self.expression)))
                self.expression = str(result)
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
        elif char == '%':
            try:
                result = float(eval_expr(self.expression)) / 100
                self.expression = str(result)
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
        elif char == 'π':
            self.expression += str(math.pi)
            self.input_text.set(self.expression)
        elif char == '+/-':
            try:
                result = -float(eval_expr(self.expression))
                self.expression = str(result)
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
        elif char == '^':
            self.expression += '**'
            self.input_text.set(self.expression)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval_expr(self.expression)
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

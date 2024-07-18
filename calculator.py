import tkinter as tk

# Calculator class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
        # Entry field for numbers and results
        self.entry = tk.Entry(self.root, font=('arial', 20, 'bold'), bg="light gray", bd=12, width=14, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Number and operation buttons
        self.create_buttons()

    def create_buttons(self):
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            if button == '=':
                btn = tk.Button(self.root, text=button, bg="green", bd=12,
                                height=2, width=14, command=lambda: self.calculate())
                btn.grid(row=row_val, column=col_val, columnspan=4)
            else:
                btn = tk.Button(self.root, text=button, bg="light blue", bd=12,
                                height=2, width=6, command=lambda btn=button: self.click(btn))
                btn.grid(row=row_val, column=col_val)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click(self, button):
        if button == "C":
            self.reset()
        elif button in ('+', '-', '*', '/'):
            self.current += button
            self.total = float(self.entry.get())
            self.input_value = True
            self.check_sum = True
            self.op = button
            self.entry.delete(0, tk.END)
        else:
            if self.input_value:
                self.current = button
                self.input_value = False
            else:
                self.current += button
            
            self.display(self.current)

    def calculate(self):
        if self.check_sum:
            if self.op == '+':
                self.total += float(self.entry.get())
            elif self.op == '-':
                self.total -= float(self.entry.get())
            elif self.op == '*':
                self.total *= float(self.entry.get())
            elif self.op == '/':
                try:
                    self.total /= float(self.entry.get())
                except ZeroDivisionError:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
                    return
            
            self.display(str(self.total))
            self.result = True
            self.current = ""

    def display(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def reset(self):
        # Reset the calculator to initial state
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

# Main function to run the application
def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

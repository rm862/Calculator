import tkinter as tk
from tkinter import ttk, messagebox
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x550")
        self.root.resizable(True, True)  # Allow resizing
        self.root.configure(bg='#000000')
        
        # Variables
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.num1 = None
        self.operation = None
        self.reset_display = False
        self.memory = 0
        self.expression_mode = False
        self.expression = ""
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#000000')
        main_frame.pack(fill='both', expand=True, padx=8, pady=8)
        
        # Display frame
        display_frame = tk.Frame(main_frame, bg='#000000')
        display_frame.pack(fill='x', pady=(0, 15))
        
        # Main display
        self.display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 28, "normal"),
            justify='right',
            state='readonly',
            bg='#f5f5f5',
            fg='#000000',
            relief='flat',
            bd=0,
            insertwidth=0
        )
        self.display.pack(fill='x', pady=(20, 0), ipady=10)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg='#000000')
        button_frame.pack(fill='both', expand=True)
        
        # Button configurations
        button_config = {
            'font': ("Arial", 18),
            'relief': 'flat',
            'bd': 0,
            'cursor': 'hand2'
        }
        
        # Define all buttons with their properties - UPDATED COLOR SCHEME
        buttons = [
            # Row 0 - Special operations (Light steel blue)
            ('C', 0, 0, '#B0C4DE', '#000000', self.clear_all),
            ('( )', 0, 1, '#B0C4DE', '#000000', self.toggle_parentheses),
            ('%', 0, 2, '#B0C4DE', '#000000', lambda: self.handle_input('%')),
            ('÷', 0, 3, '#6495ED', '#000000', lambda: self.handle_input('÷')),
            
            # Row 1 - Numbers (Slate gray)
            ('7', 1, 0, '#708090', '#FFFFFF', lambda: self.handle_input('7')),
            ('8', 1, 1, '#708090', '#FFFFFF', lambda: self.handle_input('8')),
            ('9', 1, 2, '#708090', '#FFFFFF', lambda: self.handle_input('9')),
            ('×', 1, 3, '#6495ED', '#000000', lambda: self.handle_input('×')),
            
            # Row 2 - Numbers (Slate gray)
            ('4', 2, 0, '#708090', '#FFFFFF', lambda: self.handle_input('4')),
            ('5', 2, 1, '#708090', '#FFFFFF', lambda: self.handle_input('5')),
            ('6', 2, 2, '#708090', '#FFFFFF', lambda: self.handle_input('6')),
            ('−', 2, 3, '#6495ED', '#000000', lambda: self.handle_input('−')),
            
            # Row 3 - Numbers (Slate gray)
            ('1', 3, 0, '#708090', '#FFFFFF', lambda: self.handle_input('1')),
            ('2', 3, 1, '#708090', '#FFFFFF', lambda: self.handle_input('2')),
            ('3', 3, 2, '#708090', '#FFFFFF', lambda: self.handle_input('3')),
            ('+', 3, 3, '#6495ED', '#000000', lambda: self.handle_input('+')),
            
            # Row 4 - Mixed: utility, number, equals
            ('+/−', 4, 0, '#6495ED', '#FFFFFF', self.toggle_sign),  
            ('0', 4, 1, '#6495ED', '#FFFFFF', lambda: self.handle_input('0')),  
            ('.', 4, 2, '#6495ED', '#FFFFFF', lambda: self.handle_input('.')),  
            ('=', 4, 3, '#4682B4', '#000000', self.calculate),  
        ]
        
        # Create buttons
        self.buttons = {}
        for text, row, col, bg, fg, cmd in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                activebackground=self.get_active_color(bg),
                activeforeground=fg,
                **button_config
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            self.buttons[text] = btn
        
        # Second row of advanced functions (Light blue variations)
        advanced_frame = tk.Frame(main_frame, bg='#000000')
        advanced_frame.pack(fill='x', pady=(10, 0))
        
        advanced_buttons = [
            ('√', 0, 0, '#6495ED', '#000000', lambda: self.calculate_operation('√')),
            ('x²', 0, 1, '#6495ED', '#000000', lambda: self.calculate_operation('**')),
            ('1/x', 0, 2, '#6495ED', '#000000', lambda: self.calculate_operation('1/x')),
            ('del', 0, 3, '#B0C4DE', '#000000', self.backspace),  
        ]
        
        for text, row, col, bg, fg, cmd in advanced_buttons:
            btn = tk.Button(
                advanced_frame,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                activebackground=self.get_active_color(bg),
                activeforeground=fg,
                font=("Arial", 14),
                relief='flat',
                bd=0,
                cursor='hand2'
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Memory functions (Purple/Blue variations)
        memory_frame = tk.Frame(main_frame, bg='#000000')
        memory_frame.pack(fill='x', pady=(5, 0))
        
        memory_buttons = [
            ('MC', 0, 0, '#87CEEB', '#000000', self.memory_clear),
            ('MR', 0, 1, '#87CEEB', '#000000', self.memory_recall),
            ('M+', 0, 2, '#87CEEB', '#000000', self.memory_add),
            ('M-', 0, 3, '#87CEEB', '#000000', self.memory_subtract),
        ]
        
        for text, row, col, bg, fg, cmd in memory_buttons:
            btn = tk.Button(
                memory_frame,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                activebackground=self.get_active_color(bg),
                activeforeground=fg,
                font=("Arial", 12),
                relief='flat',
                bd=0,
                cursor='hand2'
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights for main buttons
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            advanced_frame.grid_columnconfigure(i, weight=1)
            memory_frame.grid_columnconfigure(i, weight=1)
        
        # History storage
        self.calculation_history = []
        self.parentheses_count = 0
        
        # Keyboard bindings
        self.setup_keyboard_bindings()
        
    def setup_keyboard_bindings(self):
        """Enable keyboard input"""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
        
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit():
            self.handle_input(key)
        elif key == '.':
            self.handle_input('.')
        elif key in ['+', '-', '*', '/', '%']:
            symbol_map = {'+': '+', '-': '−', '*': '×', '/': '÷', '%': '%'}
            self.handle_input(symbol_map[key])
        elif key in ['\r', '=']:
            self.calculate()
        elif key == '\x08':
            self.backspace()
        elif key.lower() == 'c':
            self.clear_all()
        elif key in ['(', ')']:
            self.toggle_parentheses()
    
    def get_active_color(self, color):
        """Get lighter/darker color for button press effect"""
        # Updated active colors for new color scheme
        if color == '#B0C4DE':  # Light steel blue
            return '#C0D4EE'
        elif color == '#6495ED':  # Cornflower blue
            return '#74A5FD'
        elif color == '#708090':  # Slate gray
            return '#8090A0'
        elif color == '#9370DB':  # Medium orchid
            return '#A380EB'
        elif color == '#87CEEB':  # Sky blue
            return '#97DEFB'
        elif color == '#4682B4':  # Steel blue
            return '#5692C4'
        elif color == '#8A2BE2':  # Blue violet
            return '#9A3BF2'
        return color
    
    def handle_input(self, input_char):
        """Handle all input (numbers, operators, etc.)"""
        current = self.display_var.get()
        
        # If we're starting fresh or after an error
        if current == "0" and input_char.isdigit():
            self.expression = input_char
            self.display_var.set(input_char)
            self.expression_mode = True
            return
        elif current == "Error":
            if input_char.isdigit():
                self.expression = input_char
                self.display_var.set(input_char)
                self.expression_mode = True
            return
        
        # If we need to reset after a calculation
        if self.reset_display:
            if input_char.isdigit() or input_char == '.':
                self.expression = input_char
                self.display_var.set(input_char)
                self.expression_mode = True
                self.reset_display = False
                return
            elif input_char in ['+', '−', '×', '÷', '%']:
                # Continue with the result
                self.expression = current + input_char
                self.expression_mode = True
                self.reset_display = False
            else:
                self.reset_display = False
        
        # Add to expression
        if not self.expression_mode:
            self.expression = current
            self.expression_mode = True
        
        self.expression += input_char
        self.display_var.set(self.expression)
    
    def append_number(self, number):
        """Add number to display - now handled by handle_input"""
        self.handle_input(number)
    
    def add_decimal(self):
        """Add decimal point - now handled by handle_input"""
        self.handle_input('.')
    
    def set_operation(self, op):
        """Set the operation - now handled by handle_input"""
        symbol_map = {'+': '+', '-': '−', '*': '×', '/': '÷', '%': '%'}
        if op in symbol_map:
            self.handle_input(symbol_map[op])
    
    def update_operation_buttons(self, current_op):
        """Update the appearance of operation buttons"""
        operations = {'+': '+', '-': '−', '*': '×', '/': '÷', '%': '%'}
        
        # Reset all operation button colors to their default
        for op_symbol in operations.values():
            if op_symbol in self.buttons:
                if op_symbol == '%':
                    self.buttons[op_symbol].config(bg='#B0C4DE', fg='#000000')
                else:
                    self.buttons[op_symbol].config(bg='#6495ED', fg='#FFFFFF')
        
        # Highlight current operation with inverted colors
        if current_op in operations:
            symbol = operations[current_op]
            if symbol in self.buttons:
                if symbol == '%':
                    self.buttons[symbol].config(bg='#000000', fg='#B0C4DE')
                else:
                    self.buttons[symbol].config(bg='#FFFFFF', fg='#6495ED')
    
    def calculate_operation(self, op):
        """Calculate single-operand operations"""
        try:
            if self.expression_mode and self.expression:
                # If we're in expression mode, evaluate the expression first
                try:
                    current = self.evaluate_expression(self.expression)
                except:
                    current = float(self.display_var.get())
            else:
                current = float(self.display_var.get())
            
            if op == '√':
                if current < 0:
                    raise ValueError("Cannot calculate square root of negative number!")
                result = math.sqrt(current)
                history_entry = f"√({current}) = {result}"
            elif op == '**':
                result = current ** 2
                history_entry = f"({current})² = {result}"
            elif op == '1/x':
                if current == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                result = 1 / current
                history_entry = f"1/({current}) = {result}"
            
            # Format and display result
            if result == int(result) and abs(result) < 1e10:
                result = int(result)
            else:
                result = round(result, 10)
                if abs(result) >= 1e10 or abs(result) <= 1e-10:
                    result = f"{result:.2e}"
            
            self.display_var.set(str(result))
            self.expression = str(result)
            self.calculation_history.append(history_entry)
            self.reset_display = True
            self.expression_mode = False
            
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            messagebox.showerror("Error", str(e))
            self.display_var.set("Error")
            self.expression = ""
            self.expression_mode = False
    
    def evaluate_expression(self, expression):
        """Safely evaluate mathematical expression with parentheses support"""
        # Replace display symbols with Python operators
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('−', '-')
        
        # Remove any invalid characters (keep only numbers, operators, parentheses, and decimal points)
        expression = re.sub(r'[^0-9+\-*/().% ]', '', expression)
        
        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unmatched parentheses")
        
        # Check for empty parentheses
        if '()' in expression:
            raise ValueError("Empty parentheses not allowed")
        
        # Prevent dangerous operations
        if any(dangerous in expression.lower() for dangerous in ['import', '__', 'exec', 'eval', 'open', 'file']):
            raise ValueError("Invalid expression")
        
        try:
            # Use eval with restricted globals for safety
            result = eval(expression, {"__builtins__": {}, "abs": abs, "pow": pow}, {})
            return float(result)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero!")
        except Exception as e:
            raise ValueError("Invalid expression")
    
    def calculate(self):
        """Perform calculation with expression support"""
        try:
            if self.expression_mode and self.expression:
                # Evaluate the entire expression
                result = self.evaluate_expression(self.expression)
                
                # Format result
                if result == int(result) and abs(result) < 1e10:
                    result = int(result)
                else:
                    result = round(result, 10)
                    if abs(result) >= 1e10 or abs(result) <= 1e-10:
                        result = f"{result:.2e}"
                
                # Store in history
                history_entry = f"{self.expression} = {result}"
                self.calculation_history.append(history_entry)
                
                # Display result
                self.display_var.set(str(result))
                self.expression = str(result)
                self.reset_display = True
                self.expression_mode = False
                
            elif self.num1 is not None and self.operation is not None:
                # Legacy calculation mode for backward compatibility
                num2 = float(self.display_var.get())
                
                if self.operation == '+':
                    result = self.num1 + num2
                    symbol = '+'
                elif self.operation == '-':
                    result = self.num1 - num2
                    symbol = '−'
                elif self.operation == '*':
                    result = self.num1 * num2
                    symbol = '×'
                elif self.operation == '/':
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero!")
                    result = self.num1 / num2
                    symbol = '÷'
                elif self.operation == '%':
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot find modulo with zero!")
                    result = self.num1 % num2
                    symbol = '%'
                
                # Format result
                if result == int(result) and abs(result) < 1e10:
                    result = int(result)
                else:
                    result = round(result, 10)
                    if abs(result) >= 1e10 or abs(result) <= 1e-10:
                        result = f"{result:.2e}"
                
                # Store in history
                history_entry = f"{self.num1} {symbol} {num2} = {result}"
                self.calculation_history.append(history_entry)
                
                # Display result
                self.display_var.set(str(result))
                
                # Reset for next calculation
                self.num1 = None
                self.operation = None
                self.reset_display = True
                self.expression_mode = False
                
                # Reset operation button colors
                self.update_operation_buttons("")
                
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            messagebox.showerror("Error", str(e))
            self.display_var.set("Error")
            self.num1 = None
            self.operation = None
            self.expression = ""
            self.expression_mode = False
    
    def clear_all(self):
        """Clear everything"""
        self.display_var.set("0")
        self.num1 = None
        self.operation = None
        self.reset_display = False
        self.parentheses_count = 0
        self.expression = ""
        self.expression_mode = False
        self.update_operation_buttons("")
    
    def backspace(self):
        """Remove last character"""
        if self.expression_mode and self.expression:
            if len(self.expression) > 1:
                self.expression = self.expression[:-1]
                self.display_var.set(self.expression)
            else:
                self.expression = ""
                self.display_var.set("0")
                self.expression_mode = False
        else:
            current = self.display_var.get()
            if current != "Error":
                if len(current) > 1:
                    self.display_var.set(current[:-1])
                else:
                    self.display_var.set("0")
    
    def toggle_sign(self):
        """Toggle positive/negative"""
        if self.expression_mode and self.expression:
            # In expression mode, add/remove negative at the current position
            if self.expression.startswith('-'):
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.display_var.set(self.expression)
        else:
            current = self.display_var.get()
            if current != "0" and current != "Error":
                if current.startswith('-'):
                    self.display_var.set(current[1:])
                else:
                    self.display_var.set('-' + current)
    
    def toggle_parentheses(self):
        """Add opening or closing parenthesis based on context"""
        if not self.expression_mode:
            self.expression = self.display_var.get()
            self.expression_mode = True
        
        # Count current open parentheses
        open_parens = self.expression.count('(')
        close_parens = self.expression.count(')')
        
        # Determine whether to add opening or closing parenthesis
        if open_parens == close_parens:
            # Add opening parenthesis
            # If last character is a number or closing paren, add multiplication
            if self.expression and (self.expression[-1].isdigit() or self.expression[-1] == ')'):
                self.expression += '×('
            else:
                self.expression += '('
        else:
            # Add closing parenthesis if we have unmatched opening ones
            # But only if the last character is a number or closing paren
            if self.expression and (self.expression[-1].isdigit() or self.expression[-1] == ')'):
                self.expression += ')'
            else:
                # If last character is an operator, we might want to add opening paren instead
                self.expression += '('
        
        self.display_var.set(self.expression)
    
    # Memory functions
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
    
    def memory_recall(self):
        """Recall from memory"""
        self.display_var.set(str(self.memory))
        self.expression = str(self.memory)
        self.expression_mode = True
        self.reset_display = False
    
    def memory_add(self):
        """Add current value to memory"""
        try:
            if self.expression_mode and self.expression:
                current = self.evaluate_expression(self.expression)
            else:
                current = float(self.display_var.get())
            self.memory += current
        except (ValueError, ZeroDivisionError):
            pass
    
    def memory_subtract(self):
        """Subtract current value from memory"""
        try:
            if self.expression_mode and self.expression:
                current = self.evaluate_expression(self.expression)
            else:
                current = float(self.display_var.get())
            self.memory -= current
        except (ValueError, ZeroDivisionError):
            pass

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# Calculator

A modern, feature-rich GUI calculator built with Python and Tkinter, featuring a sleek blue-themed interface and advanced mathematical operations.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)

## Features

### Basic Operations
- Addition, Subtraction, Multiplication, Division
- Modulo (%) operation
- Decimal point support
- Sign toggle (+/-)
- Backspace (delete last character)

### Advanced Operations
- Square root (√)
- Square (x²)
- Reciprocal (1/x)
- Parentheses support for complex expressions
- Expression evaluation (e.g., `2+3×4`)

### Memory Functions
- Memory Clear (MC)
- Memory Recall (MR)
- Memory Add (M+)
- Memory Subtract (M-)

### User Interface
- Clean, modern blue-themed design
- Responsive button layout
- Keyboard input support
- Resizable window
- Error handling with user-friendly messages
- Calculation history tracking

## Screenshots

The calculator features a modern interface with:
- **Light steel blue** function buttons (C, (), %, del)
- **Cornflower blue** operator buttons (+, −, ×, ÷)
- **Slate gray** number buttons (0-9)
- **Sky blue** memory function buttons (MC, MR, M+, M-)
- **Steel blue** equals button (=)

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

3. **Check Tkinter availability**
   ```bash
   python -m tkinter
   ```
   This should open a small Tkinter window. If it doesn't, you may need to install Tkinter:
   
   - **Ubuntu/Debian:**
     ```bash
     sudo apt-get install python3-tk
     ```
   
   - **Fedora:**
     ```bash
     sudo dnf install python3-tkinter
     ```
   
   - **macOS:**
     Tkinter comes pre-installed with Python on macOS
   
   - **Windows:**
     Tkinter comes pre-installed with Python on Windows

4. **Run the calculator**
   ```bash
   python calculator.py
   ```
   or
   ```bash
   python3 calculator.py
   ```

## Usage

### Mouse Input
- Click any button to input numbers, operators, or perform operations
- Click `=` to evaluate the expression
- Click `C` to clear all input
- Click `del` to delete the last character

### Keyboard Input

| Key | Function |
|-----|----------|
| `0-9` | Number input |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |
| `(` or `)` | Toggle parentheses |
| `Enter` or `=` | Calculate result |
| `Backspace` | Delete last character |
| `C` or `c` | Clear all |

### Expression Mode

The calculator supports full expression evaluation with proper order of operations:

```
Example: 2+3×4 = 14 (not 20)
Example: (2+3)×4 = 20
Example: 10÷2+5 = 10
```

### Parentheses

- Click the `( )` button to add opening or closing parentheses
- The calculator automatically determines which type to add based on context
- Supports nested parentheses for complex expressions

### Memory Functions

1. **M+**: Add current display value to memory
2. **M-**: Subtract current display value from memory
3. **MR**: Recall value from memory
4. **MC**: Clear memory

### Advanced Operations

- **√ (Square Root)**: Calculate the square root of the displayed number
- **x² (Square)**: Calculate the square of the displayed number
- **1/x (Reciprocal)**: Calculate the reciprocal (1 divided by the number)

## Code Structure

```
calculator/
│
├── calculator.py       # Main application file
├── requirements.txt    # Dependencies (none required)
├── README.md          # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore rules
```

### Main Components

#### `Calculator` Class
The main class that handles all calculator functionality:

- `__init__(self, root)`: Initialize the calculator
- `setup_ui(self)`: Create the user interface
- `handle_input(self, input_char)`: Process all button/keyboard input
- `calculate(self)`: Evaluate expressions and perform calculations
- `evaluate_expression(self, expression)`: Safely evaluate mathematical expressions
- `calculate_operation(self, op)`: Handle single-operand operations (√, x², 1/x)
- Memory functions: `memory_clear()`, `memory_recall()`, `memory_add()`, `memory_subtract()`
- Utility functions: `clear_all()`, `backspace()`, `toggle_sign()`, `toggle_parentheses()`

## Error Handling

The calculator handles various error cases:

- **Division by zero**: Shows error message and prevents calculation
- **Square root of negative numbers**: Shows error message
- **Invalid expressions**: Catches and handles syntax errors
- **Unmatched parentheses**: Detects and prevents evaluation
- **Overflow errors**: Handles very large numbers with scientific notation

## Technical Details

### Dependencies
- `tkinter`: GUI framework (built-in)
- `math`: Mathematical operations (built-in)
- `re`: Regular expressions for expression parsing (built-in)

### Color Scheme
- Background: `#000000` (Black)
- Display: `#f5f5f5` (Off-white) with black text
- Function buttons: `#B0C4DE` (Light steel blue)
- Operator buttons: `#6495ED` (Cornflower blue)
- Number buttons: `#708090` (Slate gray)
- Memory buttons: `#87CEEB` (Sky blue)
- Equals button: `#4682B4` (Steel blue)

### Expression Evaluation
The calculator uses Python's `eval()` function with restricted globals for safe expression evaluation. It:
- Replaces display symbols (×, ÷, −) with Python operators (*, /, -)
- Validates parentheses balance
- Filters out potentially dangerous characters
- Restricts access to built-in functions except `abs` and `pow`

## Known Limitations

1. Very large numbers (> 1e10) are displayed in scientific notation
2. Results are rounded to 10 decimal places for display
3. Expression evaluation is limited to basic arithmetic operations
4. No support for trigonometric functions (sin, cos, tan, etc.)
5. No support for logarithmic functions

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Reva Malik**

## Acknowledgments

- Built with Python's Tkinter library
- Inspired by modern calculator designs
- Thanks to the Python community for excellent documentation

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/calculator/issues) page
2. Create a new issue with detailed information about the problem
3. Include your Python version and operating system

## Changelog

### Version 1.0.0 (2025)
- Initial release
- Basic arithmetic operations
- Advanced operations (√, x², 1/x)
- Memory functions
- Parentheses support
- Expression evaluation
- Keyboard input support
- Modern blue-themed UI

---

**Happy Calculating!**

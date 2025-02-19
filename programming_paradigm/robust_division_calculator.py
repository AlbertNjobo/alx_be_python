# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)  # Convert numerator to float
        denom = float(denominator)  # Convert denominator to float
        
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        return f"The result of the division is {num / denom:.1f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

















  


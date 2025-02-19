# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs an arithmetic operation on num1 and num2 based on the given operation string.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Valid options are 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or an error message for invalid operations or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"


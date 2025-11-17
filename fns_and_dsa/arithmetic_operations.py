def perform_operation(num1: float, num2: float, operation: str):

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "DIVIDE_BY_ZERO"

    else:
        return "INVALID_OPERATION"

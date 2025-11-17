def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "DIVIDE_BY_ZERO"
        case _:
            return "INVALID OPERATION"
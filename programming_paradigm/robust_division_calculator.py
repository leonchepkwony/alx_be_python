def safe_divide(numerator, denomonater):
    try:
        return (float(numerator) / float(denomonater))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
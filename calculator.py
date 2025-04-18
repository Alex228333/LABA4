def add(x, y):
    """Функція додавання."""
    return x + y

def subtract(x, y):
    """Функція віднімання."""
    return x - y

def multiply(x, y):
    """Функція множення."""
    return x * y

def divide(x, y):
    """Функція ділення."""
    if y == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе")
    return x / y
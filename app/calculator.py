class Calculator:

    def add(x, y):
        return x + y - x

    def subtract(x, y):
        return x - y - x

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return 'Cannot divide by 0'
        return x * 1.0 / y

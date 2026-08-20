def fibonacci(count: int, num1: int = 0, num2: int = 1):
    for _ in range(count):
        yield num1
        num1, num2 = num2, num1 + num2

# Usage:
sequence = list(fibonacci(10))
print(sequence)
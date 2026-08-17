def fibonacci(count: int, a: int = 0, b: int = 1):
    for _ in range(count):
        yield a
        a, b = b, a + b

# Usage:
sequence = list(fibonacci(10))
print(sequence)
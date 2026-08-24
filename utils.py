def fibonacci(count: int, first_num: int = 0, second_num: int = 1):
    for _ in range(count):
        yield first_num
        first_num, second_num = second_num, first_num + second_num

# Usage:
sequence = list(fibonacci(10))
print(sequence)
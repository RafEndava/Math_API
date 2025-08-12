from functools import lru_cache


def calculate_pow(a: int, b: int) -> int:
    return a ** b


@lru_cache(maxsize=1000)
def calculate_fibonacci(n: int) -> int:
    print(">> Calculating fibonacci...")

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@lru_cache(maxsize=1000)
def calculate_factorial(n: int) -> int:
    if n == 0:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

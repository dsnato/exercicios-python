def f(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / f(x, -n)
    elif n % 2 == 0:
        return f(x * x, n // 2)
    else:
        return x * f(x * x, (n - 1) // 2)

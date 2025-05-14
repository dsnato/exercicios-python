def A(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 10)
    else:
        return A(m - 1, A(m, n - 1))

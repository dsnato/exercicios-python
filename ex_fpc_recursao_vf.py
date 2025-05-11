def divisivel7(n):
    if n < 0:
        n = -n
    if n < 70:
        return n == 0 or n == 7 or n == 14 or n == 21 or n == 28 or n == 35 or n == 42 or n == 49 or n == 56 or n == 63

    ultimo = n % 10
    restante = n // 10
    novo = restante - 2 * ultimo
    return divisivel7(novo)

numero = int(input())
if divisivel7(numero):
    print("s")
else:
    print("n")
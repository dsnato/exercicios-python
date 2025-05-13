def fatorial(n):
    if n < 0:
        return 0  # Fatoriais de números negativos são nulos
    if n == 0 or n == 1:
        return 1  # Caso base: 0! e 1! = 1
    return n * fatorial(n - 1)  # Chamada recursiva

# Entrada
n = int(input())

# Saída
print(fatorial(n))

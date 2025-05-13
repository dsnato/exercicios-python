def mod_exp(a, n, m):
    if m <= 1:
        return "impossível calcular"
    if a == 0 and n == 0:
        return "impossível calcular"
    if n == 0:
        return 1
    if n % 2 == 0:
        half = mod_exp(a, n // 2, m)
        return (half * half) % m
    else:
        return (a % m) * mod_exp(a, n - 1, m) % m

# Leitura da entrada
a = int(input())
n = int(input())
m = int(input())

# Cálculo e saída
resultado = mod_exp(a, n, m)
print(resultado)

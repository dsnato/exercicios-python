def exponencial(a, n):
    if a == 0 and n == 0:
        return "impossível calcular"
    if n == 0:
        return 1  # Qualquer número elevado a 0 é 1
    return a * exponencial(a, n - 1)  # Chamada recursiva

# Entrada
a = float(input())
n = int(input())

# Saída
resultado = exponencial(a, n)

if resultado == "impossível calcular":
    print(resultado)
else:
    print(resultado)

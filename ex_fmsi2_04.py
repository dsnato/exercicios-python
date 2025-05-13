def mdc(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    if b == 0:
        return abs_valor(a)
    return mdc(b, a % b)

# Função auxiliar para valor absoluto (não pode usar abs do Python)
def abs_valor(n):
    if n < 0:
        return -n
    return n

# Leitura da entrada
a = int(input())
b = int(input())

resultado = mdc(a, b)
print(resultado)

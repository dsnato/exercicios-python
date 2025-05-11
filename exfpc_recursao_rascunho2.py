def divisivel7(numero):
    if numero == 7:
        return True
    if numero == 0:
        return True
    if numero < 10:
        return False
    if numero == 49:
        return True
    ultimoDigito = numero % 10
    resto = numero // 10
    novoNumero = resto + ultimoDigito * 5

    return divisivel7(novoNumero)


numero = int(input())

if divisivel7(numero):
    print("s")
else:
    print("n")
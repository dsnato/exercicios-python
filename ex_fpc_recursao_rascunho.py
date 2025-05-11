def divisivel7(numero):
    a = numero // 10
    b = numero % 10
    mult = b * 5
    soma = mult + a
    if soma < 7:
        return 'n'
    elif soma <= 70 and soma == 70 or soma == 63 or soma == 56 or soma == 49 or soma == 42 or soma == 35 or soma == 28 or soma == 21 or soma == 14 or soma == 7:
        return 's'
    else:
        return divisivel7(soma)


print(divisivel7(int(input())))
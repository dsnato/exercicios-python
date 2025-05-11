def eh_multiplo_de_7(n, cont=0):
    # Verifica se n é um múltiplo de 7 usando apenas soma recursiva
    if cont > n:
        return False
    if cont == n:
        return True
    return eh_multiplo_de_7(n, cont + 7)

def divisivel7(numero):
    if numero < 10:
        # Casos triviais onde não é possível aplicar mais a regra
        return eh_multiplo_de_7(numero)
    elif numero < 100:
        # Para números pequenos, verifica diretamente se é múltiplo de 7
        return eh_multiplo_de_7(numero)
    else:
        # Aplica a regra de Chika Ofili recursivamente
        ultimo = numero % 10
        resto = numero // 10
        novo = resto + 5 * ultimo
        return divisivel7(novo)

def ler_entrada():
    try:
        entrada = input()
        if entrada.strip() == "":
            return
        numero = int(entrada)
        if divisivel7(numero):
            print("s")
        else:
            print("n")
        ler_entrada()  # chamada recursiva para continuar lendo
    except EOFError:
        return

ler_entrada()

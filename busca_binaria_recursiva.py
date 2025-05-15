from math import floor

def busca_binaria_recursiva(lista, alvo, comparacoes=0):
    # Caso base: lista vazia
    if not lista:
        return comparacoes

    n = len(lista)

    # Índice do elemento central
    if n % 2 == 0:
        meio = n // 2  # primeiro elemento da segunda parte
    else:
        meio = floor(n / 2)  # piso da metade

    comparacoes += 1

    if lista[meio] == alvo:
        return comparacoes
    elif alvo < lista[meio]:
        return busca_binaria_recursiva(lista[:meio], alvo, comparacoes)
    else:
        return busca_binaria_recursiva(lista[meio + 1:], alvo, comparacoes)

# Entrada
entrada = input().split()
alvo = int(entrada[0])
lista = list(map(int, entrada[1:]))

# Chamada e saída
comparacoes = busca_binaria_recursiva(lista, alvo)
print(comparacoes)

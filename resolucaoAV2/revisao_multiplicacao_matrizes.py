from random import randint

def gerar_matriz_dict(linhas, colunas):
    matriz = {"linhas": linhas, "colunas": colunas}
    for i in range(linhas):
        for j in range(colunas):
            matriz[(i, j)] = randint(1, 10)
    return matriz

def multiplicar_matrizes(matriz1, matriz2):
    if matriz1["colunas"] != matriz2["linhas"]:
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz!")

    matriz_resultante = {"linhas": matriz1["linhas"], "colunas": matriz2["colunas"]}

    for i in range(matriz1["linhas"]):
        for j in range(matriz2["colunas"]):
            soma = 0
            for k in range(matriz1["colunas"]):
                soma += matriz1[(i, k)] * matriz2[(k, j)]
            matriz_resultante[(i, j)] = soma

    return matriz_resultante

def imprimir_matriz_dict(matriz, nome):
    print(f"{nome}:")
    for i in range(matriz["linhas"]):
        for j in range(matriz["colunas"]):
            print(f"{matriz[(i, j)]:5d}", end=" ")
        print()
    print()

def main():
    linhas_m1 = int(input("Digite o número de linhas da primeira matriz: "))
    colunas_m1 = int(input("Digite o número de colunas da primeira matriz: "))
    linhas_m2 = int(input("Digite o número de linhas da segunda matriz: "))
    colunas_m2 = int(input("Digite o número de colunas da segunda matriz: "))

    if colunas_m1 != linhas_m2:
        print("Erro! O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        return

    matriz1 = gerar_matriz_dict(linhas_m1, colunas_m1)
    matriz2 = gerar_matriz_dict(linhas_m2, colunas_m2)
    matriz_produto = multiplicar_matrizes(matriz1, matriz2)

    imprimir_matriz_dict(matriz1, "Matriz 1")
    imprimir_matriz_dict(matriz2, "Matriz 2")
    imprimir_matriz_dict(matriz_produto, "Matriz Produto")

if __name__ == "__main__":
    main()

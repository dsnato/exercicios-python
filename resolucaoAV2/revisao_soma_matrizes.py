from random import randint


def gerar_matriz_dict(linhas, colunas):
    matriz = {"linhas": linhas, "colunas": colunas}
    for i in range(linhas):
        for j in range(colunas):
            matriz[(i, j)] = randint(1, 10)
    return matriz


def somar_matrizes(matriz1, matriz2):
    if matriz1["linhas"] != matriz2["linhas"] or matriz1["colunas"] != matriz2["colunas"]:
        raise ValueError("As matrizes devem ter as mesmas dimensões para a soma!")

    matriz_soma = {"linhas": matriz1["linhas"], "colunas": matriz1["colunas"]}

    for i in range(matriz1["linhas"]):
        for j in range(matriz1["colunas"]):
            matriz_soma[(i, j)] = matriz1[(i, j)] + matriz2[(i, j)]

    return matriz_soma


def imprimir_matriz_dict(matriz, nome):
    print(f"{nome}:")
    for i in range(matriz["linhas"]):
        for j in range(matriz["colunas"]):
            print(f"{matriz[(i, j)]:5d}", end=" ")
        print()
    print()


def main():
    linhas = int(input("Digite o número de linhas das matrizes: "))
    colunas = int(input("Digite o número de colunas das matrizes: "))

    matriz1 = gerar_matriz_dict(linhas, colunas)
    matriz2 = gerar_matriz_dict(linhas, colunas)
    matriz_soma = somar_matrizes(matriz1, matriz2)

    imprimir_matriz_dict(matriz1, "Matriz 1")
    imprimir_matriz_dict(matriz2, "Matriz 2")
    imprimir_matriz_dict(matriz_soma, "Matriz Soma")


if __name__ == "__main__":
    main()

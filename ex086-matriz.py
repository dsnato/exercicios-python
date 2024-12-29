'''matriz = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0, ]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:>4}', end='')
    print()'''

'''# Função para inicializar a matriz 3x3
def inicializaMatriz():
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return mat

# Função para imprimir a matriz em formato amigável
def imprimeMatriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end=" ")  # Reserva 4 espaços e alinha à direita
        print()  # Pula para a próxima linha após imprimir uma linha da matriz

# Inicializando a matriz
m = inicializaMatriz()

# Inserindo o número 10 no elemento central (posição [1][1])
m[1][1] = 10

# Imprimindo a matriz
print("Matriz resultante:")
imprimeMatriz(m)'''

# Função para inicializar a matriz 3x3
def inicializaMatriz():
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return mat

# Função para imprimir a matriz em formato amigável
def imprimeMatriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end=" ")  # Reserva 4 espaços e alinha à direita
        print()  # Pula para a próxima linha após imprimir uma linha da matriz

# Inicializando a matriz
m = inicializaMatriz()

# Solicitando input do usuário para o elemento central
valor = int(input("Digite o valor para o elemento central da matriz: "))

# Inserindo o valor no elemento central (posição [1][1])
m[1][1] = valor

# Imprimindo a matriz
print("\nMatriz resultante:")
imprimeMatriz(m)

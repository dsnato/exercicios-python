'''matriz = []
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))
for l in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'Digite o elemento a{l}{c} da matriz: '))
        linha.append(elemento)
    matriz.append(linha)
for linha in matriz:
    for elemento in linha:
        print(f'\n{elemento:4}', end='')
    print()'''

matriz = [[0, 0, 0 ], [0, 0, 0 ], [0, 0, 0 ]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:>4}', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
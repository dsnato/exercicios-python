'''Considere o seguinte trecho de código em Python:
matriz = [ [1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

Crie uma matriz matDic utilizando dicionários usando tuplas como chave
contendo as posições da matriz. Use índices iniciando em 1. A matriz deve
ser preenchida automaticamente utilizando loop.'''

# Matriz original
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Criando a matriz matDic com dicionários usando tuplas como chaves
matDic = {}

# Preenchendo o dicionário com a matriz original
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        # Índices começam em 1, então adicionamos 1 aos índices i e j
        matDic[(i+1, j+1)] = matriz[i][j]

# Exibindo o resultado
print(matDic)

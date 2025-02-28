#Considere o seguinte trecho de código em Python:
matriz = [ [1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

#Crie uma matriz matDic utilizando dicionários usando tuplas como chave
#contendo as posições da matriz. Use índices iniciando em 1. A matriz deve
# ser preenchida automaticamente utilizando loop.
matDic = {}
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        matDic[(l+1, c+1)] = matriz[l][c]

print("Matriz usando listas: ", matriz)
print("Matriz com dicionários (índices iniciando em 1): \n", matDic)
qtdeLinhas = int(input('Digite a qtde de linhas da matriz: '))
qtdeColunas = int(input('Digite a qtde de colunas da matriz: '))

matriz = []
for l in range(qtdeLinhas):
    novaLinha = []
    for c in range(qtdeColunas):
        numero = float(input('Digite o número da linha %d coluna %d: '%(l+1, c+1)))
        novaLinha.append(numero)
    matriz.append(novaLinha)

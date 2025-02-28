from random import randint

#lendo a qtde de linhas e colunas das matrizes:
qtdeLinhasM1 = int(input("Digite a qtde de LINHAS da MATRIZ 1:"))
qtdeColunasM1 = int(input("Digite a qtde de COLUNAS da MATRIZ 1:"))
qtdeLinhasM2= int(input("Digite a qtde de LINHAS da MATRIZ 2:"))
qtdeColunasM2 = int(input("Digite a qtde de COLUNAS da MATRIZ 2:"))

if qtdeLinhasM1 == qtdeLinhasM2 and qtdeColunasM1 == qtdeColunasM2: #posso fazer a SOMA das matrizes
    mat1 = {}
    mat1['qtdeLinhas'] = qtdeLinhasM1
    mat1['qtdeColunas'] = qtdeColunasM1
    mat2 = {'qtdeLinhas': qtdeLinhasM2, 'qtdeColunas': qtdeColunasM2}
    matRes = {'qtdeLinhas': qtdeLinhasM1, 'qtdeColunas': qtdeColunasM1}

    #preenchendo a 1a matriz:
    for l in range(qtdeLinhasM1):
        for c in range(qtdeColunasM1):
            mat1[(l,c)] = randint(0, 99)
    #preenchendo a 2a matriz:
    for l in range(qtdeLinhasM2):
        for c in range(qtdeColunasM2):
            mat2[(l,c)] = randint(0, 99)
    #realizando a SOMA das matrizes:
    for l in range(qtdeLinhasM1):
        for c in range(qtdeColunasM1):
            matRes[(l, c)] = mat1[(l, c)] + mat2[(l, c)]

    #imprimindo as matrizes:
    def imprimeMatDic(matriz): #o dic. matriz deve ter as chaves qtdeLinhas e qtdeColunas
        for i in range(matriz['qtdeLinhas']):
            for j in range(matriz['qtdeColunas']):
                print("%5d"%matriz[(i,j)], end=" ")
            print()
    print("Matriz 1: ")
    imprimeMatDic(mat1)
    print("Matriz 2:")
    imprimeMatDic(mat2)
    print("SOMA de Matriz 1 com Matriz 2:")
    imprimeMatDic(matRes)

else:
    print("Erro! As dimensões das matrizes devem ser idênticas")
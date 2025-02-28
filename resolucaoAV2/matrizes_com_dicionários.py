def imprimeMatrizDicionarios(matriz, linhas, colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(f"{matriz[(l, c)]:5.2f}", end=" ")
        print() #enter

m = {}
#
# m[(0, 0)] = 21
# m[(0, 1)] = 22
# m[(1, 0)] = 23
# m[(1, 1)] = 25
#
# #m[0][0] = 0 #aw utilizasse listas seria assim
#
# #com dicionarios:
# m[(0, 0)] = 0

nlinhas = int(input("Digite a quantidade de linhas da matriz:"))
ncolunas = int(input("Digite a quantidade de colunas da matriz:"))

for l in range(nlinhas):
    for c in range(ncolunas):
        elem = float(input(f"Digite o elemento da linha {l} coluna {c}: "))
        m[(l, c)] = elem
print("Matriz: ")
imprimeMatrizDicionarios(m, nlinhas, ncolunas)

print("===== Alteração de elemento =====")
l = int(input("Digite a linha:"))
c = int(input("Digite a coluna:"))
if (l, c) not in m.keys():
    print("Erro! A posição informada não existe na matriz")
else:
    elem = float(input("Digite o novo elemento: "))
    m[(l, c)] = elem
    imprimeMatrizDicionarios(m, nlinhas, ncolunas)

print(type(m))
print(m)
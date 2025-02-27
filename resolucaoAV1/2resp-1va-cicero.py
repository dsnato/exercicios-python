# Entrada da quantidade de linhas e colunas
qtdeLinhas = int(input("Digite a quantidade de linhas da matriz: "))
qtdeColunas = int(input("Digite a quantidade de colunas da matriz: "))

# Inicialização da matriz
matriz = []
for l in range(qtdeLinhas):
    novaLinha = []
    for c in range(qtdeColunas):
        numero = float(input(f"Digite o número da linha {l+1}, coluna {c+1}: "))
        novaLinha.append(numero)
    matriz.append(novaLinha)

# Impressão do triplo de cada elemento da matriz
print("\nMatriz com o triplo de cada elemento (formatado):")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento * 3:8.2f}", end=" ")  # Formato: 8 espaços totais, 2 decimais
    print()  # Pula para a próxima linha

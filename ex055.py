pesoMaior = 0
pesoMenor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa em Kg: '))
    if p == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'O maior peso lido foi de {pesoMaior}Kg.')
print(f'O menor peso lido foi de {pesoMenor}Kg.')
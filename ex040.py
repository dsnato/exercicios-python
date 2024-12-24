n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print(f'Você tirou {n1} na primeira prova e {n2} na segunda prova, sua média é: {média}')
if média < 5:
    print('Reprovado!')
elif média >= 5 and média <= 6.99:
    print('Recuperação!')
else:
    print('Aprovado!')

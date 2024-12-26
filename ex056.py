somaIdade = 0
médiaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaIdade += idade
    if p == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        totMulher20 += 1
médiaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {médiaIdade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos.')

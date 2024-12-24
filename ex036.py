casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário da pessoa? R$'))
anos = int(input('Em quantos anos quer pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}.'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')

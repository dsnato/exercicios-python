salário = float(input('Qual o salário do funcionário: R$'))
if salário > 1250:
    aumento = salário * 1.1
    print('O salário era de R${:.2f} e passou a ser com o aumento R${:.2f}.'.format(salário, aumento))
else:
    aumento = salário * 1.15
    print('O salário era de R${:.2f} e passou a ser com o aumento R${:.2f}.'.format(salário, aumento))

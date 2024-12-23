#EXEMPLOS ANTES DOS EXERCÍCIOS

"""tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')"""

"""tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo!' if tempo <= 3 else 'Carro velho')
print('--FIM--')"""

"""nome = str(input('Qual é seu nome? '))
if nome == 'Renato':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! Estude mais!')"""

#EXERCÍCIO 28

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e você disse {}.'.format(computador, jogador))

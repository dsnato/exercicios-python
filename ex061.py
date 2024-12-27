print('=' * 30)
print('         GERADOR DE PA')
print('=' * 30)
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiroTermo
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razão
    cont += 1
print('FIM!')

print('=' * 30)
print('         GERADOR DE PA')
print('=' * 30)
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razão
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais (Digite 0 para finalizar)? '))
print(f'A Progressão foi finalizada com {total} termos mostrados. FIM!')

números = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado novamente.')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(números)}')

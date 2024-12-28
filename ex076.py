listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 20,
            'Mochila', 120,
            'Canetas', 5)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for p in range(0, len(listagem)):
    if p % 2 == 0:
        print(f'{listagem[p]:.<30}', end='')
    else:
        print(f'R${listagem[p]:>7.2f}')
print('-' * 40)
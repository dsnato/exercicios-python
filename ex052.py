n = int(input('Digite um número inteiro para descobrir se ele é primo: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m0 número {n} foi divisível {tot} vezes')
if tot == 2:
    print('e por isso ele é primo!')
else:
    print('e por isso ele não é primo!')

print('=' * 50)
n = int(input('Digite um número inteiro para saber sua tabuada: '))
print('=' * 50)
for c in range(0, 11):
    print(f'{c:>3} X {n:>3} = {n * c:>3}')
print('=' * 50)

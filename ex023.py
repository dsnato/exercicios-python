'''num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
print(f'Analisando o número {num}')
print(f'Unidade é: {n[3]}')
print(f'Dezena é: {n[2]}')
print(f'Centena é: {n[1]}')
print(f'Milhar é: {n[0]}')'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade é: {u}')
print(f'Dezena é: {d}')
print(f'Centena é: {c}')
print(f'Milhar é: {m}')

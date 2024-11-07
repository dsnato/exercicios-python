"""from math import trunc
n = float(input('Digite um valor: '))
i = trunc(n)
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, i))"""

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {:.1f}.'.format(n, int(n)))

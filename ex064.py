n = c = s = 0
n = int(input('Digite um número [999 para parar!]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar!]: '))
print(f'Você digitou {c} números e a soma entre eles foi {s}. Fim!')

print('-=-' * 20)
print('Analisador de triângulo')
print('-=-' * 20)
r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores passados podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os valores passados NÃO podem formar um triângulo.')

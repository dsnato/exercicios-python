num = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão:
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Digite a opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é: {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')

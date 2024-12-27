cont = soma = 0
while True:
    num = int(input('Digite um número inteiro: [999 para o programa] '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'Você digitou {cont} números e a soma foi {soma}.')

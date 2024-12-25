peso = float(input('Qual é o peso (em Kg)? '))
altura = float(input('Qual é a altura (em m)? '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}.')
if imc < 18.5:
    print('Abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida!')

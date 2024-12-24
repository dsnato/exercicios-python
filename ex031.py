distância = float(input('Qual a distância em Km da sua viagem? '))
print('Você está prestes a cimnela uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('Já que a distância da sua viagem é de {}Km e o preço será de R${:.2f}.'.format(distância, preço))

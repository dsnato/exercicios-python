primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimoTermo = primeiroTermo + (10 - 1) * razão
for c in range(primeiroTermo, décimoTermo + razão, razão):
    print(c, end= ' > ')
print('Essa foi a PA solicitada!')

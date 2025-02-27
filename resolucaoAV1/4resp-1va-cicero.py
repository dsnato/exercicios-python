nome = "Isabel Cristina Leopoldina"
nome += " Augusta Micaela Gabriela"
nome += " Rafaela Gonzaga de Orléans"
nome += " e Bragança"

# Remove "Micaela" e "Rafaela" da string
nome = nome.split(' Micaela ')
nome = ' '.join(nome)
nome = nome.split(' Rafaela ')
nome = ' '.join(nome)

# Exibe o resultado
print(nome)

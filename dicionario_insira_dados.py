n = str(input('Digite seu nome: '))
i = int(input('Digite sua idade: '))
t = int(input('Digite seu telefone: '))
e = str(input('Digite seu endereço: '))

d = {'nome': n, 'idade': i, 'telefone': t, 'endereço': e}

print(d)
lista_de_chaves = list(d.keys())
lista_de_chaves.sort()
print(lista_de_chaves)

for i in lista_de_chaves:
    print(i, ":", d[i])



#for chave in listaDeChaves:


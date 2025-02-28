'''Observe o programa abaixo. Escreva um trecho de código
após o programa para exibir o CPF e o nome das pessoas que
 possuem 18 anos ou mais.
'''

pessoas = {
    "123.456.789-00": {"nome": "Ana", "idade": 17},
    "987.654.321-00": {"nome": "Carlos", "idade": 20},
    "456.123.789-00": {"nome": "Mariana", "idade": 18},
    "741.852.963-00": {"nome": "Paulo", "idade": 15}
}

print("Pessoas com 18 anos ou mais:")
for cpf, dados in pessoas.items():
    if dados["idade"] >= 18:
        print(f"CPF: {cpf}, Nome: {dados['nome']}")

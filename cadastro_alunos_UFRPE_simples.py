# Função para adicionar um novo aluno
def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    curso = input("Curso do aluno: ")

    endereco = {
        'rua': input("Rua: "),
        'numero': input("Número: "),
        'bairro': input("Bairro: ")
    }

    alunos[nome] = {
        'curso': curso,
        'endereco': endereco
    }
    print(f"Aluno {nome} adicionado com sucesso!")


# Função para atualizar dados de um aluno
def atualizar_aluno(alunos):
    nome = input("Nome do aluno a ser atualizado: ")
    if nome in alunos:
        print("O que você deseja atualizar?")
        print("1. Nome")
        print("2. Curso")
        print("3. Endereço")

        opcao = input("Opção: ")
        if opcao == '1':
            novo_nome = input("Novo nome: ")
            alunos[novo_nome] = alunos.pop(nome)
            print("Nome atualizado com sucesso!")
        elif opcao == '2':
            novo_curso = input("Novo curso: ")
            alunos[nome]['curso'] = novo_curso
            print("Curso atualizado com sucesso!")
        elif opcao == '3':
            nova_rua = input("Nova rua: ")
            novo_numero = input("Novo número: ")
            novo_bairro = input("Novo bairro: ")
            alunos[nome]['endereco'] = {
                'rua': nova_rua,
                'numero': novo_numero,
                'bairro': novo_bairro
            }
            print("Endereço atualizado com sucesso!")
        else:
            print("Opção inválida!")
    else:
        print(f"Aluno {nome} não encontrado!")


# Função principal
def main():
    alunos = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Atualizar aluno")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_aluno(alunos)
        elif opcao == '2':
            atualizar_aluno(alunos)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    main()

def exibir_torres(torres):
    """Exibe o estado atual das torres."""
    for nome, torre in torres.items():
        print(f"{nome}: {torre}")
    print("-" * 30)


def mover_disco(torres, origem, destino):
    """Move um disco de uma torre para outra."""
    if not torres[origem]:
        print(f"Torre {origem} está vazia! Movimento inválido.")
        return False
    if torres[destino] and torres[destino][-1] < torres[origem][-1]:
        print(f"Movimento inválido! Não pode colocar o disco {torres[origem][-1]} sobre {torres[destino][-1]}.")
        return False

    disco = torres[origem].pop()
    torres[destino].append(disco)
    return True


def torre_de_hanoi_jogo(n_discos):
    """Inicia o jogo interativo da Torre de Hanói."""
    torres = {
        'A': list(range(n_discos, 0, -1)),  # Torre de origem
        'B': [],  # Torre auxiliar
        'C': []  # Torre de destino
    }

    print("Bem-vindo ao jogo da Torre de Hanói!")
    exibir_torres(torres)

    while torres['C'] != list(range(n_discos, 0, -1)):
        origem = input("Mover de (A, B, C): ").strip().upper()
        destino = input("Mover para (A, B, C): ").strip().upper()

        if origem in torres and destino in torres:
            if mover_disco(torres, origem, destino):
                exibir_torres(torres)
            else:
                print("Tente novamente.")
        else:
            print("Entrada inválida. Escolha entre A, B ou C.")

    print("Parabéns! Você completou o jogo!")


# Inicia o jogo com 3 discos
torre_de_hanoi_jogo(3)

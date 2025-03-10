def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def verificar_empate(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)


def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    print("\n🎮 Bem-vindo ao Jogo da Velha! 🎮")

    while True:
        exibir_tabuleiro(tabuleiro)

        try:
            linha = int(input(f"\n{jogador_atual}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"{jogador_atual}, escolha a coluna (0, 1, 2): "))

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual

                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"\n🎉 Parabéns! O jogador {jogador_atual} venceu!")
                    break

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("\n🤝 O jogo terminou em empate!")
                    break

                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("❌ Posição já ocupada! Escolha outra.")

        except (ValueError, IndexError):
            print("⚠️ Entrada inválida! Escolha um número entre 0 e 2.")


jogo_da_velha()

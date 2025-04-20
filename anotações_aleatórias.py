def maior_faltante(n, s):
    proibidos = set(s.split())
    left, right = 1, n
    resposta = -1

    while left <= right:
        mid = (left + right) // 2
        if str(mid) in proibidos:
            right = mid - 1
        else:
            resposta = mid  # candidato atual
            left = mid + 1  # tenta achar maior ainda

    print(resposta)

# Exemplo de uso:
n = 4
s = '2 4 3'
maior_faltante(n, s)

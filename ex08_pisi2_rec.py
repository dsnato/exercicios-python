def gols(m, n, sequencia=""):
    if m == 0 and n == 0:
        print(sequencia)
    if m > 0:
        gols(m - 1, n, sequencia + "A ")
    if n > 0:
        gols(m, n - 1, sequencia + "B ")

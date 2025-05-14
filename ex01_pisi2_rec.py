def comb_rec(n, k):
    if k == 0 or k == n:
        return 1
    return comb_rec(n - 1, k - 1) + comb_rec(n - 1, k)

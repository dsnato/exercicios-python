n = 4
s = '2 4 3'

passo = 0
while n != passo:
    if str(n-passo) in s:
        passo += 1
    else:
        print((n-passo))
        break

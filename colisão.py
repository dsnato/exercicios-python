X0A, Y0A, X1A, Y1A = [int(i) for i in input().split()]
X0B, Y0B, X1B, Y1B = [int(i) for i in input().split()]

#testando a não colisão para eixo x
if X1A < X0B or X0A > X1B:
    print('0') #não colide em X
elif Y1A < Y0B or Y0A > Y1B:
    print('0')  # não colide em Y
else:
    print('1')  # não não colide em X nem não colide em Y


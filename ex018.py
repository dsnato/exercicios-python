from math import sin, cos, tan, radians

ângulo = float(input('Digite um número: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} o SENO é {:.2f}, COSSENO é {:.2f} e TANGENTE é {:.2f}'.format(ângulo, seno, cosseno, tangente))

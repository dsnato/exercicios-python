class Retangulo:
    lado_a = None
    lado_b = None

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print('Criada uma nova instância Retângulo')


    def calcula_area(self):
        return self.lado_a * self.lado_b


    def calcula_perimetro(self):
        return 2 * self.lado_a + 2 * self.lado_b


#Programa principal
listaRetangulos, listaAreas = [], []
for i in range(1, 51):
    lado1 = float(input(f'Insira um lado do retângulo {i}: '))
    lado2 = float(input(f'Insira o outro lado do retângulo {i}: '))
    novoRetangulo = Retangulo(lado1, lado2)
    listaRetangulos.append(novoRetangulo)
maiorArea, maiorRetangulo = 0, None
for r in listaRetangulos:
    area = r.calcula_area()
    if area > maiorArea:
        if area > maiorArea:
            maiorArea, maiorRetangulo = area, r
        listaAreas.append(area)
print(f'Maior retângulo:Retângulo {listaRetangulos.index(maiorRetangulo)+1}')
print(f'Maior Lado A: {maiorRetangulo.lado_a}')
print(f'Maior Lado B: {maiorRetangulo.lado_b}')

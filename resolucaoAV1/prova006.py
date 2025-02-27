'''class Retangulo:
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


listaRetangulos = []
for i in range(50):
    lado_a = int(input(f'insira o lado a do retângulo {i+1}: '))
    lado_b = int(input(f'insira o lado b do retângulo {i+1}: '))
    r = Retangulo(lado_a, lado_b)
    listaRetangulos.append(r)

maior_retangulo, maior_area = None, 0
for i in listaRetangulos:
    area = i.calcula_area()
    if area > maior_area:
        maior_retangulo = i
        maior_area = area

print(f"Área: {maior_area}")
print('lado a:', maior_retangulo.lado_a)
print('lado b:', maior_retangulo.lado_b)'''
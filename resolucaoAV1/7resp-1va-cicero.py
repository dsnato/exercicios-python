class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print("Criada uma nova instancia Retangulo")

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_perimetro(self):
        return 2 * self.lado_a + 2 * self.lado_b


# Programa principal
listaRetangulos = []

# Criando 50 retângulos
for i in range(5):
    print(f"\nDigite os lados do retângulo {i + 1}:")
    lado_a = float(input("Lado A: "))
    lado_b = float(input("Lado B: "))

    retangulo = Retangulo(lado_a, lado_b)
    listaRetangulos.append(retangulo)

# Encontrando o retângulo com a maior área
maior_area = 0
retangulo_maior_area = None

for retangulo in listaRetangulos:
    area = retangulo.calcula_area()
    if area > maior_area:
        maior_area = area
        retangulo_maior_area = retangulo

# Exibindo os lados do retângulo com a maior área
print("\nO retângulo com a maior área tem os seguintes lados:")
print(f"Lado A: {retangulo_maior_area.lado_a}")
print(f"Lado B: {retangulo_maior_area.lado_b}")
print(f"Área: {maior_area}")

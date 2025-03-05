def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Erro! Divisão por zero."
        return num1 / num2
    else:
        return "Operação inválida!"


while True:
    print("\n🔢 CALCULADORA SIMPLES 🔢")

    try:
        n1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        n2 = float(input("Digite o segundo número: "))

        resultado = calcular(n1, n2, operador)
        print(f"🟢 Resultado: {resultado}")

    except ValueError:
        print("❌ Entrada inválida! Certifique-se de digitar números válidos.")

    continuar = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando a calculadora. Até mais!")
        break

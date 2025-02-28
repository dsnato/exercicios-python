class ContaBancaria:
    def __init__(self, nomeDoTitular, numero, saldo, tipo):
        if tipo not in ["corrente", "poupança"]:
            raise ValueError("Tipo de conta inválido! Escolha 'corrente' ou 'poupança'.")
        self.nomeDoTitular = nomeDoTitular
        self.numero = numero
        self.__saldo = saldo  # Protegendo o saldo
        self.tipo = tipo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.__saldo -= valor
        else:
            print("O valor do saque deve ser positivo.")

    def imprimir_dados(self):
        print(f"Titular: {self.nomeDoTitular}, Número: {self.numero}, Tipo: {self.tipo}, Saldo: {self.__saldo}")


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        if isinstance(conta, ContaBancaria):
            self.contas.append(conta)
        else:
            print("Erro: O objeto fornecido não é uma ContaBancaria.")

    def remover_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                return
        print("Conta não encontrada.")

    def imprimir_contas(self):
        for conta in self.contas:
            conta.imprimir_dados()


# Exemplo de uso:
try:
    conta1 = ContaBancaria("João Silva", "12345", 1000.0, "corrente")
    conta2 = ContaBancaria("Maria Souza", "67890", 500.0, "poupança")
    # conta3 = ContaBancaria("Carlos Pereira", "11223", 700.0, "investimento")  # Vai gerar erro

    cliente = Cliente("João Silva", "123.456.789-00")
    cliente.adicionar_conta(conta1)
    cliente.adicionar_conta(conta2)

    cliente.imprimir_contas()
except ValueError as e:
    print(e)

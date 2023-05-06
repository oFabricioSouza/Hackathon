from cliente import Cliente


class Conta:
    # Abertura do construtor.
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = Cliente
        self.saldo = saldo
        self.limite = limite

    # Função de depósito.
    def depositar(self, valor):
        # Saldo recebe um encremento de valor.
        self.saldo += valor
        print(f'Valor depositado: {valor}')
        
    def trasnfere_para(self, destino, valor):
        # Saldo recebe um decremento de valor.
        self.saldo -= valor

        # Saldo da conta destino recebe um encremento de valor.
        destino.saldo += valor
        print(f'Valor a ser transferido: {valor}')

    def saca(self, valor):
        # Só vai sacar se o saldo for maior ou igual ao valor requerido.
        if(self.saldo >= valor):
            self.saldo -= valor
        
        else:
            print('Você não possui esta quantia')

    def extrato(self):
        print(f'Nome do titular: {self.titular} \n'
              f'Número da conta: {self.numero} \n'
              f'Saldo disponível: {self.saldo} \n'
              f'Limite disponível: {self.limite}')

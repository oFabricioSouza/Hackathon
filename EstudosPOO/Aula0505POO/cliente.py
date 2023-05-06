
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def exibir(self):
        print(f"""
            Cliente: {self.nome} {self.sobrenome}\n
            CPF: {self.cpf}
        """)
    
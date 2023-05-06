
from conta import *
from cliente import *

if __name__ == '__main__':
    cliente1 = Cliente('Fabricio', 'Souza', '122.466.407-84')
    conta1 = Conta('0803', 'Fabricio Souza' , 5400.00, 6000.00)
    conta1.extrato()
    print("=-"*25)
    cliente1.exibir()
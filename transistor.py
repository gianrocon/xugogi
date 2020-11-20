from prettytable import PrettyTable

class Transistor():

    """
        Classe para criação de transistores.

        EXEMPLO (utilizei opcional Prettytable para melhorar output):

            tabela = PrettyTable(['Entrada', 'Chave', 'Saída'])
            transistor1 = Transistor()
            tabela.add_row([transistor1.entrada, transistor1.chave, transistor1.saida])
            transistor1.switch_chave()
            tabela.add_row([transistor1.entrada, transistor1.chave, transistor1.saida])
            transistor1.entrada = 1
            tabela.add_row([transistor1.entrada, transistor1.chave, transistor1.saida])
            transistor1.chave = 0
            tabela.add_row([transistor1.entrada, transistor1.chave, transistor1.saida])
            print(tabela)

            OUTPUT:
            +---------+-------+-------+
            | Entrada | Chave | Saída |
            +---------+-------+-------+
            |    0    |   0   |   0   |
            |    0    |   1   |   0   |
            |    1    |   1   |   1   |
            |    1    |   0   |   0   |
            +---------+-------+-------+
    """

    def __init__(self, chave=0, entrada=0):
        self.entrada = entrada
        self.chave = chave
    
    def liga_chave(self):
        self.chave = 1

    def desliga_chave(self):
        self.chave = 0

    def switch_chave(self):
        self.chave = int(not self.chave)

    @property
    def saida(self):
        return int(self.entrada and self.chave)

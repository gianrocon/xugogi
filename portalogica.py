from prettytable import PrettyTable
from transistor import Transistor


class BasePorta():

    """
    Classe base para criação das classes das portas lógicas.

    """

    def __init__(self, energia=0):
        self.energia = energia
        self.transistorA = Transistor()
        self.transistorB = Transistor()


class AndPorta(BasePorta):

    """
    Classe para criação de portas lógicas  do tipo AND.

    EXEMPLO (utilizei opcional Prettytable para melhorar output):

            tableand = PrettyTable(['Energia', 'Chave A', 'Chave B', 'Saída'])
            tableand.title = 'AND'
            and1 = AndPorta(energia=1)
            tableand.add_row([and1.energia, and1.transistorA.chave, and1.transistorB.chave, and1.saida])
            and1.transistorA.liga_chave()
            tableand.add_row([and1.energia, and1.transistorA.chave, and1.transistorB.chave, and1.saida])
            and1.transistorB.liga_chave()
            tableand.add_row([and1.energia, and1.transistorA.chave, and1.transistorB.chave, and1.saida])
            and1.transistorA.switch_chave()
            tableand.add_row([and1.energia, and1.transistorA.chave, and1.transistorB.chave, and1.saida])
            print(tableand)

            OUTPUT:
            +-------------------------------------+
            |                 AND                 |
            +---------+---------+---------+-------+
            | Energia | Chave A | Chave B | Saída |
            +---------+---------+---------+-------+
            |    1    |    0    |    0    |   0   |
            |    1    |    1    |    0    |   0   |
            |    1    |    1    |    1    |   1   |
            |    1    |    0    |    1    |   0   |
            +---------+---------+---------+-------+
    """

    @property
    def saida(self):
        self.transistorA.entrada = self.energia
        self.transistorB.entrada = self.transistorA.saida
        return self.transistorB.saida


class OrPorta(BasePorta):
    
    """
    Classe para criação de portas lógicas  do tipo OR.

    EXEMPLO (utilizei opcional Prettytable para melhorar output):

            tableor = PrettyTable(['Energia', 'Chave A', 'Chave B', 'Saída'])
            tableor.title = 'OR'
            or1 = OrPorta(energia=1)
            tableor.add_row([or1.energia, or1.transistorA.chave, or1.transistorB.chave, or1.saida])
            or1.transistorA.liga_chave()
            tableor.add_row([or1.energia, or1.transistorA.chave, or1.transistorB.chave, or1.saida])
            or1.transistorB.liga_chave()
            tableor.add_row([or1.energia, or1.transistorA.chave, or1.transistorB.chave, or1.saida])
            or1.transistorA.switch_chave()
            tableor.add_row([or1.energia, or1.transistorA.chave, or1.transistorB.chave, or1.saida])
            print(tableor)

            OUTPUT:
            +-------------------------------------+
            |                 AND                 |
            +---------+---------+---------+-------+
            | Energia | Chave A | Chave B | Saída |
            +---------+---------+---------+-------+
            |    1    |    0    |    0    |   0   |
            |    1    |    1    |    0    |   0   |
            |    1    |    1    |    1    |   1   |
            |    1    |    0    |    1    |   0   |
            +---------+---------+---------+-------+
    """

    @property
    def saida(self):
        self.transistorA.entrada = self.energia
        self.transistorB.entrada = self.energia
        return int(self.transistorA.saida or self.transistorB.saida)


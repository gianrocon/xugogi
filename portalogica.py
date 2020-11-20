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
            xor1 = AndPorta(energia=1)
            tableand.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.liga_chave()
            tableand.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorB.liga_chave()
            tableand.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.switch_chave()
            tableand.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
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
            |                 OR                  |
            +---------+---------+---------+-------+
            | Energia | Chave A | Chave B | Saída |
            +---------+---------+---------+-------+
            |    1    |    0    |    0    |   0   |
            |    1    |    1    |    0    |   1   |
            |    1    |    1    |    1    |   1   |
            |    1    |    0    |    1    |   1   |
            +---------+---------+---------+-------+
    """

    @property
    def saida(self):
        self.transistorA.entrada = self.energia
        self.transistorB.entrada = self.energia
        return int(self.transistorA.saida or self.transistorB.saida)


class NandPorta(BasePorta):
    
    """
        Classe para criação de portas lógicas  do tipo NAND.

        EXEMPLO (utilizei opcional Prettytable para melhorar output):

            tablexor = PrettyTable(['Energia', 'Chave A', 'Chave B', 'Saída'])
            tablexor.title = 'NAND'
            xor1 = NandPorta(energia=1)
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.liga_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorB.liga_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.switch_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            print(tablexor)

            OUTPUT:
            +-------------------------------------+
            |                 NAND                |
            +---------+---------+---------+-------+
            | Energia | Chave A | Chave B | Saída |
            +---------+---------+---------+-------+
            |    1    |    0    |    0    |   1   |
            |    1    |    1    |    0    |   1   |
            |    1    |    1    |    1    |   0   |
            |    1    |    0    |    1    |   1   |
            +---------+---------+---------+-------+
    """

    @property
    def saida(self):
        self.transistorA.entrada = self.energia
        self.transistorB.entrada = self.transistorA.saida
        return int(not self.transistorB.saida)


class XorPorta(BasePorta):

    """
        Classe para criação de portas lógicas do tipo XOR.

        EXEMPLO (utilizei opcional Prettytable para melhorar output):

            tablexor = PrettyTable(['Energia', 'Chave A', 'Chave B', 'Saída'])
            tablexor.title = 'XOR'
            xor1 = XorPorta(energia=1)
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.liga_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorB.liga_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            xor1.transistorA.switch_chave()
            tablexor.add_row([xor1.energia, xor1.transistorA.chave, xor1.transistorB.chave, xor1.saida])
            print(tablexor)

            OUTPUT:
            +-------------------------------------+
            |                 XOR                 |
            +---------+---------+---------+-------+
            | Energia | Chave A | Chave B | Saída |
            +---------+---------+---------+-------+
            |    1    |    0    |    0    |   0   |
            |    1    |    1    |    0    |   1   |
            |    1    |    1    |    1    |   0   |
            |    1    |    0    |    1    |   1   |
            +---------+---------+---------+-------+
    """

    def __init__(self, energia=0):
        super().__init__(energia=energia)
        self.orporta = OrPorta()
        self.nandporta = NandPorta()
        self.andporta = AndPorta()

    @property
    def saida(self):
        self.orporta.energia = self.nandporta.energia = self.andporta.energia = self.energia
        self.orporta.transistorA.chave = self.nandporta.transistorA.chave = self.transistorA.chave
        self.orporta.transistorB.chave = self.nandporta.transistorB.chave = self.transistorB.chave
        self.andporta.transistorA.chave = self.orporta.saida
        self.andporta.transistorB.chave = self.nandporta.saida
        return int(self.andporta.saida)

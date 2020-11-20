from portalogica import XorPorta, AndPorta, OrPorta
from transistor import Transistor
from prettytable import PrettyTable

class Halfadder():

    """
        Classe para criação do componemte HALF ADDER.

        EXEMPLO (utilizei opcional Prettytable para melhorar output):

            hatable = PrettyTable(['Energia', 'Chave A', 'Chave B', 'Carrier', 'Direita'])
            hatable.title = 'Half Adder'
            ha1 = Halfadder()
            ha1.energia = 1
            hatable.add_row([ha1.energia, ha1.inputA, ha1.inputB, ha1.carrier, ha1.direita])
            ha1.inputA = 1
            hatable.add_row([ha1.energia, ha1.inputA, ha1.inputB, ha1.carrier, ha1.direita])
            ha1.inputB = 1
            hatable.add_row([ha1.energia, ha1.inputA, ha1.inputB, ha1.carrier, ha1.direita])        
            ha1.inputA = 0
            hatable.add_row([ha1.energia, ha1.inputA, ha1.inputB, ha1.carrier, ha1.direita])
            print(hatable)

            OUTPUT:
            +--------------------------------------------------+
            |                    Half Adder                    |
            +---------+---------+---------+----------+---------+
            | Energia | Chave A | Chave B | Carrier  | Direita |
            +---------+---------+---------+----------+---------+
            |    1    |    0    |    0    |    0     |    0    |
            |    1    |    1    |    0    |    0     |    1    |
            |    1    |    1    |    1    |    1     |    0    |
            |    1    |    0    |    1    |    0     |    1    |
            +---------+---------+---------+----------+---------+
    """

    def __init__(self, energia=0):
        self.energia = energia
        self.inputA = 0
        self.inputB = 0
        self.xorporta = XorPorta()
        self.andporta = AndPorta()

    @property
    def direita(self):
        self.xorporta.energia = self.energia
        self.xorporta.transistorA.chave = self.inputA
        self.xorporta.transistorB.chave = self.inputB
        return int(self.xorporta.saida)

    @property
    def carrier(self):
        self.andporta.energia = self.energia
        self.andporta.transistorA.chave = self.inputA
        self.andporta.transistorB.chave = self.inputB
        return int(self.andporta.saida)


class Fulladder():

    """
        Classe para criação do componemte HALF ADDER.

        EXEMPLO (utilizei opcional Prettytable para melhorar output):

            fatable = PrettyTable(['Energia', 'Received', 'Input A', 'Input B', 'Carrier' ,'Direita'])
            fatable.title = 'Full Adder'
            fa1 = Fulladder()
            fa1.energia = 1
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.inputA = 1
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.inputB = 1
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.inputA = 0
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.received = 1
            fa1.inputA = 0
            fa1.inputB = 0
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.inputA = 1
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            fa1.inputB = 1
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])        
            fa1.inputA = 0
            fatable.add_row([fa1.energia, fa1.received, fa1.inputA, fa1.inputB, fa1.saidas[0], fa1.saidas[1]])
            print(fatable)

            OUTPUT:
            +------------------------------------------------------------+
            |                         Full Adder                         |
            +---------+----------+---------+---------+---------+---------+
            | Energia | Received | Input A | Input B | Carrier | Direita |
            +---------+----------+---------+---------+---------+---------+
            |    1    |    0     |    0    |    0    |    0    |    0    |
            |    1    |    0     |    1    |    0    |    0    |    1    |
            |    1    |    0     |    1    |    1    |    1    |    0    |
            |    1    |    0     |    0    |    1    |    0    |    1    |
            |    1    |    1     |    0    |    0    |    0    |    1    |
            |    1    |    1     |    1    |    0    |    1    |    0    |
            |    1    |    1     |    1    |    1    |    1    |    1    |
            |    1    |    1     |    0    |    1    |    1    |    0    |
            +---------+----------+---------+---------+---------+---------+
    """

    def __init__(self, energia=0, received=0):
        self.energia = energia
        self.received = received
        self.inputA = 0
        self.inputB = 0

    @property
    def saidas(self):
        ha_prev = Halfadder()
        ha_new = Halfadder()
        ha_prev.energia = ha_new.energia = self.energia
        ha_new.inputA = self.inputA
        ha_new.inputB = self.inputB
        ha_prev.inputA = self.received
        ha_prev.inputB = ha_new.direita
        direita = ha_prev.direita
        or_do_carrier = OrPorta()
        or_do_carrier.energia = self.energia
        or_do_carrier.transistorA.chave = ha_prev.carrier
        or_do_carrier.transistorB.chave = ha_new.carrier
        carrier = or_do_carrier.saida 
        return carrier, direita

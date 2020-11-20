from componente import Fulladder as Adder
from itertools import zip_longest

digitsA = input('Digite o primeiro número binário: ')
digitsB = input('Digite o segundo número binário: ')

carrier = 0
resultado = ''

for digitA, digitB in zip_longest(digitsA[::-1], digitsB[::-1], fillvalue='0'):
    adder1 = Adder(energia=1, received=carrier)
    adder1.inputA = int(digitA)
    adder1.inputB = int(digitB)
    direita = adder1.saidas[1]
    resultado = str(direita) + resultado
    carrier = adder1.saidas[0]
if carrier:
    resultado = str(carrier) + resultado

# print()
# print(digitsA.rjust(len(resultado)), str(int(digitsA, 2)).rjust(len(str(int(resultado, 2)))))
# print(digitsB.rjust(len(resultado)), str(int(digitsB, 2)).rjust(len(str(int(resultado, 2)))))
# print('-'*len(resultado), '-'*len(str(int(resultado, 2))))
# print(resultado, int(resultado, 2))

print(f'A soma foi: {resultado}')
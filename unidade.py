from componente import Fulladder as Adder, Fullsubtracter as Subtracter
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

print(f'A soma foi: {resultado}')


digitsA = str(0)
digitsB = str(0)

while int(digitsA, 2) <= int(digitsB, 2):
    digitsA = str.lstrip(input('Digite um minuendo binário: '),'0')
    digitsB = str.lstrip(input('Digite um subtraendo binário: '), '0')
borrowout = 0
resultado = ''

for digitA, digitB in zip_longest(digitsA[::-1], digitsB[::-1], fillvalue='0'):
    subtracter1 = Subtracter(energia=1)
    subtracter1.borrowin = borrowout
    subtracter1.inputA = int(digitA)
    subtracter1.inputB = int(digitB)
    direita = subtracter1.saidas[1]
    resultado = str(direita) + resultado
    borrowout = subtracter1.saidas[0]

print(f'A diferença foi: {resultado}')
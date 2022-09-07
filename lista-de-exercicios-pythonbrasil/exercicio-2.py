"""
classe Quadrado

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe.
Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos
e de rodapés necessárias para o local.
"""

class Square:
    def __init__(self, side_len):
        self.side_len = side_len

    def changeSideLen(self, side_len):
        self.side_len = side_len
        print(f'This is the new side lenght: {self.side_len}')

    def showSideLen(self):
        print(self.side_len)

    def calculateArea(self):
        area = self.side_len ** 2
        print(area)

s1 = Square(15)
s1.showSideLen()
s1.changeSideLen(20)
s1.showSideLen()
s1.calculateArea()



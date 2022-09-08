"""
Crie uma classe que modele um retangulo:

"""

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def showValue(self):
        print(f'my height is {self.height} and my width is {self.width}')

    def changeValue(self, height, width):
        self.height = height
        self.width = width
        print(f'my new height is {self.height} and my new width is {self.width}')

    def calculateArea(self):
        area_rectangle = self.height * self.width
        print(f'My area is {area_rectangle}')

    def calculatePerimeter(self):
        perimeter_rectangle = (self.height * 2) + (self.width * 2)
        print(f'My perimeter is {perimeter_rectangle}')


# Implementation

height = int(input('Digite a altura do retangulo: '))
width = int(input('Digite a largura do retangulo: '))

r1 = Rectangle(height, width)
r1.showValue()
r1.calculateArea()
r1.calculatePerimeter()

height = int(input('altere a altura do retangulo: '))
width = int(input('altere a largura do retangulo: '))
r1.changeValue(height, width)
r1.showValue()
r1.calculateArea()
r1.calculatePerimeter()

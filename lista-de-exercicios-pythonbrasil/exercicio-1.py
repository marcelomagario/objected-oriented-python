# Exercício 1 - Crie uma classe que modele uma bola
class Bola:
    pass

    # Atributos
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    # Metodos

    def trocaCor(self, cor):
        self.cor = cor
        print(f'a nova cor é: {self.cor}')

    def mostraCor(self):
        print(f'mostra a cor: {self.cor}')

# Implementação - Instanciação


# melão
melao = Bola('Amarela', 12, 'Plastico')
print(melao.cor, melao.circunferencia, melao.material)
melao.mostraCor()
melao.trocaCor('Verde')
melao.mostraCor()

# chumbo
chumbo = Bola('Preta', 14, 'Couro')
print(chumbo.cor, chumbo.circunferencia, chumbo.material)
chumbo.mostraCor()
chumbo.trocaCor('Prata')

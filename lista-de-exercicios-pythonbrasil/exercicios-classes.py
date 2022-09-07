# Exercício 1 - Crie uma classe que modele uma bola
class Bola:
    pass

    # Atributos
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    # Metodos

    def trocaCor(self):
        print('Aqui será a troca de cores')

    def mostraCor(self):
        print(f'mostra a cor: {self.cor}')

# Implementação - Instanciação
melao = Bola('Amarela', 12, 'Plastico')
chumbo = Bola('Preta', 14, 'Couro')

print(melao.cor, melao.circunferencia, melao.material)
melao.trocaCor()
melao.mostraCor()

print(chumbo.cor, chumbo.circunferencia, chumbo.material)
chumbo.trocaCor()
chumbo.mostraCor()

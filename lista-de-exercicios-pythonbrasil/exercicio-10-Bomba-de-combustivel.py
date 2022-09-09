# Bomba de Combustível e POO

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self):
        reais_abastecidos = float(input('Informe quantos reais vc quer abastecer R$ __,__ : '))
        qtde_litros = reais_abastecidos / self.valor_litro
        print(f'Foi colocado {qtde_litros}L no seu veículo. ')

    # def abastecerPorLitro(self):
    # def alterarValor(self):
    # def alterarCombustivel(self):
    # def alterarQuantidadeCombustivel(self):

 #implementação

texaco = BombaCombustivel('Diesel', 2.2, 100)
texaco.abastecerPorValor()

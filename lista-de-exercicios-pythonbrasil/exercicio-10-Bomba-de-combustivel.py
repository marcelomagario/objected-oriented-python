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
        self.quantidade_combustivel -= qtde_litros  # atualiza o level da bomba

    def abastecerPorLitro(self):
        litros_abastecidos = int(input('Informe quantos litros vc quer abastecer: '))
        custo_abastecimento = litros_abastecidos * self.valor_litro
        print(f'O valor a ser pago é de R$ {custo_abastecimento} ')
        self.quantidade_combustivel -= litros_abastecidos

    # def alterarValor(self):
    # def alterarCombustivel(self):
    # def alterarQuantidadeCombustivel(self):

 #implementação

texaco = BombaCombustivel('Diesel', 2.2, 100)
texaco.abastecerPorValor()
texaco.abastecerPorLitro()

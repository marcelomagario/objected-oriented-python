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

    def alterarValor(self):
        novo_preco = float(input('Informe o novo preço do combustível (R$/litro): '))
        self.valor_litro = novo_preco

    # def alterarCombustivel(self):
    # def alterarQuantidadeCombustivel(self):

 #implementação

print('#'*40)
print(f'Postão do canal 2')
print('#'*40)
print('Selecione a opção desejada')
opcao_do_usuario = int(input('1- Administrador, 2 - Frentista: '))
if opcao_do_usuario == 1:
    print('Menu')
    opcao_do_usuario = int(input('1 - Cadastrar nova bomba, 2 - Alterar preço: '))
    if opcao_do_usuario == 1:
        print('# Inserir aqui o método de cadastrar uma nova bomba')
    if opcao_do_usuario == 2:
        print('# Inserir aqui o método para alterar o preço do combustível')

if opcao_do_usuario == 2:
    print('# Inserir aqui todos os métodos do frentista')


# bomba1 = BombaCombustivel('Diesel', 2.2, 100)
# bomba1.abastecerPorValor()
# bomba1.abastecerPorLitro()
# bomba1.alterarValor()
# print(bomba1.__dict__)

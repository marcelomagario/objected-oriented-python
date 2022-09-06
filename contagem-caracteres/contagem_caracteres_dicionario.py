"""
- Algoritmo para avaliar uma string de entrada.
- Contar a quantidade de cada caracteres da string.
- Mostrar em ordem alfabética
    Ex.
    >>> contar_caracteres('marcelo')
    {'m': 1, 'a': 1, 'r': 1, 'c': 1, 'e': 1, 'l': 1, 'o': 1}
    >>> contar_caracteres('ovo')
    {'o': 2, 'v': 1}
    """


def contar_caracteres(s):
    """Função que conta caracteres de uma string"""
    resultado = {}
    for i in s:
        # pegar o resultado respectivo do i de dentro do dicionario, se ele não estiver lá irá retornar 0
        # a este resultado vc ira somar 1 e vai armazenar esse resultador novamente no dicionario[i]
        resultado[i] = resultado.get(i, 0) + 1
    return resultado

    # Solução mais newbie usando contador
    # resultado = {}
    # for i in s:
    #     contador = resultado.get(i, 0)
    #     contador += 1
    #     resultado[i] = contador






if __name__ == '__main__':
    print(contar_caracteres('marcelo'))
    print()
    print(contar_caracteres('banana'))



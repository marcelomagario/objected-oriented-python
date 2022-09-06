"""
- Algoritmo para avaliar uma string de entrada.
- Contar a quantidade de cada caracteres da string.
- Mostrar em ordem alfabética
    Ex.
    >>> contar_caracteres('marcelo')
    a = 1
    c = 1
    e = 1
    l = 1
    m = 1
    o = 1
    r = 1
    """

def contar_caracteres(s):
    """Função que conta caracteres de uma string"""
    caracteres_ordenados = sorted(s) # cria uma lista ordenada
    caracter_anterior = caracteres_ordenados[0]
    contador = 1
    for i in caracteres_ordenados[1:]:
        if i == caracter_anterior:
            contador += 1
        else:
            print(f'{caracter_anterior} = {contador}')
            caracter_anterior = i
            contador = 1
    print(f'{caracter_anterior} = {contador}')



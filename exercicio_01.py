# 1. Calcular Média de Valores em uma Lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def media_valores(lista: list)-> float:
    """
    Calcula a media dos valores de uma lista
    """
    media = sum(lista) / len(lista)
    return print(media)

media_valores(lista)

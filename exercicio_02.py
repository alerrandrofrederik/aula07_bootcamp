# 2. filtrar dados acima de um limite

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtra_valores_maiores_5(lista: list)-> list:
    """
    Filtrar Dados Acima de 5
    """
    valores_filtrados = []
    for i in lista:
        if i > 5:
            valores_filtrados.append(i)
    return valores_filtrados

print(filtra_valores_maiores_5(lista))




def ler_arquivo_csv(nome_arquivo: str) -> list:
    """
    Função para ler um arquivo CSV e retornar os dados como uma lista de dicionários.
    """
    import csv

    dados = []
    with open(nome_arquivo, mode = 'r', encoding='utf8') as arquivo:
        leitor = csv.DictReader(arquivo)
        # adicionar cada linha (um dicionário) à lista de dados
        for linha in leitor:
            dados.append(linha)
    return dados

def filtrar_vendas_entregues(lista: dict) -> list:
    """
    Função para filtra vendas entregues
    """

    dados = []
    for item in lista:
        if item['entregue'] == 'True':
            dados.append(item)
    return dados

def Soma_vendas_entregues(lista: dict) -> float:
    """
    Função para somar vendas entregues
    """

    total = 0
    for item in lista:
        total += float(item['price'])
    return total







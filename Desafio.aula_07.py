'''
Desafio.aula_07 - Soma de vendas entregues de um arquivo CSV, criadndo funções em outro arquivo'''

from etl import ler_arquivo_csv, filtrar_vendas_entregues, Soma_vendas_entregues

vendas = ler_arquivo_csv('vendas.csv')
lista_vendas_entregues = filtrar_vendas_entregues(vendas)
total_vendas_entregues = Soma_vendas_entregues(lista_vendas_entregues)
print(total_vendas_entregues)


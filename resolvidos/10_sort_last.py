# -*- coding: utf-8 -*-

"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.
"""

def sort_last(tuples):
    # transformando as tuplas em lista
    listTuples = list(tuples)
    # conforme a dica acima, foi usado uma função para obter a key, no caso uma lambda para trazer o último valor
    return sorted(listTuples, key=lambda value: value[-1], reverse=False)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = sort_last(value)

    if result == expected:
        print('Resultado correto!')
    else:
        print('Resultado incorreto!')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test([(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test([(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test([(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

# -*- coding: utf-8 -*-

"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    # Como existe o método extends para listar no python, basta adicionar os elementos da lista 2 sem repetilos e depois usar a função sorted
    list1.extend(list2)
    return sorted(list1)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,value2,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = linear_merge(value,value2)

    if result == expected:
        print('Resultado correto!')
    else:
        print('Resultado incorreto!')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(['aa', 'xx', 'zz'], ['bb', 'cc'],
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(['aa', 'xx'], ['bb', 'cc', 'zz'],
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(['aa', 'aa'], ['aa', 'bb', 'bb'],
         ['aa', 'aa', 'aa', 'bb', 'bb'])

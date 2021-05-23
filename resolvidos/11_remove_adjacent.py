# -*- coding: utf-8 -*-

"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    novaLista = []
    for num in nums:
        # adiciona na nova lista caso o último elemento da novaLista seja diferente do número, para não repetilos
        if (not novaLista or num != novaLista[-1]):
            novaLista.append(num)
    return novaLista


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = remove_adjacent(value)

    if result == expected:
        print('Resultado correto!')
    else:
        print('Resultado incorreto!')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test([1, 2, 2, 3], [1, 2, 3])
    test([2, 2, 3, 3, 3], [2, 3])
    test([], [])
    test([2, 2, 3, 3, 3, 2, 2], [2, 3, 2])

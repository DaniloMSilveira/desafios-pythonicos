# -*- coding: utf-8 -*-

"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""

def mix_up(a, b):
    return b[:2]+a[2:] + ' ' + a[:2]+b[2:]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,value2,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = mix_up(value,value2)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test('mix', 'pod', 'pox mid')
    test('dog', 'dinner', 'dig donner')
    test('gnash', 'sport', 'spash gnort')
    test('pezzy', 'firm', 'fizzy perm')

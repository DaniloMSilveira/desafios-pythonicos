# -*- coding: utf-8 -*-

"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s):
    if (len(s) < 2):
        return ''
    else:
        return s[:2] + s[-2:]              


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = both_ends(value)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test('spring', 'spng')
    test('Hello', 'Helo')
    test('a', '')
    test('xyz', 'xyyz')
    test('ab', 'abab')

# -*- coding: utf-8 -*-

"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    count = 0
    for word in words:
        if (len(word) >= 2 and word[0] == word[-1]):
            count += 1
    return count


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = match_ends(value)

    if result == expected:
        print('Resultado correto! ' + str(expected))
    else:
        print('Resultado incorreto! Valor esperado era: ' + str(expected))


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(['aaa', 'be', 'abc', 'hello'], 1)

# -*- coding: utf-8 -*-

"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""

def not_bad(s):
    if('bad' in s and 'not' in s):
        if(s.find('bad') > s.find('not')):
            newString = s[:s.find('not')] + 'good'
            if(s[-1] in '!.?'):
                newString += s[-1]
            return newString
        else:
            return s
    
    return s


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = not_bad(value)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test('This movie is not so bad', 'This movie is good')
    test('This dinner is not that bad!', 'This dinner is good!')
    test('This tea is not hot', 'This tea is not hot')
    test("It's bad yet not", "It's bad yet not")

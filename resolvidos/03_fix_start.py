# -*- coding: utf-8 -*-

"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""

def fix_start(s):
    firstCaracter = s[0]
    s = s[1::]
    s = firstCaracter + s.replace(firstCaracter, '*')
    return s


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = fix_start(value)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test('babble', 'ba**le')
    test('aardvark', 'a*rdv*rk')
    test('google', 'goo*le')
    test('donut', 'donut')
    test('avadakedabra', 'av*d*ked*br*')

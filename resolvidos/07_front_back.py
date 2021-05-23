# -*- coding: utf-8 -*-

"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def indexMeio(valor):
    if len(valor) % 2 == 0:
        return int(len(valor) / 2)
    else:
        return int(len(valor) / 2) + 1

def front_back(a, b):
    return a[:indexMeio(a)] + b[:indexMeio(b)] + a[indexMeio(a):] + b[indexMeio(b):]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,value2,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = front_back(value,value2)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test('abcd', 'xy', 'abxcdy')
    test('abcde', 'xyz', 'abcxydez')
    test('Kitten', 'Donut', 'KitDontenut')

# -*- coding: utf-8 -*-

"""
01. donuts

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""

def donuts(count):
    if (count >= 10):
        return 'Number of donuts: many'
    else:
        return 'Number of donuts: ' + str(count)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = donuts(value)

    if result == expected:
        print('Resultado correto! ' + expected)
    else:
        print('Resultado incorreto! Valor esperado era: ' + expected)
        

if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(4, 'Number of donuts: 4')
    test(9, 'Number of donuts: 9')
    test(10, 'Number of donuts: many')
    test(99, 'Number of donuts: many')

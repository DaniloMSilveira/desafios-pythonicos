# -*- coding: utf-8 -*-

"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""

def front_x(words):
    lista1 = []
    lista2 = []
    for word in words:
        if (word[0] in 'x'):
            lista1.append(word)
        else:
            lista2.append(word)
    return sorted(lista1) + sorted(lista2)

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
# Foi reescrito a função de teste visto que a original não funcionava
def test(value,expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    result = front_x(value)

    if result == expected:
        print('Resultado correto!')
    else:
        print('Resultado incorreto!')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

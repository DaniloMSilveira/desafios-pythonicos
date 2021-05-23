# -*- coding: utf-8 -*-

"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys

def get_words_qtd(filename): 
    # criando dicionário, visto que guarda chave e valor, onde chave é a palavra e valor é a qtd
    words = {}
    with open(filename) as file:
        text = file.read().lower().split()

    # esse laço ira percorrer cada palavra do array "text" criado acima com split e adicionar na listagem de words
    for word in text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words

# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename):
    words = get_words_qtd(filename)

    # segundo parametro é a quantidade
    # items é necessário para não ocorrer exception de "too many values to unpack"
    for word, qtd in sorted(words.items()):
        print(word, qtd)


def print_top(filename):
    words = get_words_qtd(filename)

    top = {}
    # invertendo o dicionário para chave ser a quantidade e o valor ser a palavra, para depois criar lista ordenada
    for word, qtd in words.items():
        top[qtd] = word

    # Podemos usar o [:20] para os primeiros resultados. O procedimento na lista é igual em uma string, visto que uma string é uam lista de caracteres
    lista = list(sorted(top.items(), reverse=True))[:20]
    for word in lista:
        print(str(word[1]) + ' ' + str(word[0]))

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()

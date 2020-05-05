"""Os mapas são estruturas de dados que são chamadas de estruturas associativas. Estas estruturas possuem esse nome
pois permitem associar um valor de acesso a um determinado elemento. Um exemplo é o dicionario, onde procura-se
uma palavra e entao ver seu significado. E assim como no dicionario nao tem palavras repetidas, o mesmo vale para a
estrutura mapas. Logo as chaves em um mapa não podem ser duplicadas."""


class Associacao():
    def __init__(self, chave, valor):  # criar uma associacao da chave com  o valor
        self.__chave = chave
        self.__valor = valor

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return f'{self.__chave} {self.__valor}'

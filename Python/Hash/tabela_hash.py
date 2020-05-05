'''Tabela hash é uma estrutura de dados que associa achaves de pesquisa a valores. Dessa forma, tem como objetivo
fazer busca rapida a partir de uma chave simpes e obter o valor desejado.'''

# importar o arquivo lista ligada. Sera usado uma lista ligada para cada categoria
# e tabem listas ligadas para armazenar os elementos de certa categoria
from Listas.Listas_ligadas import ListaLigada


class TabelaHash():
    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numeroCategorias = 10  # numero de categorias para a tabela
        self.__tamanho = 0  # o tamanho da tabela

        for i in range(self.__numeroCategorias):  # for para percorrer o numero de categorias da tabela
            self.__elementos.inserir(ListaLigada())  # inserir uma lista para armazenar o elementos da categoria

    @property
    def tamanho(self):
        return self.__tamanho

    def __gerar_numero_hash(self, elemento):
        # gera um hash pro elemento, divide por 10 e retorna o resto da divisao. nunca sera gerado um numero maior
        # que o numero de categorias
        return hash(elemento) % self.__numeroCategorias

    def contem(self, elemento):
        numero_hash = self.__gerar_numero_hash(elemento)  # gera um hash e joga na variavel
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)  # recupara a categoria do elemento
        return categoria.cotem(elemento)  # verifica se o elemento passado como paramentor esa na categoria

    def inserir(self, elemento):
        if self.contem(elemento):  # verifica se o elemento existe. Caso sim retorna false
            return False
        # gera uma hash do elemento para ver qual categoria se enquadra
        numero_hash = self.__gerar_numero_hash(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)  # recupera a categoria
        categoria.inserir(elemento)  # insere o elemento
        self.__tamanho += 1  # incrementa o tam da tabela
        return True

    def remover(self, elemento):
        numero_hash = self.__gerar_numero_hash(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)
        categoria.remover_elemento(elemento)
        self.__tamanho -= 1

    # metodo para retornar todos os elementos da tabela de espalhamento
    def __str__(self):
        return self.__elementos.__str__()

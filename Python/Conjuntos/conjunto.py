"""Os sets (também conhecidos como conjuntos) são estruturas de dados muito similares às listas ligadas com uma 
única diferença: não é possível adicionar elementos duplicados.Quando um set recebe um elemento a ser inserido e 
este já possui em seu conjunto, o set não é modificado e nenhuma exceção é lançada. """

"""usaremos listas ligadas para implementacao de sets. Quase todas as funcoes sao as mesmas com excecao dos 
metodos de inserção"""
from Listas.Listas_ligadas import ListaLigada


class Conjunto():
    def __init__(self):
        self.__elementos = ListaLigada()

    def inserir(self, elemento):
        # verificar se o elemento nao esta no conjunto para poder inserir
        if not self.contem(elemento):  # se o metodo contem retorna falso, entra na condição
            self.__elementos.inserir(elemento)
            return True  # Retorna True caso o elemento tenha sido inserido com sucesso
        return False  # nao conseeguiu inserir retorna falso

    def inserir_posicao(self, posicao, elemento):
        # mesma logica do metodo inserir
        if not self.contem(elemento):
            self.__elementos.inserir_posicao(elemento, posicao)
            return True
        return False

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.cotem(elemento)

    def indice(self, elemento):
        return self.__elementos.indice(elemento)

    def estar_vazia(self):
        return self.__elementos.estar_vazia()

    def recuperar_elemento_no(self, posicao):
        return self.__elementos.recuperar_elemento_no(posicao)

    def recuperar_no(self, posicao):
        return self.__elementos.recuperar_no(posicao)

    def tamanho(self):
        return self.__elementos.tamanho

    def remover_posicao(self, posicao):
        self.__elementos.remover_posicao(posicao)

    def remover_elementos(self, elemento):
        self.__elementos.remover_elemento(elemento)


# Testando os metodos
teste = Conjunto()
teste.inserir(1)
teste.inserir(2)
teste.inserir(4)
teste.inserir(8)
teste.remover_elementos(8)
print(teste.inserir_posicao(1,3))
print(teste)
from Listas import Listas_dupl_ligadas


class Pilha():
    def __init__(self):
        self.__elementos = Listas_dupl_ligadas.ListaDuplamenteLigada()

    # metodo verifica se esta vazia
    def esta_vazia(self):
        return self.__elementos.estar_vazia()  # metodo da lista dupl encadeada

    # metodo adciona um elemento no topo da pilha
    def empilhar(self, elemento):
        # chama o metodo inseriri da lista dupl ligada, pois ela insere do mesmo jeito que uma pilha
        self.__elementos.inserir(elemento)

    # metodo retira um elemento do topo da pilha
    def desempilhar(self):
        if self.esta_vazia():
            return None
        # recuperar o elemento do topo da pilha e armazena na variavel resultado
        resultado = self.__elementos.recuperar_elemento_no(self.__elementos.tamanho - 1)
        self.__elementos.remover_posicao(self.__elementos.tamanho - 1)
        return resultado


teste = Pilha()
teste.empilhar(3)
teste.empilhar(5)
teste.empilhar(7)
print(teste.desempilhar())

from Arvores.No_arvore_inteiro import NoArvoreInteiro


class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if self.__raiz is None:
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)  # chama o metodo para inserir caso haja elementos nos Nós filhos

    # metodo para usar de modo recursivo para inserir na arvore
    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():  # se novo no é maior q o da raiz
            if referencia.no_direito is None:  # verifica se o lado direito esta vazio para poder inserir
                referencia.no_direito = novo_no
            else:
                # chama inserir passando como referencia o no direito. logo percorre a arvore ate
                # encontrar o lugar vazio para inserir
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo is None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)

    def buscar(self, no_busca):
        # chama o metodo buscar, passa a raiz como referencia e o no que se deseja buscar
        return self.__buscar(self.__raiz, no_busca)

    def __buscar(self, referencia, no_buscado):
        if referencia.valor == no_buscado.valor:  # verifica se o valor do no e o requerido
            return referencia
        else:
            # direita da arvore
            if referencia.peso() < no_buscado.peso():  # verifica se o no é menor q o nó passado
                if referencia.no_direito is None:  # verifica se o nó da direita é nulo
                    raise ValueError("elemento nao encontrado")
                else:
                    return self.__buscar(referencia.no_direito, no_buscado)  # vai para o lado direito da arvore
            # esquerda do arvore
            else:
                if referencia.no_esquerdo is None:
                    raise ValueError("Elemento nao encontrado")
                else:
                    # vai para o lado esquerdo passando o no esq como o novo no de referencia
                    return self.__buscar(referencia.no_esquerdo, no_buscado)

    # metodo para imprimir de maneira em ordem - ERD(esq,raiz,dir)
    def em_ordem(self):
        self.__em_ordem(self.__raiz)

    def __em_ordem(self, referencia):
        if referencia.no_esquerdo is not None:
            self.__em_ordem(referencia.no_esquerdo)
            print(referencia.valor.__str__())
            if referencia.no_direito is not None:
                self.__em_ordem(referencia.no_direito)
        else:
            print(referencia.valor.__str__())
            if referencia.no_direito is not None:
                self.__em_ordem(referencia.no_direito)

    # metodo para imprimir de maneria pre ordem - RED(raiz,esq,dir)
    def pre_ordem(self):
        self.__pre_ordem(self.__raiz)

    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.no_esquerdo is not None:  # lado esquerdo da arvore
            self.__pre_ordem(referencia.no_esquerdo)
            if referencia.no_direito is not None:
                self.__pre_ordem(referencia.no_direito)
        else:
            if referencia.no_direito is not None:  # lado direito da arvore
                self.__pre_ordem(referencia.no_direito)

    # metodo para imprimir de maneira pos-ordem - EDR(esq,dir,raiz)
    def pos_ordem(self):
        self.__pos_ordem(self.__raiz)

    def __pos_ordem(self, referencia):
        if referencia.no_esquerdo is not None:  # anda do lado esq da arvore
            self.__pos_ordem(referencia.no_esquerdo)
            if referencia.no_direito is not None:
                self.__pos_ordem(referencia.no_direito)
            print(referencia.valor.__str__())
        else:
            if referencia.no_direito is not None:  # anda do lado direito da arvore
                self.__pos_ordem(referencia.no_direito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())

    # metodo para calcular altura da arvore
    def altura(self):
        return self.__altura(self.__raiz)

    def __altura(self, referencia):
        if referencia is None:
            return -1
        altura_esquerda = self.__altura(referencia.no_esquerdo)
        altura_direita = self.__altura(referencia.no_direito)
        return (altura_esquerda + 1) if altura_esquerda > altura_direita else (altura_direita + 1)

    # metodo para imprimir a arvore
    def __str__(self):
        return "[(X)]" if self.__raiz is None else self.__raiz.__str__()


# ---------------TESTE-----------------#
teste = Arvore()
teste.inserir_elemento(NoArvoreInteiro(7))
teste.inserir_elemento(NoArvoreInteiro(6))
teste.inserir_elemento(NoArvoreInteiro(4))
teste.inserir_elemento(NoArvoreInteiro(5))
teste.inserir_elemento(NoArvoreInteiro(10))
teste.inserir_elemento(NoArvoreInteiro(9))
teste.inserir_elemento(NoArvoreInteiro(12))
print("Em ordem")
print(teste.em_ordem())
print("Pré-ordem")
print(teste.pre_ordem())
print("Pós-ordem")
print(teste.pos_ordem())
print("Altura da arvore: {}".format(teste.altura()))
# print(teste)
# print(teste.buscar(NoArvoreInteiro(3)))

from Listas.No import No


class ListaLigada():
    def __init__(self):
        self.__primeiro_no = None  # Primeiro No da lista
        self.__ultimo_no = None  # Guardar a refe do ultimo nó inserido
        self.__tamanho = 0  # Contador para controle do tam da lista

    @property
    def tamanho(self):
        return self.__tamanho

    # metodo para verificar se a lista esta vazia
    def estar_vazia(self):
        return self.__tamanho == 0

    # metdo que vai imprimir a lista
    def __str__(self):
        temp = self.__primeiro_no  # temp armazena o primeiro no da lista
        elementos = '['  # guardar os elementos percorridos
        while temp is not None:  # percorre a lista equanto nao achar o elemetno nulo, ou seja, o ultimo
            elementos = f'{elementos} {temp.elemento}'  # concatenas os elementos
            temp = temp.proximoNo  # passa para o proximo no
        elementos = f'{elementos} ]'
        return elementos  # retorna a variavel elementos q contem todos os elementos da lista

    # metodo para inserir um novo elemento na lista
    def inserir(self, elemento):
        novo_no = No(elemento)  # Cria um novo no, sem nenhuma ligaçao
        if self.estar_vazia():  # Verifica se a lista esta vazia
            # novo_no passara a ser o primeiro no da lista e tambem o ultimo no por ser o unico no na lista
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            # caso a lista n estaja vazia, o no inserido passara a ser o ultimo no da lista
            self.__ultimo_no.proximoNo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1  # incrementa o tamanho da lista

    def inserir_posicao(self, elemento, posicao):
        # se a posicao passda for 0 significa q insere no inicio
        if posicao == 0:
            novo_no = No(elemento)  # cria um novo No
            novo_no.proximoNo = self.__primeiro_no  # novo No aponta pro primeiro No atual da lista
            self.__primeiro_no = novo_no  # novo no passa a ser o primeiro no da lista

        # se quiser inserir no fim da lista
        elif posicao == self.__tamanho:  # se a piscao passada for igual ao tamanho da ista
            novo_no = No(elemento)
            self.__ultimo_no.proximoNo = novo_no  # nultimo No atual da lista passa a pontar para o novo No
            self.__ultimo_no = novo_no  # Novo No é setado como sendo o ultimo no da lista

        # significa que temos que pegar a posicao anterior a passada e a posicao apos a posicao passada
        else:
            no_anterior = self.recuperar_no(posicao - 1)  # recupara o no anterior da posicao q se deseja inserir
            no_atual = self.recuperar_no(posicao)  # recupera a posicao onde se deseja inserir
            novo_no = No(elemento)  # cria novo No
            no_anterior.proximoNo = novo_no  # faz o no anteriro apontar pro novo No
            novo_no.proximoNo = no_atual  # novo No aponta pro proximo No que era o no atual
        self.__tamanho += 1

    def cotem(self, elemento):
        for i in range(self.__tamanho):  # percorre o vetor
            no_atual = self.recuperar_no(i)  # no atual recebe o no do range atual
            if no_atual.elemento == elemento:  # se encontrado retora True
                return True
        return False  # retorna False caso n encontre

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i  # retorna o indice do elemento
        return -1

    # metodo para recuparar o elemento do No na lista
    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)  # usa a funcao recuperar_no para pegar o no da posicao passada
        if no is not None:
            return no.elemento
        return None

    # metodo para recupeara um no completo
    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao + 1):  # percorre a lista ate a posicao passado, caso essa exista
            if i == 0:  # significa q é a primeiro NO da lista
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximoNo  # anda para o prox No ate a posicao especificada(caso exista)
        return resultado

    # metodo para remover um No da lista
    def remover_posicao(self, posicao):
        # caso o no a ser removido sejo o primeiro da lista
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximoNo  # pega a referencia do segundo no para poder rm o primeiro
            self.__primeiro_no = None  # o valor do primero No passa a ser None
            self.__primeiro_no = proximo_no  # o segundo No passa a ser o primero da lista
        # caso queira rmover o ultimo No
        elif posicao == self.__tamanho - 1:
            penultimo_no = self.recuperar_no(self.__tamanho - 2)  # pega a referencia do penultimo no da lista
            penultimo_no.proximoNo = None  # faz o penultimo no apontar para nulo
            self.__ultimo_no = penultimo_no  # atribui ao penultimo No a funcao de ultimo no
        # remover um elemento que tenha no antes e depois
        else:
            no_remover = self.recuperar_no(posicao)  # pega o no da posicao desejada
            no_anterior = self.recuperar_no(posicao - 1)  # pega o No anterior
            no_anterior.proximoNo = no_remover.proximoNo  # faz o no anterior apontar para o No seguinte ao da posicao
            no_remover.proximoNo = None  # atrui None ao no que se deseja remover .python limpa
        self.__tamanho -= 1  # decrementa o tam da lista ja que removeu-se um No

    def remover_elemento(self, elemento):
        no_remover = self.indice(elemento)  # chama a funcao indice para pegar a posicao do elemento
        if no_remover != -1:
            self.remover_posicao(no_remover)  # chama o metodo remover e passa o no_remover que contem a posicao do no
        else:
            print("Elemento nao existe")

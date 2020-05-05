class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        return ' '.join([ str(i) for i in self.__elementos]) #conatenando um espaço em branco com cada elemento

    def contem(self,elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return True
        return False

    def indice(self,elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return i
        return -1

    def inserir_elemento_posicao(self, elemento, posicao):
        # 1,2,3 | 1,2,3,4 | 1,2,4=vetor_ini | 3=vetor_fin
        vetor_ini = self.__elementos[:posicao] + [None]  # 1,2,[None]
        vetor_fin = self.__elementos[posicao:]
        vetor_ini[len(vetor_ini) - 1] = elemento
        self.__elementos = vetor_ini + vetor_fin
        self.__posicao += 1

        self.__elementos[posicao] = elemento

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.tamanho_vetor():
            self.__elementos = self.__elementos + [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elem_posicao(self,posicao):
        vetor_inicio = self.__elementos[:posicao]
        vetor_final = self.__elementos[posicao+1:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao -= 1

    def remover_elemento(self,elemento):
        posicao = self.indice(elemento)
        self.remover_elem_posicao(posicao)

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]

#resposta do desafio 1
'''class Vetor():
    def __init__(self):
        self.__elementos = []

    def __str__(self):
        return '\n'.join([ str(i) for i in self.__elementos])

    def inserir_elemento(self, elemento):
        self.__elementos = self.__elementos + [elemento]'''
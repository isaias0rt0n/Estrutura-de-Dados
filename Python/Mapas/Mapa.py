from Listas.Listas_ligadas import ListaLigada
from Mapas.Associacao import Associacao

""" mapas similiar a tabela hash. a dierença é que ao inves de inserir elementos arbitrario, gera-se o hash 
apartirda chave, insere a associacao dentro da categoria. Dessa forma todos elementos estarao associados a 
uma chave e essa chave categorizada pelo seu hash."""


# 0: ("par", 10)
# 1: 15,20
# 2: (150:200)


class Mapa():
    def __init__(self):
        self.__elementos = ListaLigada()
        self.__numero_categorias = 10

        # criar uma nova lista ligada para associar os elementos ao seu respectivo indice
        for i in range(self.__numero_categorias):
            self.__elementos.inserir(ListaLigada())

    # gerar um hash para a chave
    def gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__numero_categorias

    def contem(self, chave):
        numero_hash = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)
        for i in range(categoria.tamanho):  # percorrer toda a lista da categoria
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:  # verifica se a chave da associacao do range e a passada por parametro
                return True
        return False

    # metodo remover elemento apartir da sua chave
    def remover(self, chave):
        numero_hash = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)  # obter a categoria da chave
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                categoria.remover_elemento(associacao)  # remove tda a associação da lista da categoria encontrada
                return True
        return False

    # metodo para inserir mapa
    def adcionar(self, chave, valor):
        if self.contem(chave):  # verifica se ja existe a chave no mapa
            self.remover(chave)  # se existir, remove a associação dessa chave
        numero_hash = self.gerar_numero_espalhamento(chave)  # gerar uma hash apartir da chave
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)  # obter a categoria q se encaixa
        categoria.inserir(Associacao(chave, valor))  # inserir a associaco nessa determinada categoria

    # recuperar uma associacao apartir da chave
    def recuperar(self, chave):
        numero_hash = self.gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar_elemento_no(numero_hash)
        for i in range(categoria.tamanho):
            associacao = categoria.recuperar_elemento_no(i)
            if associacao.chave == chave:
                return associacao.valor  # retorna o valor da associacao
        return False

    def __str__(self):
        temp = self.__elementos.__str__()
        return temp


# ---------------TESTE---------------#
mapa = Mapa()

print(mapa)
mapa.adcionar("par", 10)
mapa.adcionar("impar", 5)
mapa.adcionar("par", 2)
mapa.adcionar("impar", 1)
mapa.remover("impar")
print(mapa)
print(mapa.contem("par"))
print(mapa.recuperar("par"))

'''Dada uma lista de telefone, com nome e número, exiba o nome e o número da pessoa informada ou "Não achado".

Inicialmente você receberá uma lista, a lista de telefone, com o nome e número. Em seguinda receberá o nome do contato que deve ser localizado na lista de telefone.

O código precisa implementar uma classe Mapa, que utiliza a classe ListaLigada fornecida e implementa um mapa.

Entrada de dados:

3
uncle sam
99912222
tom
11122222
harry
12299933
3
uncle sam
uncle tom
harry
Saída esperada

uncle sam=99912222
Não achado
harry=12299933'''

#resposta

'''import re
import inspect

class No():
    def __init__(self, val):
        self.val = val
        self.prox = None

class ListaLigada():
    
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def remover(self, valor):
        if(self.cabeca != None and self.cabeca.prox != None):
            aux = self.cabeca

            while(aux.prox != None):
                if(aux.prox.val == valor):
                    val = aux.prox.val
                    aux.prox = aux.prox.prox
                    self.tamanho -=1
                    return val
        
                aux = aux.prox

            return None
        elif(self.cabeca != None):
            valor = self.cabeca.val
            self.cabeca = None
            self.tamanho -=1
            return valor
        else:
            return None
    
    def inserir(self, valor):
        if(self.cabeca == None):
            self.cabeca = No(valor)
            self.tamanho+=1
        else:
            aux = self.cabeca
            
            while(aux.prox != None):
                aux = aux.prox
                
            aux.prox = No(valor)
            self.tamanho+=1

    def recuperar(self, index):
        if(index > self.tamanho):
            return None
        else:
            aux = self.cabeca
            i = 0
            while(i < index and aux.prox != None):
                aux = aux.prox
                i+=1

            return aux.val
    
    def contem(self, valor):
        aux = self.cabeca
        while(aux != None):
            if(aux.val == valor):
                return True
                
            aux = aux.prox
        
        return False
    
    def exibir(self):
        aux = self.cabeca
        
        while(aux != None):
            print(aux.val)
            aux = aux.prox
    
    def get_tamanho(self):
        return self.tamanho

class Mapa():

    def __init__(self):
        self.__elementos = ListaLigada()
        self.__quantidade_categorias = 16

        for i in range(0, self.__quantidade_categorias):
            self.__elementos.inserir(ListaLigada())

    def contem_chave(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                return True
        
        return False

    def remover(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                categoria.remover(associacao)
                return

        raise Exception("A chave {} não existe".format(chave))

    def adicionar(self, chave, valor):
        if (self.contem_chave(chave)):
            self.remover(chave)
    
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)
        categoria.inserir(Associacao(chave, valor))

    def recuperar(self, chave):
        numero_espalhamento = self.__gerar_numero_espalhamento(chave)
        categoria = self.__elementos.recuperar(numero_espalhamento)

        for i in range(0, categoria.get_tamanho()):
            associacao = categoria.recuperar(i)
            if (associacao.chave == chave):
                return associacao.valor

        raise Exception("A chave {} não existe".format(chave))

    def __str__(self):
      return "Mapa [elementos={}]".format(self.__elementos)

    def __gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__quantidade_categorias

class Associacao ():

    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor

    @property
    def chave(self):
      return self.__chave

    @property
    def valor(self):
      return self.__valor

    def __str__(self):
      return "Associacao: {} - {}".format(self.__chave,self.__valor)

def processa_mapa():
  
    t = int(input())
  
    mapa = Mapa()
    for i in range(0,t):
        nome = input()
        telefone = input()
        
        mapa.adicionar(nome, telefone)

    t = int(input())
    for i in range(0,t):
        nome = input()
        if(mapa.contem_chave(nome)):
            print("{}={}".format(nome,mapa.recuperar(nome)))
        else:
            print("Não achado")

if __name__ == "__main__":

    filtro = {k: v for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k) }

    if not "Mapa" in filtro:
        print("É necessário declarar uma classe Mapa")
        quit()

    obj = Mapa()

    membro = [member for _name, member in inspect.getmembers(obj) if isinstance(member,ListaLigada)]

    if(len(membro) < 1):
        print("A classe deve implementar uma tabela de espalhamento com lista ligada")

    processa_mapa()'''
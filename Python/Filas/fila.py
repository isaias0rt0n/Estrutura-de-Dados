from Listas.Listas_ligadas import ListaLigada


class Fila():
    def __init__(self):
        self.__elementos = ListaLigada()

    # metodo verifica se esta vazia
    def esta_vazia(self):
        self.__elementos.estar_vazia()

    # metodo inserir na fila
    def enfileirar(self, elemento):
        self.__elementos.inserir(elemento)  # insere sempre no fim da fila

    # metodo remove da fila
    def desenfileirar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(0)  # pega o primeiro elemento da fila
        self.__elementos.remover_posicao(0)  # remove o elemento do inicio da fila
        return resultado  # retorna o elemento desenfileirado

    # metodo para retornar todos os elementos da fila / sobreescreve o metodo str presente na lista ligada
    def __str__(self):
        temp = self.__elementos.__str__()
        return temp


teste = Fila()
teste.enfileirar(1)
teste.enfileirar(2)
teste.enfileirar(4)
teste.enfileirar(8)
teste.enfileirar(16)
teste.enfileirar(32)
teste.enfileirar(64)
teste.desenfileirar()
teste.desenfileirar()

print(teste)









'''Balanceada
Balanceada
Não balanceada
Balanceada


import re
import inspect

class No():
    def __init__(self, val):
        self.val = val
        self.prox = None

class Fila():
    def __init__(self):
        self.cabeca = None
      
    def remove(self):
        if (self.cabeca != None and self.cabeca.prox != None):
            aux = self.cabeca
            valor = aux.val
            self.cabeca = aux.prox
            return valor
        elif (self.cabeca != None):
            valor = self.cabeca.val
            self.cabeca = None
            return valor
        else:
            return None
      
    def inserir(self,valor):
        if(self.cabeca == None):
            self.cabeca = No(valor)
        else:
            aux = self.cabeca
            while(aux.prox != None):
                aux = aux.prox;

            aux.prox = No(valor)
    
    def exibir(self):
        aux = self.cabeca
          
        while(aux != None):
            print(aux.val)
            aux = aux.prox


def analisa_fila(fila):
  
    if(fila != None):
        caractere = fila.remove()
        parentese = 0
        chave = 0
        colchete = 0
        while(caractere != None):
            if (caractere == "("):
                parentese+=1
            elif (caractere == ")"):
                if(parentese==0):
                    return False
                else:
                    parentese-=1
            elif (caractere == "["):
                colchete+=1
            elif (caractere == "]"):
                if(colchete==0):
                    return False
                else:
                    colchete-=1
                break;
            elif (caractere == "{"):
                chave+=1
            elif (caractere == "}"):
                if(chave==0):
                    return False
                else:
                    chave-=1
            else:
                return False

            caractere = fila.remove()
            

        if(chave == 0 and parentese == 0 and colchete == 0):
            return True;
        else:
            return False
  
    return False

def analisa_string():

    n = int(input())
    for i in range(0, n):
        fila = Fila()
        linha = input()
        for car in linha:
            
            if(car != "\n" and len(car) != 0):
                fila.inserir(car)

        print("Balanceada" if analisa_fila(fila) else "Não balanceada")

def generate_call(obj):
    name = obj.__name__
    args = "( "
    for i in range(1, obj.__code__.co_argcount):
        args += "0,"
        
    args = args[:-1] + ")"
    return name.strip() + args

if __name__ == "__main__":

    filtro = {k: v for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k) }

    if not "Fila" in filtro:
        print("É necessário declarar uma classe Fila")

    for classe in filtro:
        if not inspect.ismodule(filtro[classe]) and inspect.isclass(filtro[classe]):
            args = "( "
            for i in range(1, vars(filtro[classe])["__init__"].__code__.co_argcount):
                args += "0,"
            
            args = args[:-1] + ")"
            
            obj = eval(filtro[classe].__name__ + args)
            
            metodos = {k: v for k, v in dict(inspect.getmembers(obj, inspect.ismethod)).copy().items() if not re.search(r'\b__\w+__\b', k) }
            for nome in metodos:
                metodo = generate_call(metodos[nome])
                if metodo != None:
                  eval("obj." + metodo)
            
            membros = {k: v for k, v in dict(inspect.getmembers(obj)).copy().items() if not re.search(r'\b__\w+__\b', k) }
            for nome in membros:

                if isinstance(membros[nome], (list, tuple)):
                    print ("Um membro da classe não pode ser dos tipos list ou tuple")

    analisa_string()'''
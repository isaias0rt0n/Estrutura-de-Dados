# Classe que cria a estrutura do No
class No():
    def __init__(self, elemento, proxNo=None):
        self.__elemento = elemento
        self.__proxNo = proxNo

    @property
    def elemento(self):
        return self.__elemento

    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def proximoNo(self):
        return self.__proxNo

    @proximoNo.setter
    def proximoNo(self, proximoNo):
        self.__proxNo = proximoNo

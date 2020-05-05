# Classe que cria a estrutura do No
class NoDuplamenteLigada():
    def __init__(self, elemento, proxNo=None, anteNo=None):
        self.__elemento = elemento
        self.__proxNo = proxNo
        self.__anteNo = anteNo

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

    @property
    def anteNo(self):
        return self.__anteNo

    @anteNo.setter
    def anteNo(self, anterior):
        self.__anteNo = anterior

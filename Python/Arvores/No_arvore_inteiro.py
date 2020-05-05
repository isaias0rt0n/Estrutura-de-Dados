from Arvores.No_arvore import NoArvore


class NoArvoreInteiro(NoArvore):
    def __init__(self, valor):
        super().__init__(valor)

    def peso(self):
        return self.valor  # como e valores int, o peso é o proprio valor

listas_inteiros = [1, 2, 4, 6, 8, 10, 12]

meu_iter = iter(listas_inteiros)

print(next(meu_iter))
print(next(meu_iter))

class Iteretor:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            resultado = 2 ** self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration

for i in Iteretor(5):
    print(i)
def eleva_dois(maximo=0):
    n = 0
    while n < maximo:
        # yield - responsável por, além de retornar os elementos, guardar o estado atual de uma coleção de elementos
        yield 2 ** n
        n += 1


for i in eleva_dois(5):
    print(i)

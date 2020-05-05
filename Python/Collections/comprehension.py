listas_inteiros = [1, 2, 4, 8, 16, 32, 64]

# metodo usando for
print("Usando for")
nova_lista = []
for i in listas_inteiros:
    nova_lista.append(i * i)
print(nova_lista)

# metodo usando comprehension
print("Usando comprehension")
new_lista = [i + i for i in listas_inteiros]
print(new_lista)

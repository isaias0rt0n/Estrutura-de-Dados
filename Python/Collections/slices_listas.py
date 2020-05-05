lista_simples = [1, 2, 4, 16, 256, 4096]

print(lista_simples[:3])
print(lista_simples[2:5])
print(lista_simples[2:])
sub_lista = lista_simples[3:5]
print(sub_lista)

# usando slice
new_lista = slice(0, 4)
print(lista_simples[new_lista])
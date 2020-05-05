import copy

nested_list = [[0, 1, 2], ["A", "B", "C"], [True, False]]

# Deep Copy
nova_lista = copy.deepcopy(nested_list)
nested_list[0][1] = 3
print(nova_lista)
print(nested_list)

# shallow Copy - copya a referencia
outra_lista = copy.copy(nested_list)
nested_list[0][2] = 5
print("\n", outra_lista)
print(nested_list)

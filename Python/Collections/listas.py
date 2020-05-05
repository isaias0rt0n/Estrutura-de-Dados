listas_inteiro = [1, 2, 3, 4]
listas_strings = ["ab", "cd", "ef"]
listas_mescladas = [1, "ola", True, 2.5]
nested_list = [[1, 2], ["ola", "eu"]]  # listas dentro de listas

listas_inteiro.append(5)  # insere no fim
listas_inteiro.insert(2, 9)  # insere em uma posicao

listas_inteiro.remove(1)

count = listas_inteiro.count(2)  # conta quantos elementos 2 a na lista
print(count)
print(listas_inteiro)
listas_inteiro.sort(reverse=True)  # ordena a lista do maior para o menor
print(listas_inteiro)

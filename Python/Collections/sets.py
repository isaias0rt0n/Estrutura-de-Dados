meu_set = {1, 2, 3, 4, 1}
meu_set2 = set([4, 7, 8, 9, 10])

print(type(meu_set2))

# add()
meu_set.add(2)

# update()
meu_set.update([3, 4, 5, 6])

# discard() - remover
meu_set.discard(1)

# uniao
print(meu_set | meu_set2)
print(meu_set.union(meu_set2))

# Interseção
print(meu_set & meu_set2)
print(meu_set.intersection(meu_set2))

# Diferença
print(meu_set.difference(meu_set2))

# Diferença Simétrica - exclui o q é em comum entre eles
print(meu_set ^ meu_set2)
print(meu_set.symmetric_difference(meu_set2))

print(meu_set)

# --------------------------------------------------------------
print("-" * 30)
print("Criando um set comprehensions")

set_1 = {1, 2}
set_2 = {3, 4}

set_comprehension = {i * i for i in range(0, 10)}
print(set_comprehension)

set_comprehension2 = {i for i in set_1.union(set_2)}
print(set_comprehension2)
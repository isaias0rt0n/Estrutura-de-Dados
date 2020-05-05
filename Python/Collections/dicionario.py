meu_dic = {1: "isac", 2: "joao", 3: "ezequiel"}
print(meu_dic)

for chave, valor in meu_dic.items():
    print("A chave é {} e o valor é {}".format(chave, valor))

# -------------------OPERAÇÕES-------------------#
print("=-=" * 15)
meu_dicionario = {1: "isaias", 2: "olavo", 3: "jose", 4: "girl"}
meu_dicionario_v2 = {'nome': 'isaias', 'sobrenome': 'carmo', 'idade': 50, 'profissao': 'estudante'}

# get()
print(meu_dicionario.get(2))
# len()
print(len(meu_dicionario))
# pop()
meu_dicionario.pop(2)
print(meu_dicionario)
# clear()
# meu_dicionario.clear()
# keys()
print(meu_dicionario.keys())

# Adcionando elementos
meu_dicionario[2] = 'olavo'
meu_dicionario_v2.update({'profissao': 'hacker'})

print(meu_dicionario)
print(meu_dicionario_v2)
from Listas.Listas_ligadas import ListaLigada
from Listas.Listas_dupl_ligadas import ListaDuplamenteLigada

print(30 * "-", "MENU", 30 * "-")
print("1.Listas Ligadas\n2.Listas Duplamente Ligadas")

op = int(input("Escolha a estrutura: "))
if op == 1:
    lista = ListaLigada()
    lista.inserir(1)
    lista.inserir(3)
    lista.inserir(5)
    lista.inserir_posicao(10, 2)

    lista.remover_elemento(2)
    # lista.remover_posicao(0)

    print(lista)
    lista.remover_posicao(0)

    # print(lista.recuperar_no(2))  # recupera o No da posicao 2
    # print(lista.recuperar_elemento_no(2))  # printa o elemento da posicao 2
    # print(lista.cotem(5))  # verifica se existe o elemento 5 na lista
    # print(lista.indice(5)) # retorna a posicao do elemento 5
elif op == 2:
    lista = ListaDuplamenteLigada()
    lista.inserir(1)
    lista.inserir(3)
    lista.inserir(5)
    lista.inserir_posicao(10, 2)
    print(lista)
    # lista.remover_elemento(4)
    lista.remover_posicao(3)
    print(lista)

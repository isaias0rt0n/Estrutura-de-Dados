from array import array
from Vetores import vetores
"""vetor_inteiros = array('b', [1, 2, 3, 4])
print(vetor_inteiros)
vetor_inteiros.insert(4, 5)
print(vetor_inteiros)
print(vetor_inteiros.index(5))  # retorna a posição do elemento 5"""


print(30 * "-", "MENU", 30 * "-")
print("1. Vetores\n2. Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetores.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)
    vetor_teste.inserir_elemento_posicao(5, 2)
    vetor_teste.inserir_elemento_final(1)
    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)

    '''vetor_teste.inserir_elemento_final(1)
    print(vetor_teste.listar_elemento(0))
    print("Taman0 do vetor: {}".format(vetor_teste.tamanho_vetor()))
    print(vetor_teste.contem(2))
    print(vetor_teste.indice(2))'''

    print(vetor_teste.indice(4))
    vetor_teste.remover_elem_posicao(3)
    print(vetor_teste)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)
    print(vetor_teste.tamanho_vetor())
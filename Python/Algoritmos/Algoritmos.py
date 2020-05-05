# ----------Inicializa vetor----------#
numeros = list()
tam = int(input("Digite o tamanh do vetor: "))
for i in range(tam):
    valor = int(input(f"Digite o valor do vetro na posição {i}: "))
    numeros.append(valor)

# -----------Selection Sort----------- #
for i in range(tam):
    indice_menor = i  # atribui primeiro indice do vetor a variavel
    for j in range(int(i + 1), tam):  # percorre a partir do segundo indice ate o fim do vetor
        if numeros[j] < numeros[indice_menor]:  # se o valor do indice atual é menor q o valor do incio do vetor
            indice_menor = j  # se o valor atual do indice for menor, ele passa a ser o novo indice_menor
    # trocar valores de lugar. Por o menos valor pro incio do vetor
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("Vetor: {}".format(numeros))

# ------------Busca linear------------- #
numero_pesquisa = int(input("Digite o valor a ser pesquisado no vetor: "))
posicao_resultado = -1
for i in range(tam):
    if numeros[i] == numero_pesquisa:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print("O elemento nao foi encontrado no vetor")
else:
    print("Elemento encontrado na posição {}".format(posicao_resultado))

# -----------Busca Binaria------------- #
resultado = -1
ini = 0
fim = tam
meio = 0
alvo = int(input("Digite o elemento a ser encontrado por busca binaria: "))
while ini <= fim:
    meio = int((ini + fim) / 2)
    if numeros[meio] < alvo:
        ini = meio + 1
    elif numeros[meio] > alvo:
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print("Elemento n encontrado por BB")
else:
    print(f"Elemento {alvo} esta na posicao {resultado}")
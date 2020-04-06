/*Implementar as operações listadas abaixo para uma estrutura de dados com alocação sequencial.
a)Buscar elemento-OK;b)Busca Binária-OK;c)Inserir elemento-OK;d)Alterar elemento-OK;e)Excluir elemento-OK;

By: Isaias do Carmo*/

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

typedef struct lista Lista;
struct lista{
    int info;
    Lista *prox;
};
//Funcao cria lista vazia
Lista* lista_cria(){
    return NULL;
}
//Funcao testa se a lista esta vazia
int lista_vazia(Lista *l){
    return (l==NULL);
}
//Funcao que insere de forma ordenada um elemento na lista sequencial
Lista* lista_insere(Lista *l, int info){
    Lista *ln = (Lista*)malloc(sizeof(Lista));
    ln->info = info;
    if(l == NULL){          //Lista esta vazia, adciona o elemento a lista vazia
        ln->prox = NULL;
        return ln;
    } else if (l->info >= info){    //elemento é menor q todos os valores da lista. insere no inicio
        ln->prox = l;
        return ln;
    } else{
        Lista *lant = l;
        Lista *lprox = l->prox;
        while (lprox!=NULL&&lprox->info<info){ //percorre a lista ate encontrar o fim dela ou o valor maior q o elemento
            lant = lprox;
            lprox = lprox->prox;
        }
        //Adciona o elemento ao lista na ordem. Caso elemento passado seja maior q todos os elementos da fila, ele é adcionado no fim
        lant->prox = ln;
        ln->prox = lprox;
        return l;
    }
}
//Funcao busca elemento
int lista_busca(Lista *l, int info){
    Lista* aux = l;
    while (aux != NULL){
        if(aux->info == info)
            return aux->info;
        aux = aux->prox;
    }
    return -1;
}
//Funcao que exclui elemento
Lista* lista_remove(Lista *l, int info){
    if(!lista_vazia(l)){
        Lista* aux = l->prox; //aux aponta para o segundo elemento da lista
        if(l->info==info){  //Caso o elemento buscado sejo o primeiro da fila
            free(l);
            return aux;
        } else{
            Lista* lAnt = l; //lAnt apont pro primeiro no da lista
            //Agora, procurar pelo valor e ao encontrar tem que tira-lo da lista mas mantendo a sequencia
            //Assim, o elemento anterior ao valor encontrado passa a apontar para o No depois do valor
            //Em seguida, remove o elemeneto encontrado
            while (aux!=NULL){
                if(aux->info == info){
                    lAnt->prox = aux->prox;
                    free(aux);
                    break;
                } else{ //Nao encontrou. Entao avança na lista
                    lAnt = aux;
                    aux = aux->prox;
                }
            }
        }
    }
    return l;
}
//imprime lista
void lista_imprime(Lista *l){
    Lista* aux = l;
    while (aux!=NULL){
        printf("%d ",aux->info);
        aux = aux->prox;
    }
}
//Funcao busca binaria
int busca_binaria(int tam, int vet[], int elem){
    int ini=0, fim=tam-1, meio;
    while (fim-ini >= 0){
        meio = (ini + fim)/2;
        if(vet[meio] == elem)
            return meio;
        else if(elem > vet[meio])
            ini = meio + 1;
        else if(elem < vet[meio])
            fim = meio - 1;
    }
    return -1;    //Nao encontrou
}
//Funcao Altera um elemento da lista
Lista* lista_autera_elemento(Lista *l, int info, int newInfo){
    Lista *ln = (Lista*)malloc(sizeof(Lista));
    ln->info = newInfo;
    if(lista_vazia(l)){
        printf("Lista vazia!"); exit(1);
    }
    Lista *lAnt = l;
    Lista *lProx = l->prox;
    while (lProx!=NULL && lProx->info!=info){ //Percorre a lista
        lAnt = lProx;
        lProx = lProx->prox;
    }
    //inserir o elemento na lista no lugar do antigo elemento
    lAnt->prox = ln;
    ln->prox = lProx->prox;
    free(lProx); //tira o elemento antigo da lista
    return l;

}

int main (void){
    setlocale(LC_ALL,"");
    Lista* l = lista_cria(); //Cria uma lista vazia

//-----------------------------------------------------------------------------------------------------------------------------------
    //para usar poder usar a funcao busca binaria é necessario um vetor
    int tam;
    printf("Numero de elementos a inserir:");
    scanf("%d",&tam);
    int vet[tam];
    for (int i = 0; i < tam; ++i) {
        printf("Elemento%d:",(i+1));
        //Preenche um vetor. Sera usado para fazer busca binaria
        scanf("%d",&vet[i]);
        //Adciona os elementos na lista
        l = lista_insere(l,vet[i]);
    }
    lista_imprime(l);
    
    //Busca binaria é feita no vetor. A lista é mostrada de forma ordenada
    printf("\n%d\n",busca_binaria(tam,vet,5)); //Busca pelo elemento 5, caso encontre retorna o indice dele no vetor
    printf("%d\n",lista_busca(l,5));  //Busca pelo elemento 5, caso encontre retorna o valor buscado e -1 caso nao encontre
    l = lista_remove(l,3);
    l = lista_autera_elemento(l,2,4);

//-----------------------------------------------------------------------------------------------------------------------------------
    //por passagem de parametro para melhor entendimento
    /*l = lista_insere(l,10);
    l = lista_insere(l,20);
    l = lista_insere(l,30);
    l = lista_insere(l,40);
    l = lista_insere(l,50);
    l = lista_remove(l,20);*/
    //troca lemento da lista(lista_criada; valor a ser alterado; novo_valor) passar valor q exista na lista
    //l = lista_autera_elemento(l,35,25);
//-----------------------------------------------------------------------------------------------------------------------------------

    lista_imprime(l);

    return 0;
}
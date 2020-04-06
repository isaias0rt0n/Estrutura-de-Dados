#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/* By:Isaias do Carmo
 * N pilha a inserção, remoção e acesso de elemento é feita sempre no topo da pilha
 * primeiro que sai é o ultimo que entrou*/

//typedef struct pilha Pilha;
//Operações com pilha usando vetor
#define MAX 5
typedef struct pilha {
    int n;  //numero de elementos armazenados
    int v[MAX]; //tamanho do vetor
}Pilha;

//Funcao que cria uma pilha
Pilha* cria_pilha(void){
    Pilha *p = (Pilha*)malloc(sizeof(Pilha));
    if(p==NULL){
        printf("Passou da memória");
        exit(1);
    }
    p->n = 0;  // numero de elementos igual a zero
    return p;
}
//Funcao que verifica se a pilha esta vazia
int vazia_pilha(Pilha *p){
    return p->n==0; //Se o numero de elementos for 0, seginifica que a pilha esta vazia
}
//Funcao que insere elemento - sempre no topo, caracteristica de uma pilha
Pilha* insere_pilha(Pilha *p, int info){
    if(p->n==MAX){ //Verifica se a pilha ja esta cheia
        printf("Limite da pilha alcançcado!");
        exit(1);
    }
    p->v[p->n] = info; //insere o elemento no ultimo indice disponivel do vetor, ou seja, no topo da pilha
    p->n = p->n + 1; //Incrementa o numero de elementos na pilha
}
//Funcao que imprime uma pilha
void imprime_pilha(Pilha *p){
    for(int i=p->n-1; i>=0; i--){ //Imprime a pilha de cima para baixo
        printf("%d\n",p->v[i]);
    }
}
//Funcao que remove elemento da pilha - remoção sempre no topo
Pilha* remove_pilha(Pilha *p){
    int a;
    if(!vazia_pilha(p)){
        a = p->v[p->n-1]; //'a' recebe o penultimo elemento da pilha
        p->n--;     //decrementa o numro de elementos da pilha
        return p;   //Retorna o ultimto elemento
    }
}
//Funcao busca elemento na pilha
int busca_pilha(Pilha *p, int info){
    for(int i=p->n-1; i>=0; i--){ //Percorre o vetor pilha
        if(p->v[i] == info) //verifica se o valor contido no indice é o valor desejado
            return p->v[i]; // retorna o indice caso seja encontrado o valor
    }
    return -1; //retorna -1 caso nao encontre
}
//Funcao que altera elemento da pilha
Pilha* altera_pilha(Pilha *p, int info, int newInfo){
    for(int i=p->n-1;i>=0;i--){
        if(p->v[i] == info){
            p->v[i] = newInfo;
            return p;
        }
    }
    return NULL;
}
//funco busca binaria
int busca_binaria(int tam, int vet[],int elem){
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

//Funcao libera pilha
void libera_pilha(Pilha *p){
    free(p);
}

int main() {
    setlocale(LC_ALL,"");

    //Exemplo de uso
    Pilha *p = cria_pilha();
    p = insere_pilha(p,1);
    p = insere_pilha(p,2);
    p = insere_pilha(p,3);
    p = insere_pilha(p,10);
    p = insere_pilha(p,20);
    p = remove_pilha(p); //Remove do topo. no caso o elemento 10
    imprime_pilha(p);

    //faz uma busca usando metodo de busca binaria no vetor
    printf("busca binaria: %d\n",busca_binaria(MAX, p->v,3)); //busca o elemento 3 e retorna o indice dele
    //busca elemento-(pilha; valor a ser buscado)
    printf("buscando elemento: %d\n",busca_pilha(p,3)); //busca o elemento 3 e retorna ele caso encontre e -1 caso nao

    //altera um elemento da pilha(pilha; valor a ser alterado; novo valor)
    p = altera_pilha(p,3,5);
    imprime_pilha(p);

    libera_pilha(p);
    return 0;
}

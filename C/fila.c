#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*Estrutura de dados Fila: O primeiro que entra é o primeiro que sai(First in, first out)*/

typedef struct lista Lista;
typedef struct fila Fila;

struct lista{
    int info;
    Lista *prox;
};
struct fila{
    Lista *ini;
    Lista *fim;
};

//Funcao cria uma fila
Fila* cria_fila(void){
    Fila *f = (Fila*)malloc(sizeof(Fila));
    if(f==NULL){
        printf("Erro na criação");
        exit(1);
    }
    f->ini = NULL;
    f->fim = NULL;
    return f;
}
//Funcao testa se a fila esta vazia
int vazia_fila(Fila *f){
    return f->ini == NULL;
}
//Funcao que insere elemento na fila. Sempre no fim
void insere_fila(Fila *f, int info){
    Lista *l = (Lista*)malloc(sizeof(Lista));//Cria o No
    if(l==NULL){printf("Erro na criaçao");exit(1);}
    l->info = info; //campo informacao recebe o valor passado
    l->prox = NULL; //novos valores sempre apontam para null, pois na fila sempre é inserido no fim
    if(!vazia_fila(f)){
        f->fim->prox = l; //se a fila n estiver vazia, o campo prox do ultimo elemento da fila passa a pontar para o novo no
    } else {f->ini = l;}    //se estiver vazia significa que o no adcionado é unico da fila.
    f->fim = l; //o fim da fila passa a pontar para o novo No
}
//Funcao que remove o elemento da fila. Sempre remove o primeiro elemento
int remove_fila(Fila *f){
    Lista *l;
    if(vazia_fila(f)){
        printf("Fila ja esta vazia!\n");
        exit(1);
    }
    int a;
    a = f->ini->info;   //'a' recebe o valor contido no incio da fila
    l = f->ini; //novo no aponta pro inicio da fila
    f->ini = f->ini->prox;  //o ponteiro inicio passa a pontar para o proximo valor da fila
    free(l);    //remove o primeiro No da fila
    if(vazia_fila(f)){f->fim = NULL;}   //caso a fila esteja vazia o ponteiro fim aponta para NULL;
    return a;
}
//Funcao para imprimir fila
void imprime_fila(Fila *f){
    Lista *aux = f->ini; //Cria um No auxiliar que aponta pro inicio da fila
    while (aux!=NULL){  //percorre toda a fila
        printf("%d ",aux->info);    //printa os valores de cada No
        aux = aux->prox;    //avança na fila
    }
    printf("\n");
}
//Funcao libera espaço usado por uma fila
void libera_fila(Fila *f){
    Lista *aux; Lista *l = f->ini; //no l aponta pro incio da fila
    while (l!=NULL){
        aux = l->prox;  //  No auxiliar aponta pro segundo no da fila
        free(l);    // limpa o primeiro No da fila
        l = aux;    // l aponta pro incio da fila de novo
    }
    free(f); //limpa o espaço alocado por f
}
//Funcao que busca elemento da fila
int busca_elemento(Fila *f, int info){
    if(!vazia_fila(f)){ //verifica se a fila nao esta vazia
        Lista *aux = f->ini; //Cria um no auxiliar para percorrer a fila. ele aponta para o inicio da fila
        while (aux!=NULL){
            if(aux->info == info) //retorna o elemento caso seja encontrado
                return aux->info;
            aux = aux->prox; //avança na fila
        }
        return -1; //retorna -1 caso nao encontre o elemento
    }
}
//Funcao que altera elemento na fila
void altera_elemento(Fila *f, int info, int newInfo){
    Lista *aux = f->ini;    //cria um no aux que aponta para o inicio da fila
    while (aux!=NULL){ //percorre toda a fila
        if(aux->info == info){
            aux->info = newInfo; //Se o elemento for encontrado substitui pelo novo elemento
        }
        aux = aux->prox; //avança na fila
    }
}


int main() {
    setlocale(LC_ALL,"");

    //exemplo de uso
    Fila *f = cria_fila(); //cria uma fila
    insere_fila(f,1); //insere elementos no inicio da fila
    insere_fila(f,3);
    insere_fila(f,5);
    insere_fila(f,7);
    insere_fila(f,9);
    insere_fila(f,11);

    //Busca um elemento na fila - (fila; elemento que deseja buscar) retorna o elemento ou -1 caso nao exista
    printf("Buscando elemento: %d\n", busca_elemento(f,3));

    //Altera um elemento na fila - (fila; elemento a ser alterado; novo elemento)
    altera_elemento(f,11,4);

    remove_fila(f); //remove o primerio elemento da fila
    remove_fila(f);

    imprime_fila(f);
    libera_fila(f); //libera o espaço alocado por uma fila

    return 0;
}

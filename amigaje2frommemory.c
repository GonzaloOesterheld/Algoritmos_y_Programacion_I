#include <stdio.h>

void encontar_extremos(int array[], int n, int *max, int *min){
    *min = array[0];
    *max = array[0];

    
    for(int i = 1; i < n; i++){
        if (array[i] < *min){
            *min = array[i];
        }
        if (array[i] > *max){
            *max = array[i];
        }
    }

}

int main(){
    int minimo;
    int maximo;
    int array[] = {8,5,0,3,1,55};

    encontar_extremos(array, sizeof(array)/sizeof(array[0]), &maximo, &minimo);

    printf("Minimo: %d\n",minimo);
    printf("Maximo: %d",maximo);


    return 0;
}
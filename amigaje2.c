#include <stdio.h>

void hallar_max_min(int array[], int n, int* max, int* min){
    
    *min = array[0];
    *max = array[0];
    
    for (int i = 1; i < n; i++){
        if (array[i] < *min) {
            *min = array[i];
        }
        if (array[i] > *max){
            *max = array[i];
        }
    }
}

int main(){
    
    int array[] = {1, 2, 3, 4, 5};
    int minimo;
    int maximo;

    hallar_max_min(array, sizeof(array) / sizeof(array[0]), &maximo, &minimo);

    printf("Minimo: %d\n", minimo);
    printf("Maximo: %d\n", maximo);

    return 0;
}


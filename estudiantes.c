#include <stdio.h>

void funcion1(int array[], int j){
    int i = 0;
    int fin = j -1;
    int temp;

    while (i < fin){
        temp = array[i];
        array[i] = array[fin];
        array[fin] = temp;

        i++;
        fin--;
    }

}

int main(){

    int array[] = {1,2,3,4,5};
    int j = sizeof(array)/sizeof(array[0]);

    funcion1(array, j);

    for(int i = 0; i < j; i++){
        printf("%d ", array[i]);
    }

    return 0;
}
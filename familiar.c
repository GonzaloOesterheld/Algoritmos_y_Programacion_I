#include <stdio.h>

int funcion(int array[], int tam){
    //Encuentra el numero mas alto
    int mayor = 0;
    for (int i = 0; i < tam; i++){
        if (array[i] > mayor){
            mayor = array[i];
        }
    }
    //Convierte el numero mas alto a 0
    for (int i = 0; i < tam; i++){
        if(array[i] == mayor){
            array[i] = 0;
        }
    }
    //Vuelve a buscar el numero mas alto
    int segundo = 0;
    for (int i = 0; i < tam; i++){
        if (array[i] > segundo){
            segundo = array[i];
        }
    }
    return segundo;

}

int main(){

    int i = 0;
    int array[10];

    while (i < 10)
    {
        printf("Ingrese un numero: ");
        scanf("%d", &array[i]);
        i++;
    }
    printf("TUS NUMEROS:\n");
    for (int j = 0; j<10; j++){
        printf("%d ", array[j]);
    }

    int tam = sizeof(array)/sizeof(array[0]);
    int segundo_mayor = funcion(array, tam);

    printf("\nEl segundo numero mas grande es: %d", segundo_mayor);

    return 0;
}
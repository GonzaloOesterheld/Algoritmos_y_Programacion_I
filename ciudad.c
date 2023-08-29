#include <stdio.h>

void bool_ksum(int vector[], int n, int k){
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            if (vector[i] + vector[j] == k){
                if (vector[i] != vector[j]){
                printf("%d + %d = %d\n", vector[i], vector[j], k);
                }
            }
        }
    }
}

int main(){

    int vector[] = {1,2,3,4,5,7,8,9};
    int n = sizeof(vector) / sizeof(vector[0]);
    int k;

    printf("Ingrese un numero: ");
    scanf("%d", &k);


    bool_ksum(vector, n, k);


    return 0;
}
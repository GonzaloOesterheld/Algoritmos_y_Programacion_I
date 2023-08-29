#include <stdio.h>
#include <string.h>

void funcion1(char user[100],int j){
    char respuesta = '_';
    for(int i = 0; i < j; i++){
        for(int k = i + 1; k < j; k++){
            if(user[i] == user[k]){
                respuesta = user[i];
            }
        }
    }
    printf("Respuesta: %c", respuesta);
}


int main(){

    char user[100];

    printf("Ingrese un string: ");
    scanf("%s", user);

    int j = (int)strlen(user);

    funcion1(user, j);

    return 0;
}
#include <stdio.h>
#include <string.h>

//ESTAS FUNCIONES DEBEN SER INT SI DEVUELVEN UN ENTERO
void funcion1(){

}
//SI SON VOID PROBLABLEMENTE TOMEN UN ENTERO COMO VALOR PARA TRABAJAR CON EL
void funcion2(algo){

}

int main(){

    int user;
    int condicion;

    int algo;

    do{
        printf("\n1- Opcion 1\n2- Opcion 2\n");
        printf("\nIngrese opcion: ");
        scanf("%d",&user);
        switch (user)
        {
        case 1:
            funcion1();
            break;
        case 2:
            funcion2(algo);
            break;
        default:
            printf("\nOpcion no valida\n");
            break;
        }
        printf("\n1- Opcion 1\n2- Opcion 2\n");
        printf("\nIngrese un numero al azar (cierre = -1): ");
        scanf("%d", &condicion);
    }while(condicion != -1);

    return 0;
}
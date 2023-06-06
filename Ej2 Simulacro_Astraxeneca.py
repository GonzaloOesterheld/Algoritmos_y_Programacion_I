lista = [2, 8, 4, 1]

def suma_loca(lista):
    lista_alt = sum(lista)

    for i in range(len(lista)):

        lista[i] = lista_alt - lista[i]
    print(lista)

def main():
    lista = []
    user = int(input("Ingrese un numero para agregar a la lista (break with 111): "))
    lista.append(user)
    while user != 111:
        user = int(input("Ingrese un numero para agregar a la lista (break with 111): "))
        if user != 111:
            lista.append(user)
        
    suma_loca(lista)
    
main()
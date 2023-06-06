def funcion(lista, k):
    indices = []
    nueva_lista = lista
    
    for num in lista:
        nueva_lista.remove(num)
        for numero in nueva_lista:
            if num + numero == k:
                indices.append(num)
                indices.append(numero)
                print(indices)
        nueva_lista.append(num)
    
    tupla = (indices[0],indices[1])
    
    return tupla

def main():
    lista = []
    user = int(input("Ingrese un numero: "))
    while user != 111:
        lista.append(user)
        user = int(input("Ingrese otro numero (break with 111): "))
    k = int(input("Ingrese el numero K: "))
    tupla = funcion(lista, k)
    print(tupla)
    
main()
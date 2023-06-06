def fun_cadena(string,num):
    moved_string = ""
    for i in range(len(string)):
        moved_string += string[(i - num) % len(string)]
    return moved_string
    
def main():
    cadena = input("Ingrese un texto: ")
    numero = int(input("Ingrese un numero: "))
    
    print(fun_cadena(cadena,numero))
    
main()
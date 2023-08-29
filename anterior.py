def obtener_data():
    
    lis = []
    
    f = open(file="platos.txt", encoding="utf8", mode="r",newline="\n")
    
    for linea in f:
        linea = linea.strip("\r\n")
        lista = linea.split(",")
        lis.append(lista)
    return lis

def obtener_stock():
    
    stock = []
    
    f = open(file="stock.txt", encoding="utf8", mode="r",newline="\n")
    
    for linea in f:
        linea = linea.strip("\r\n")
        lista = linea.split(",")
        stock.append(lista)

    return stock
    
def mod_sotck(stock):
    ing = []
    for item in stock:
        print(f"{item[0]} - {item[1]}")
        ing.append(item[0])
    
    user = input("Ingrese que stock desea modificar: ")
    while user not in ing:
        user = input("Ingrese un stock existente: ")
    
    cant = input("Ingrese la nueva cantidad: ")
    

    
    with open(file="stock.txt", encoding="utf8", mode="w",newline="\n") as f:
        for item in stock:
            if item[0] == user:
                item[1] = cant
            f.write(f"{item[0]},{item[1]}\n")
    
def nuevo_plato(data):
    pass

def listar_negativos(data):
    pass

def menu():
    print("""
          1- Modificar Stock
          2- Agregar nuevo plato
          3- Listado de stocks negativos
          4- Salir
          """)
    
def main():
    
    data = obtener_data()
    stock = obtener_stock()
    menu()
    user = int(input("Ingrese una opcion: "))
    while user != 4:
        if user == 1:
            mod_sotck(stock)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            nuevo_plato(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            listar_negativos(stock)
            menu()
            user = int(input("Ingrese una opcion: "))

main()
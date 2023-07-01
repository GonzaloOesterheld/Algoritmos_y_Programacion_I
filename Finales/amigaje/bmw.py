import csv

def obtener_datos():
    
    detalles = []
    productos = []
    ventas = []
    
    with open('detalles.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for linea in reader:
            if linea[0] == "Nº Operación":
                pass
            else:
                detalles.append(linea)
                
    with open('productos.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for linea in reader:
            if linea[0] == "ID Producto":
                pass
            else:
                productos.append(linea)

    with open('ventas.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for linea in reader:
            if linea[0] == "Nº Operación":
                pass
            else:
                ventas.append(linea)
    
    return (detalles,productos,ventas)
                
     
def mas_vendido(data):
    pass

def cant_x_año(data):
    pass

def importe(data):
    pass

def porcentajes(data):
    pass

def menu():
    print("""
          ~~~~~
          BMW
          ~~~~~
          1- Linea que mas vendio segun $
          2- Cantidad de articulos vendidos por año
          3- Importe $ promedio por operacion y operaciones por encima
          4- % total segun año y producto
          5- Salir
          """)
    
def main():
    
    data = obtener_datos()
    menu()
    user = int(input("Ingrese una opcion: "))
    
    while user != 5:
        if user == 1:
            mas_vendido(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            cant_x_año(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            importe(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 4:
            porcentajes(data)
            menu()
            user = int(input("Ingrese una opcion: "))

main()
import csv

def obtener_data():
    
    lis = []
    
    try:
        with open('Gaastos.csv',encoding='utf8') as file:
            reader = csv.reader(file, delimiter=",")
            for linea in reader:
                lis.append(linea)                
        return lis
    except FileNotFoundError:
        print("\nEl archivo no existe\n")
        with open('Gaastos.csv', mode='w', encoding='utf8') as file:
            writer = csv.writer(file, delimiter=",")
            for linea in writer:
                lis.append(linea)
        return lis
        

def ingresar_ingreso(ingresos):
    
    concepto = input("Ingrese el asunto del ingreso: ")
    categoria = input("Ingrese la categoria del gasto: ")
    cant = int(input("Ingrese el monto: "))
    dic = {
        "concepto": concepto,
        "categoria": categoria,
        "cantidad": cant
    }
    ingresos.append(dic)

def porcentaje_gastos(data):
    categorias = {}
    cont = 0
    for lista in data:
        if lista[1] not in categorias.keys():
            categorias[f"{lista[1]}"] = [lista[1], 1]
        else:
            categorias[f"{lista[1]}"][1] += 1
        cont += 1
    for key,value in categorias.items():
        value[1] = (value[1] / cont) * 100
    
    ordenado = sorted(categorias.items(), key = lambda x: x[1][1], reverse=True)
    
    for tupla in ordenado:
        print(f"Categoria: {tupla[0]} - Porcentaje: {tupla[1][1]}%")

def funcion3(data):
    pass

def funcion4(data):
    pass

def funcion5(data):
    pass

def funcion6(data):
    pass


def menu():
    print("""
          1- Cargar un ingreso
          2- Reporte de porcentaje de gastos
          3- 3
          4- 4
          5- 5
          6- 6
          7- 7
          """)
    
def main():
    
    data = obtener_data()
    
    ingresos = []
    menu()
    user = int(input("Ingrese una opcion: "))
    while user != 7:
        if user == 1:
            ingresar_ingreso(ingresos)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            porcentaje_gastos(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            funcion3(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 4:
            funcion4(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 5:
            funcion5(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 6:
            funcion6(data)
            menu()
            user = int(input("Ingrese una opcion: "))

main()
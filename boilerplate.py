import csv

def obtener_data():
    
    dic = {}
    
    with open('nombre.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        
    
    return dic

def funcion1(data):
    pass

def funcion2(data):
    pass

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
          1- 1
          2- 2
          3- 3
          4- 4
          5- 5
          6- 6
          7- 7
          """)
    
def main():
    
    data = obtener_data()
    
    user = int(input("Ingrese una opcion: "))
    while user != 7:
        if user == 1:
            funcion1(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            funcion2(data)
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
import csv

def obtener_data():
    
    lis = []
    
    with open('notas.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter="\n")
        for linea in reader:
            estudiante = linea[0].split(", ")
            tupla = tuple(estudiante)
            lis.append(tupla)    
    return lis

def promedio_materia(data):
    materias = []
    for item in data:
        if item[1] not in materias:
            materias.append(item[1])
    user = input("Ingrese una materia: ")
    while user not in materias:
        print("Nadie curso esa materia")
        user = input("Ingrese otra materia: ")
        
    dic = {
        "Promedio": 0,
        "Aprobados": [],
        "Reprobados": []        
    }    
    total = 0
    nota = 0
    for estudiante in data:
        if estudiante[1] == user:
            if int(estudiante[2]) >= 4:
                dic["Aprobados"].append(estudiante[0])
            else:
                dic["Reprobados"].append(estudiante[0])
            total += 1
            nota += int(estudiante[2])
    dic["Promedio"] += (nota/total)
    print(f"""Promedio: {dic['Promedio']}\nAprobados: {dic['Aprobados']}\nReprobados: {dic["Reprobados"]}""")
    return dic

def dic_cuatrimestre(data):
    nota_primer = 0
    nota_segun = 0
    contador1 = 0
    contador2 = 0
    for linea in data:
        print(linea[3][4:])
        if linea[3][3:] == "01":
            nota_primer += int(linea[2])
            contador1 += 1
        else:
            nota_segun += int(linea[2])
            contador2 += 1
    
    dic = {
        "Primer Cuatrimestre": nota_primer/contador1,
        "Segundo Cuatrimestre": nota_segun/contador2
    }            
    print("NOTAS PROMEDIO: ")
    print(f'Primer cuatrimestre: {dic["Primer Cuatrimestre"]}')
    print(f'Segundo cuatrimestre: {dic["Segundo Cuatrimestre"]}')
    return dic

def lista_de_listas(data):
    pass
    
def arc_materia(data):
    materias = []
    for item in data:
        if item[1] not in materias:
            materias.append(item[1])
    user = input("Ingrese una materia: ")
    while user not in materias:
        print("Nadie curso esa materia")
        user = input("Ingrese otra materia: ")

    f = open(f"{user}","w",encoding="UTF-8",newline='')
    
    estudiantes = []
    top5 = []
    for linea in data:
        if linea[1] == user:
            estudiantes.append(linea)
    ordenados = sorted(estudiantes, key=lambda x: x[2])
    for i in range(5):
        top5.append(ordenados[i])
    top5ordenado = sorted(top5, key=lambda x: x[3])
    print(top5ordenado)
    
    for est in range(len(top5ordenado)):
        top5ordenado[est] = ", ".join(top5ordenado[est]) + "\n"
    
    f.writelines(top5ordenado)
    f.close()

def menu():
    print("""
          1- Ingrese una materia para obtener un diccionario con sus datos
          2- Obtener un diccionario con el promedio de notas de cada cuatrimestre
          3- 3
          4- 4
          5- Salir
          """)
    
def main():
    
    data = obtener_data()
    menu()
    user = int(input("Ingrese una opcion: "))
    while user != 5:
        if user == 1:
            promedio_materia(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            dic_cuatrimestre(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            lista_de_listas(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 4:
            arc_materia(data)
            menu()
            user = int(input("Ingrese una opcion: "))


main()
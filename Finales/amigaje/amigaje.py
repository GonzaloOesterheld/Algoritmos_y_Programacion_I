import csv

def proceso_info():
    
    personas = {}
    
    with open('integrantes.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for persona in reader:
            persona[6] = persona[6:]
            for i in range(len(persona)-1):
                if i > 6:
                    persona.remove(persona[i])
                    persona.pop()
            personas[f"{persona[0]}"] = persona
    
    return personas

def imprimir_info(personas):
    for key in personas:
        print(f"""Nombre: {personas[key][0]}
                  Incorporacion: {personas[key][1]}
                  TPs corregidos: {personas[key][2]}
                  Nota Promedio TP: {personas[key][3]}
                  Parciales corregidos: {personas[key][4]}
                  Nota promedio parciales: {personas[key][5]}
                  Temas preferidos: {personas[key][6]}                        
                                            """)

def estimar_antiguedad(personas):
    fechas = []
    for persona in personas.values():
        fechas.append(persona[1])
    años = []
    for fecha in fechas:
        años.append(int(fecha[0:4]))
    
    antiguedad = 2023 - (sum(años)/len(años))
    
    print(f"Antiguedad promedio del equipo: {antiguedad} años")

def promedio_recursividad(personas):
    recursos = {}
    for persona in personas.values():
        if "Recursividad" in persona[6]:
            recursos[f"{persona[0]}"] = persona
    
    cant_parciales = []
    not_prom = []
    for persona in recursos.values():
        cant_parciales.append(int(persona[4]))
        not_prom.append(int(persona[5]))
    
    mult = 0
    for i in range(len(not_prom)):
        mult += cant_parciales[i] * not_prom[i]

    total = mult / sum(cant_parciales)
    
    print(f"El promedio es: {total}")

def temas_fav(personas):
    temas = {}
    
    for persona in personas.values():
        for tema in persona[6]:
            if tema not in temas.keys():
                temas[f"{tema}"] = 1
            else:
                temas[f"{tema}"] += 1
    
    ordenados = sorted(temas.items(), key=lambda x: x[1], reverse=True)
    for tupla in ordenados:
        print(f"{tupla[0]} - aparece {tupla[1]} veces")

def compar_x_cuatri(personas):
    primer = {}
    segun = {}
    for persona in personas.values():
        if (int(persona[1][4:6])*10) <= 60:
            primer[f"{persona[0]}"] = persona
        else:
            segun[f"{persona[0]}"] = persona
    
    tuplita = (primer,segun)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in tuplita:   
        print(f"Cantidad de integrantes del cuatrimestre: {len(i)}")
        buen_prom = 0
        for per in i.values():
            if int(per[3]) and int(per[5]) > 6:
                buen_prom += 1
        print(f"Porcentaje de personas con promedio >6: {(buen_prom/len(i))*100}%")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
def menu():
    print("""
          1 - Informacion integrantes
          2 - Antiguedad promedio del equipo
          3 - Promedio parciales integrantes recursividad
          4 - Ranking temas favoritos del equipo
          5 - Comparar integrantes por cuatri
          6 - Salir
          """)

def main():
    data = proceso_info()
    menu()
    try:
        user = int(input("Ingrese una opcion: "))
        while user != 6:
            if user == 1:
                imprimir_info(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 2:
                estimar_antiguedad(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 3:
                promedio_recursividad(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 4:
                temas_fav(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 5:
                compar_x_cuatri(data)
                menu()
                user = int(input("Ingrese una opcion: "))
    except ValueError:
        print("INGRESE UN VALOR VALIDO")
        user = int(input("Ingrese una opcion: "))
        while user != 6:
            if user == 1:
                imprimir_info(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 2:
                estimar_antiguedad(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 3:
                promedio_recursividad(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 4:
                temas_fav(data)
                menu()
                user = int(input("Ingrese una opcion: "))
            elif user == 5:
                compar_x_cuatri(data)
                menu()
                user = int(input("Ingrese una opcion: "))
    
main()
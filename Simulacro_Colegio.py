

def ingreso_alumno(alumnos):
        dni = int(input("Ingrese el DNI del alumno: "))
        nobre_alumno = input("Ingrese el nombre y apellido del alumno: ")
        sala = input("Ingrese la sala del alumno: ")
        figus = []
        figu = int(input("Ingrese una figurita del alumno: "))
        while figu != 181:
            figu = int(input("Ingrese una figurita del alumno (break=181): "))
            figus.append(figu)
        
        alumnos.append(
            {
                "DNI": dni,
                "Nombre y Apellido": nobre_alumno,
                "Sala": sala,
                "Figus": figus
            }
        )
        
def top_5(alumnos):
    alu = []
    if len(alumnos) >= 5:
        for i in range(5):
            top = [0]
            for alumno in alumnos:
                sin_repes = list(set(alumno["Figus"]))
                if len(sin_repes) > min(top) and alumno not in alu:
                    top.remove(0)
                    top.append(len(sin_repes))
                    alu.append(alumno)
    else:
        print("No hay 5 alumnos")
    
    for alumno in alu:
        print(alumno["Nombre y Apellido"])
                

            
def repes_x_alumno(alumnos):
        a = 0
        b = 0
        c = 0
        sa = 0
        sb = 0
        sc = 0
        for alumno in alumnos:
            counter = 0
            seen = []
            for figu in alumno["Figus"]:
                #3print(alumno["Figus"].count(figu))
                if alumno["Figus"].count(figu) > 1 and figu not in seen:
                    counter += alumno["Figus"].count(figu)- 1
                    seen.append(figu)
            if alumno["Sala"] == "A":
                a += counter
                sa += 1
            elif alumno["Sala"] == "B":
                b += counter
                sb += 1
            elif alumno["Sala"] == "C":
                c += counter
                sc += 1
                
        print(f"El promedio de repes por alumno del curso A es: {a / sa}")
        print(f"El promedio de repes por alumno del curso B es: {b / sb}")
        print(f"El promedio de repes por alumno del curso C es: {c / sc}")

    

def repes_eficientes(alumnos):
        pass


def menu():
    print("""
          MENU
          1- Ingreso nuevo alumno
          2- Top 5 alumnos cercanos a completar el album
          3- Promedio de repetidas por alumno segun aula
          4- Pares de alumnos eficientes¿
          5-SALIR
          """)

def main():
    
    alumnos = [
        {
            "DNI": 45628740,
            "Nombre y Apellido": "Gonzalo Oesterheld",
            "Sala": "A",
            "Figus": [1,2,3,3,4,8,12,15,16,17,17,17] 
        },
        {
            "DNI": 44228720,
            "Nombre y Apellido": "Martin Libano",
            "Sala": "B",
            "Figus": [1,3,4,4,8,12,13,15,15,17,17] 
        },
        {
            "DNI": 42898990,
            "Nombre y Apellido": "Enzo Fontana",
            "Sala": "C",
            "Figus": [7,9,11,15,15,15,90] 
        },
        {
            "DNI": 41111140,
            "Nombre y Apellido": "Olivia Dillon",
            "Sala": "A",
            "Figus": [1,2,36,88,123,123] 
        }
    ]
    
    menu()
    
    user = int(input(" Ingrese una opcion: "))
    
    while user != 5:
        if user == 1:
            ingreso_alumno(alumnos)
            menu()
            user = int(input(" Ingrese una opcion: "))
        elif user == 2:
            top_5(alumnos)
            menu()
            user = int(input(" Ingrese una opcion: "))
        elif user == 3:
            repes_x_alumno(alumnos)
            menu()
            user = int(input(" Ingrese una opcion: "))
        elif user == 4:
            repes_eficientes(alumnos)
            menu()
            user = int(input(" Ingrese una opcion: "))

main()
def menu():
    print("""
          1- Ingreso nuevo alumno
          2- Top 10 alumnos
          3- Reporte resumen del TP2
          4- Reporte resumen del parcial
          5- Salir
          """)

def ingreso_alumno(estudiantes):
    padron = int(input("Ingrese padron: "))
    nom = input("Ingrese nombre y apellido: ")
    tp1 = int(input("Ingrese nota del TP1: "))
    tp2 = int(input("Ingrese nota del TP2: "))
    grupo = int(input("Ingrese grupo del estudiante: "))
    parcial = int(input("Ingrese nota del parcial: "))
    inten = int(input("Ingrese intentos del parcial: "))
    
    nuevo = {
        "padron": padron,
        "nom": nom,
        "tp1": tp1,
        "tp2": tp2,
        "grupo": grupo,
        "parcial": parcial,
        "intentos": inten
    }
    
    estudiantes.append(nuevo)    

def top_alumnos(estudiantes):
    top10 = [0]
    aprobados = []
    listado_final = []
    for estudiante in estudiantes:
        if estudiante["tp1"] >=4:
            if estudiante["tp2"] >= 4:
                if estudiante["parcial"] >= 4:
                    aprobados.append(estudiante)
     
    for i in range(10):               
        for estudiante in aprobados:
            prom = (estudiante["tp1"] + estudiante["tp2"] + estudiante["parcial"]) / 3
            if prom > min(top10) and estudiante not in listado_final:
                top10.append(prom)
                if 0 in top10:
                    top10.remove(0)
                listado_final.append(estudiante)
            
    for est in listado_final:
        print(est["nom"])      
            
    
def reporte_tp2(estudiantes):
    grupos = {
    }
    for estudiante in estudiantes:
        grupo = str(estudiante['grupo'])
        if str(estudiante['grupo']) not in grupos.keys():
            grupos[grupo] = [estudiante]
        else:
            grupos[grupo].append(estudiante)
    
    for key, grupo in grupos.items():
        notas = []
        aprobados = []
        
        for estudiante in grupo:
            notas.append(estudiante["tp1"])
            notas.append(estudiante["tp2"])
            notas.append(estudiante["parcial"])
            if (estudiante["tp1"] + estudiante["tp2"] + estudiante["parcial"])/ 3 >= 4:
                aprobados.append(estudiante)
        
        print(f""""Grupo: {key}
              Nota Promedio = {sum(notas)/len(notas)}
              Estudiantes aprobados:
                    {[estudiante["nom"] for estudiante in aprobados]}
                """)
    

def reporte_parcial(estudiantes):
    intentos = {}
    for est in estudiantes:
        if est["intentos"] not in intentos:
            intentos[f"{est['intentos']}"] = [est]
        else:
            intentos[f"{est['intentos']}"].append(est)
        
    for key, intento in intentos.items():
        notas = []
        desaprobados = []
        for estudiante in intento:
            
            notas.append((estudiante["tp1"] + estudiante["tp2"] + estudiante["parcial"])/3)
            
            if (estudiante["tp1"] + estudiante["tp2"] + estudiante["parcial"])/ 3 <= 4:
                desaprobados.append(estudiante)
        
        prom = sum(notas)/len(notas)
        
        print(f"""
              Intentos: {key}
              Nota Promedio: {prom}
              Alumnos desaprobados: {[estudiante["nom"] for estudiante in desaprobados]}
              """)

def main():
    estudiantes = [
        {
            "padron": 12345,
            "nom": "Bruno Lanzillota",
            "tp1": 8,
            "tp2": 10,
            "grupo": 1,
            "parcial": 9,
            "intentos": 1
        },
        {
            "padron": 98765,
            "nom": "Franco Callaneo",
            "tp1": 7,
            "tp2": 8,
            "grupo": 1,
            "parcial": 2,
            "intentos": 3
        },
        {
            "padron": 87513,
            "nom": "Lautaro Di Matteo",
            "tp1": 5,
            "tp2": 2,
            "grupo": 7,
            "parcial": 2,
            "intentos": 1
        }
    ]
    
    menu()
    
    user = int(input("Ingrese una opcion: "))
   
    while user != 5:
        if user == 1:
            ingreso_alumno(estudiantes)
        elif user == 2:
            top_alumnos(estudiantes)
        elif user == 3:
            reporte_tp2(estudiantes)
        elif user == 4:
            reporte_parcial(estudiantes)
        menu()
        user = int(input("Ingrese una opcion: "))
    
main()
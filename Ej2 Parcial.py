cadena: str = '20392194691, Leonel, Chaves, 0800, 1200||19392194602, Ramiro, Esperon, 0800, 1300||20392194691, Leonel, Chaves, 1200, 1700||18288658790, Guido, Costa, 0900, 1500'
listado = cadena.split("||")

def cantidad_salidas(listado):

    log = []
    for i in listado:
        elementos = i.split(", ")
        salidas = 0
        cuil = elementos[0]
        if cuil not in log:
            log.append(cuil)
        else:
            salidas += 1
        tupla = (cuil, salidas)
        print(tupla)

    
cantidad_salidas(listado)

def no_cumple_horario(listado):
    
    empleados = []
    repe = []
    visto = []
    print(empleados)
    for i in listado:
        elementos = i.split(", ")
        cuil = elementos[0]
        h_entrada = int(elementos[3])
        h_salida = int(elementos[4]) 
        if cuil not in visto:
            empleados.append(elementos)
        else:
            repe.append(elementos)
        
        visto.append(cuil)
        
        
        
    
    incumplidos = []
    
    
                
        
    for empleado in empleados:
        horario_entrada = int(empleado[3])
        horario_salida = int(empleado[4])
        
        entrada_horas = horario_entrada // 100
        entrada_minutos = horario_entrada % 100
        entrada_total = entrada_horas * 60 + entrada_minutos

        salida_horas = horario_salida // 100
        salida_minutos = horario_salida % 100
        salida_total = salida_horas * 60 + salida_minutos
        minutos_realizados = salida_total - entrada_total
        
        empleado.append(minutos_realizados)
        print(minutos_realizados)    
    for emp in repe:
        hor_entrada = int(emp[3])
        hor_salida = int(emp[4])
        
        ent_horas = hor_entrada // 100
        ent_minutos = hor_entrada % 100
        ent_total = ent_horas * 60 + ent_minutos

        sal_horas = hor_salida // 100
        sal_minutos = hor_salida % 100
        sal_total = sal_horas * 60 + sal_minutos
        min_realizados = sal_total - ent_total
        
        emp.append(min_realizados)
        
        for i in empleados:
            if i[0] == emp[0]:
                i[5] += emp[5]
                print(i[5])
    
    for empleado in empleados:
        if empleado[5] < 480:
            incumplidos.append(empleado)
        
    print("Los empleados que no cumplieron las horas laborales son")
    for empleado in incumplidos:
        print(f"CUIL: {empleado[0]}, Nombre: {empleado[1]}, Apellido: {empleado[2]}, Cantidad de horas realizadas: {empleado[5]//60}")
               
#no_cumple_horario(listado)


def datos_x_cuil(listado):
    user =input("Ingrese un CUIL:")
    coincidio = []
    for empleado in listado:
        elementos = empleado.split(", ")
        if user == elementos[0] and user not in coincidio:
            print(f"Nombre: {elementos[1]}, Apellido: {elementos[2]}")
            coincidio.append(user)
    if coincidio == []:
        print("No hay un empleado con ese CUIL")
    
#datos_x_cuil(listado)
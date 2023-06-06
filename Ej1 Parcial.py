def carga_asistencias(asistencias):
    fecha = input("Ingrese la fecha del servicio: ")
    numero_dominio = int(input("Ingrese el nuevo domminio: "))
    tipo_vehiculo = input("Ingrese el tipo de vehiculo (auto/moto/camioneta/camion): ")
    while tipo_vehiculo != "auto" and "moto" and "camioneta" and "camion":
        tipo_vehiculo = input("Ingrese el tipo de vehiculo (auto/moto/camioneta/camion): ")
    direccion_origen = input("Ingrese donde se requiere asistencia: ")
    direccion_destino= input("Ingrese destino del vehiculo: ")
    tipo_asistencia = input("Ingrese tipo de asistencia (mecanica/remolque): ")
    tiempo_estimado_servicio = int(input("Duracion del servicio en horas: "))
    prioridad = input("Ingrese la prioridad (alta/media/noraml): ")
    numero_movil= int(input("Ingrese el numero del movil: "))
    estado_servicio = input("Ingrese el estado del servicio(finaliado/en curso/cancelado): ")
    valor_servicio = int(input("Ingrese el valor del servicio: "))
    asistencia = {
        "fecha": fecha,
        "numero_dominio": numero_dominio,
        "tipo_vehiculo": tipo_vehiculo,
        "direccion_origen": direccion_origen,
        "direccion_destino": direccion_destino,
        "tipo_asistencia": tipo_asistencia,
        "tiempo_estimado_servicio": tiempo_estimado_servicio,
        "prioridad": prioridad,
        "numero_movil": numero_movil,
        "estado_servicio": estado_servicio,
        "valor_servicio": valor_servicio
    }
    asistencias.append(asistencia)
    
def finalizar_cancelar_pedido(asistencias):
    dom = int(input("Ingrese el dominio del pedido: "))
    canc_fin = input("Desea cancelar o finalizar el pedido: ").lower
    
    if canc_fin == "cancelar":
        for asistencia in asistencias:
            if asistencia["numero_dominio"] == dom:
                asistencia["estado_servicio"] == "cancelado"
    if canc_fin == "finalizar":
        for asistencia in asistencias:
            if asistencia["numero_dominio"] == dom:
                asistencia["estado_servicio"] == "finalizado"

def agregar_nuevo_movil(mobiles):
    num = int(input("Ingrese el numero del nuevo movil: "))
    tip = input("Ingrese el tipo de servicio del nuevo movil: ")
    ser = int(input("Ingrese los servicios prestados: "))
    mobiles.append({
        "numero_movil": num,
        "tipo_asistencia": tip,
        "servicios_prestados": ser
    })

def listado_servicios(asistencias):
    tot_serv = 0
    tot_fact = 0
    for asistencia in asistencias:
        if asistencia["estado_servicio"] == "finalizado" or "cancelado":
            tot_serv += 1
            tot_fact += asistencia["valor_servicio"]
    
    print(f"Los servicios totales son: {tot_serv} y la facturacion total es: {tot_fact}")

def obtener_promedio_tiempo(asistencias):
    t_total = 0
    for asistencia in asistencias:
        t_total += asistencia["tiempo_estimado_servicio"]
    print(f"el tiempo estimado es {t_total/len(asistencias)}")   




def porcentaje_tipo_veh(asistencias):
    v_auto = 0
    v_moto = 0
    v_camioneta = 0
    v_camion = 0
    for asistencia in asistencias:
        if asistencia["tipo_vehiculo"] == "auto":
            v_auto += 1
        if asistencia["tipo_vehiculo"] == "moto":
            v_moto += 1
        if asistencia["tipo_vehiculo"] == "camioneta":
            v_camioneta += 1
        if asistencia["tipo_vehiculo"] == "camion":
            v_camion += 1

    p_totales = v_auto + v_moto + v_camion + v_camioneta

    print(f"el porcentaje de pedidos en auto es {(v_auto/p_totales)*100}%")
    print(f"el porcentaje de pedidos en moto es {(v_moto/p_totales)*100}%")
    print(f"el porcentaje de pedidos en camioneta es {(v_camioneta/p_totales)*100}%")
    print(f"el porcentaje de pedidos en camion es {(v_camion/p_totales)*100}%")

def main():
    opciones = (
        "Carga de Asistencias",
        "Finalizar/Cancelar sercvicio",
        "Agregar nuevo movil",
        "Listado servicios prestados y total facturado",
        "Obtener promedio de tiempo estimado",
        "Obtener el movil con mas servicios prestados",
        "Porcentaje de tipo de asistencia",
        "Obtener el porcentaje de los tipos de vehiculos asistidos",
        "Salir"
    )
    
    asistencias = []
    mobiles = [
        {
            "numero_movil": 0,
            "tipo_asistencia": "mecanica",
            "servicios_prestados": 0
        }
    ]
    
    for i in range(len(opciones)):
        print(f"{i+1} - {opciones[i]}")
    opcion = int(input("Ingrese una opcion: "))
            
    while opcion != 9:
        if opcion == 1:
            carga_asistencias(asistencias)
        elif opcion == 2:
            finalizar_cancelar_pedido(asistencias)
        elif opcion == 3:
            agregar_nuevo_movil(mobiles)
        elif opcion == 4:
            listado_servicios(asistencias)
            pass
        elif opcion == 5: 
            obtener_promedio_tiempo(asistencias)
        elif opcion == 6:
            #obtener_movil_con_mas_servicios(mobiles)
            pass
        elif opcion == 7:
            #porcentaje_tipo_asist(asistencias)
            pass
        elif opcion == 8:
            porcentaje_tipo_veh(asistencias)
        opcion = int(input("Ingrese una opcion: "))

main()
def ingreso_cantidades(computadores):
    pass

def ingreso_demanda(computadores):
    pass

def distribucion_prioridad(computadores):
    pass

def reporte_demanda(computadores):
    pass



def main():
    
    computadores= [
        {
            "tipo": "basico",
            "precio": 800
        },
        {
            "tipo": "intensivo",
            "precio": 1000
        }
    ]
    user = int(input("Ingrese una opcion: "))
    print("""\n1- Ingreso de las cantidades brindadas por Dell\n
          2- Ingreso de la demanda\n
          3- Reporte de distribucion de equipamiento segun\n
          4- Reporte de demanda\n
          """)
    if user == 1:
        ingreso_cantidades(computadores)
        pass
    elif user == 2:
        ingreso_demanda(computadores)
        pass
    elif user == 3:
        distribucion_prioridad(computadores)
        pass
    elif user == 4:
        reporte_demanda(computadores)
    while user != 1 or 2 or 3 or 4:
        user = int(input("Ingrese una opcion: "))
def menu():
    print("""
    1- Carga de pedido
    2- Mostrar pedidos segun año y mes
    3- Mostrar pedidos ordenados por fecha
    4- Gasto total por categoria
    5- Gasto total anual por categoria
    6- Salir
    """)

def carga_pedido(pedidos):

    cat = ["AL","ME","FE"]
    
    idd = len(pedidos) + 1
    info = input("Ingrese descripcion del gasto: ")
    costo = int(input("Ingrese el costo: "))
    categoria = input("Ingrese la categoria (AL/ME/FE) : ")
    while categoria not in cat:
        categoria = input("Ingrese la categoria (AL/ME/FE) : ")
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    
    pedido = {
        "id": idd,
        "info": info,
        "costo": costo,
        "categoria": categoria,
        "mes": mes,
        "año": año,
            }
    
    pedidos.append(pedido)
          
def pedidos_por_mes(pedidos):

    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    
    filtrados = []
    
    for pedido in pedidos:
        if pedido["mes"] == mes and pedido["año"] == año:
            filtrados.append(pedido)
    
    print(f"AÑO: {año} - MES: {mes}")    
    tot = 0
    for pedido in filtrados:
        tot += pedido["costo"]
        print(f"Id: {pedido['id']} - Info: {pedido['info']}")
    print(f"Costo total del {mes}/{año}: {tot}")  
    
def pedido_por_fecha(pedidos):

    años = {}
    
    pedidos.sort(key = lambda pedido: pedido["año"])
    
    for pedido in pedidos:
        
        if str(pedido["año"]) not in años.keys():
            años[f"{pedido['año']}"] = [pedido]
        else:
            años[f"{pedido['año']}"].append(pedido)
            
    for key, mes in años.items():
        mes.sort(key = lambda pedido: pedido["mes"])
        print(f"AÑO: {key}")
        for dic in mes:
            print(f"MES {dic['mes']}, ID: {dic['id']}, INFO: {dic['info']}")


def gasto_categoria(pedidos):

    al = 0
    me = 0
    fe = 0
    
    for pedido in pedidos:
        if pedido["categoria"] == "AL":
            al += pedido["costo"]
        elif pedido["categoria"] == "ME":
            me += pedido["costo"]
        elif pedido["categoria"] == "FE":
            fe += pedido["costo"]
    
    print(f"""
          Costo total de Alimentos: {al}
          Costo total de Medicinas: {me}
          Costo total de Fertilizantes: {fe}
          """)
    
def gasto_anual_categoria(pedidos):

    años = {}
    
    pedidos.sort(key = lambda pedido: pedido["año"])
    
    for pedido in pedidos:
        
        if str(pedido["categoria"]) not in años.keys():
            años[f"{pedido['categoria']}"] = [pedido]
        else:
            años[f"{pedido['categoria']}"].append(pedido)
    
    for key, cat in años.items():
        print(f"Categoria: {key}")
        cost = 0
        for dic in cat:
            cost += dic["costo"]
        print(f"Gasto Total: {cost}")

def main():
    
    pedidos = [
        {
        "id": 1,
        "info": "Heno",
        "costo": 250000,
        "categoria": "AL",
        "mes": 2,
        "año": 2021,
            },
        {
        "id": 2,
        "info": "Medicina para picachu",
        "costo": 20000,
        "categoria": "ME",
        "mes": 1,
        "año": 2021,
        },
        
        ]
    
    menu()

    user = int(input("Ingrese una opcion: "))

    while user != 6:
        if user == 1:
            carga_pedido(pedidos)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            pedidos_por_mes(pedidos)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            pedido_por_fecha(pedidos)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 4:
            gasto_categoria(pedidos)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 5:
            gasto_anual_categoria(pedidos)
            menu()
            user = int(input("Ingrese una opcion: "))

main()
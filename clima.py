import csv

def obtener_data():
    
    lista = []
    
    with open('temperaturas.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for linea in reader:
            lista.append(linea)
    return lista

def registro_lectura():
    fecha = input("Ingrese la fecha (DDMMAAAA):")
    tem_min = float(input("Ingrese la temperatura minima: "))
    tem_max = float(input("Ingrese la temperatura maxima: "))
    est = input("Ingrese la estacion de la lectura: ")
    lista = [fecha,tem_min,tem_max,est]
    
    with open('temperaturas.csv',encoding='utf8',mode="a",newline="") as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(lista)     
        
def segun_fecha(data):
    print("Ingrese un rango de fechas (AAAAMMDD)")
    fecha1 = int(input("Fecha de inicio: "))
    fecha2 = int(input("Fecha de finalizacion: "))

    incluidas = []
    
    for item in data:
        date = int(item[0][4:]+ item[0][2:4]+ item[0][:2])
        if  fecha1 <= date <= fecha2:
            incluidas.append(item)
    
    final = []
    mayor = 0
    
    for item in incluidas:
        if float(item[2]) > mayor:
            final = item
            mayor = item[2]
            
    print(final)
    
def top5(data):
    dic = {}
    
    for item in data:
        if item[3] not in dic.keys():
            dic[f"{item[3]}"] = [float(item[2]) - float(item[1])]
        else:
            dic[f"{item[3]}"].append(float(item[2]) - float(item[1]))
    
    for key, value in dic.items():
        dic[key] = (sum(value) / len(value))*-1
    
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    if len(sorted_dic) >= 5:
        top5 = sorted_dic[:4]
        for k in top5:
            print(k)
    else:
        top = sorted_dic[:len(sorted_dic)]
        for k in top:
            print(k)
    
    
    
def arc_frio(data):
    lista = []
    dic = {}
    for item in data:
        if item[3] not in dic.keys():
            dic[f"{item[3]}"] = [item]
        else:
            dic[f"{item[3]}"].append(item)

    for key, value in dic.items():
        v = 0
        t = 0
        for i in value:
            t += 1
            if float(i[1]) < 0:
                v += 1
        if (v / len(value))*100 >= 10:
            lista.append([key,v,t])
           
        
    with open(file="frio.csv", mode="w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for linea in lista:
            writer.writerow(linea)

def menu():
    print("""
          1- Registro nueva lectura
          2- Filtrar temperatura mas alta por fecha
          3- Top 5 estaciones con mas amplitud termica
          4- Archivo frio.csv
          5- Salir
          """)
    
def main():
    
    data = obtener_data()
    menu()
    user = int(input("Ingrese una opcion: "))
    while user != 5:
        if user == 1:
            registro_lectura()
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 2:
            segun_fecha(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 3:
            top5(data)
            menu()
            user = int(input("Ingrese una opcion: "))
        elif user == 4:
            arc_frio(data)
            menu()
            user = int(input("Ingrese una opcion: "))

main()
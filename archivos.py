import csv

def obtener_data_txt():
    
    lista = []
    
    with open(file="arc.txt", encoding="utf8", mode="r",newline="\n") as f:
    
        for linea in f:
            linea = linea.strip("\r\n")
            linea_l = linea.split(",")
            lista.append(linea_l)
        
        return lista

def write_txt(lista):
    #TODOS LOS ITEMS DEBEN SER STR
    f = open("arc","w",encoding="UTF-8",newline='')
    
    for i in range(len(lista)):
        lista[i] = ", ".join(lista[i]) + "\n"
    
    f.writelines(lista)
    f.close()

def obtener_data_csv():
    
    lista = []
    
    with open('arc.csv',encoding='utf8') as file:
        reader = csv.reader(file, delimiter=";")
        for linea in reader:
            lista.append(linea)
    return lista

def write_csv(lista):
    
    with open(file="arc.csv", mode="w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        for linea in lista:
            writer.writerow(linea)

def cargar_vacunado(data):
    id = int(input("Ingrese el ID del vacunado: "))
    año_nacimiento = int(input("Ingrese el año de nacimiento del vacunado: "))
    año_vacunacion = int(input("Ingrese el año de vacunacion del vacunado: "))
    lote = input("Ingrese el lote de vacunas: ")
    dic = {
        "id": id,
        "año_nacimiento": año_nacimiento,
        "año_vacunacion": año_vacunacion,
        "lote": lote,
    }
    data.append(dic)
    
def mayores_70(data):
    mayores = 0
    for dic in data:
        if dic["año_nacimiento"] <= 1953:
            mayores += 1
    print(f"\nLos vacunados con mas de 70 años son {mayores}")
    
def avance_vacunacion(data):
    pass

def lote_escaso(data):
    lotes = []
    escaso = []
    for dic in data:
        lotes.append(dic["lote"])
    print(lotes)
    
    
    for lote in lotes:
        counter = lotes.count(lote)
        if (counter/len(lotes))*100 < 10:
            escaso.append(lote)
    print("Los lotes que abarcan menos del 10'%' son: ")
    for i in escaso:
        print(i)
    if escaso == []:
        print("No hay lotes que cumplan el requisito")  

def segun_año(data):
    user = int(input("Ingrese un año para obtener los vacunados aquel año: "))
    coincide = []
    for dic in data:
        if user == dic["año_nacimiento"]:
            coincide.append(dic)
            
    for dic in coincide:
        print(f"-----------\nID: {dic['id']}\nAño de vacunacion: {dic['año_vacunacion']}\nLote: {dic['lote']}\n-----------")

def main():

    data = [{
        "id": 18587,
        "año_nacimiento": 1979, 
        "año_vacunacion": 2020,
        "lote": "A123"
            },
            {
        "id": 12345,
        "año_nacimiento": 1984, 
        "año_vacunacion": 2021,
        "lote": "A124"      
                
            },
            {
        "id": 13123,
        "año_nacimiento": 1974, 
        "año_vacunacion": 2021,
        "lote": "A123"
            },
            {
        "id": 18587,
        "año_nacimiento": 1979, 
        "año_vacunacion": 2021,
        "lote": "B111"
            }]
    print("""
          1- Ingresa informacion de un nuevo vacunado\n
          2- Acceda a la cantidad de vacunados mayores a 70 años de edad\n
          3- Acceda a la informacion respecto al avance de la vacunacion\n
          4- Acceda a los lotes que abarcan menos del 10'%' de vacunados\n
          5- Ingrese un año y obtenga los vacunados nacidos ese año
          """)
    opciones = input("Ingrese una opcion: ")
    if opciones == "1":
        cargar_vacunado(data)
        print(data)
    elif opciones == "2":
        mayores_70(data)
    elif opciones == "3":
        avance_vacunacion()
        pass
    elif opciones == "4":
        lote_escaso(data)
        pass
    elif opciones == "5":
        segun_año(data)
        
    print("""
          1- Ingresa informacion de un nuevo vacunado\n
          2- Acceda a la cantidad de vacunados mayores a 70 años de edad\n
          3- Acceda a la informacion respecto al avance de la vacunacion\n
          4- Acceda a los lotes que abarcan menos del 10'%' de vacunados\n
          5- Ingrese un año y obtenga los vacunados nacidos ese año
          """)
    opciones = input("Ingrese una opcion: ")

main()
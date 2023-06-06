

def creardiccionario(cadena,num):
    palabras = cadena.split(" ")
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    diccionario_palabras = {}
    for palabra in palabras:
        for letra in letras:
            if palabra[0] == letra:
                if letra not in diccionario_palabras.keys():
                    diccionario_palabras[letra] = [palabra]
                else:
                    diccionario_palabras[letra].append(palabra)
   
    diccionario_filtrado = {}
    for key in diccionario_palabras.keys():
        for palabra in diccionario_palabras[key]:
              if diccionario_palabras[key].count(palabra) >= num:
                  if key not in diccionario_filtrado:
                    diccionario_filtrado[key] = [palabra]
                  else:
                      diccionario_filtrado[key].append(palabra)
    
    for key in diccionario_filtrado:
        unica = list(set(diccionario_filtrado[key])) #utilizo un set q no permite elementos repetidos, lo transformo a lista y se lo asigno a la claveee
        diccionario_filtrado[key] = unica
                
    
    return diccionario_filtrado
    
    
                        
def main():
    #cadena = "este es un ejemplo de como resolver este ejercicio de parcial que es muy sencillo"
    #num = 2
    print("El programa filtrara las palabras que aparezcan el numero que usted asigne o mas veces")
    cadena = input("Ingrese un texto:")
    num = int(input("Ingrese un numero: "))
    
    dic = creardiccionario(cadena,num)
    print(dic)
main()
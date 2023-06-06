
def crear_substring(cad,ind):
    for num in ind:
        if num > len(cad) or num < 0:
            ind.remove(num)
            
    
    lis = list(cad)
    
    new_str = []
    
    print(lis)
    
    for i in range(len(lis)):
        if i in ind:
            new_str.append(lis[i])
            
    
    print(new_str)
        
        
    

def main():
    
    #cadena = input("Ingrese una cadena: ")
    #indices = []
   
    #user = int(input("Numero: "))
    #while user != 111:
    #    indices.append(user)
    #    user = int(input("Otro (break w/111): "))
        
     
    cadena = "pzureta"
    indices = [0,2,4,3,5,6]
    
    
    crear_substring(cadena,indices)
    
main()
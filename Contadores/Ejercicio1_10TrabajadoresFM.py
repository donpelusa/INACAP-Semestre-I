#Realice un algoritmo que permita ingresar los datos de 10 trabajadores.
#Se conoce: Nombre , genero(F/M), Sueldo.
#Se requiere conocer el numero de trabajadores por género

import os

cont=0
acum_f=0
acum_m=0


while cont<5:  
    os.system("cls")
    nombre=input("Ingrese nombre del trabajador: ")
    
    genero=""       
    while genero!='F' and genero!='M':
        genero=input("Ingrese género del trabajador (F/M): ").upper()
        if genero=="F":
            acum_f+=1
        else:
            acum_m+=1   
                
    sueldo=int(input("Ingrese sueldo del trabajador: "))
    print("F: ",acum_f)
    print("M: ",acum_m)
    input()
    cont+=1

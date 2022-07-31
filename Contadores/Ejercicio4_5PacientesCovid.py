#Desarrolle un programa que permita ingresar 5 pacientes con los siguientes datos:
#Nombre
#Edad (entre 20 y 50 años).Validar
#Señale si el test es (N/P)  Negativo / Positivo
#una vez ingresados los 5 pacientes, indique cuantos de ellos presentan covid

import os

cont=0
acum_covid=0

while cont<5:
    os.system("cls")
    nombre=input("Ingrese nombre paciente: ")
    edad=0
    while edad<20 or edad>50:
        edad=int(input("Ingrese edad paciente (entre 20 y 50 años): "))
    covid=""
    while covid!="N" and covid!="P":
        covid=input("Ingrese si test es Negativo/Positivo (N/P): ").upper()
        if covid=="P":
            acum_covid+=1
    print("C19: ",acum_covid)
    input()    
    cont+=1

print("La cantidad de pacientes con Covid es ",acum_covid)
input()


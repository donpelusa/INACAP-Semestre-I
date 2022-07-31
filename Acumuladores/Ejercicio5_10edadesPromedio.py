#Desarrolla un algoritmo que permite ingresar 10 edades y al finalizar entrega el promedio de ellas
#Para lograr el promedio se deben sumar todas las edades ingresadas.

import os

cont=0
acum=0

while cont<10:
    os.system("cls")
    edad="0"
    edad=int(input("Ingrese edad: "))
    acum=acum+edad
    cont+=1

os.system("cls")    
print("El promedio de edades es: ",acum/cont)
input()

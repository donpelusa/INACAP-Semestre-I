#Realice un programa que permita ingresar un nombre y entregar el largo del nombre y la letra con la cual comienza.

import os

def determina_largo(nom):
    return len(nom)

def comienza_con(let):
    return let[0]

os.system("cls")
nombre=str(input("Ingrese nombre: "))
largo=determina_largo(nombre)


print("El largo de caracteres del nombre es: ",largo)
print("La primera letra del nombre es ",comienza_con(nombre))
input()
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])
print(nombre[6])
input()

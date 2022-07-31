#Realice un programa que permita ingresar un nombre y luego que permita ingresar un apellido.
#Muestre el nombre y el apellido juntos, pero entre el nombre y apellido separado por un espacio

import os

def concatenar(a,b):
    conca=a+" "+b
    return conca


nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
print(concatenar(nombre,apellido))
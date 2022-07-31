#Realice un programa que permita ingresar dos números enteros y entregue el menor valor entre ellos. 
#Construya una función con paso de parámetros (la salida debe entregarla el programa principal)

import os

def calcula (a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return "Son iguales"

os.system("cls")
num1=int(input("Ingrese num1: "))
num2=int(input("Ingrese num2: "))
menor=calcula(num1,num2)
input()
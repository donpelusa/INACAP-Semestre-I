#Desarrolle un programa que permita ingresar 5 números y determine cuantos de ellos son pares.
#Además cada vez que se ingrese el numero entregue el mensaje
#“el numero es xxxxxx”  donde xxxxxx señala la palabra par / impar según corresponda

import os

cont=0
num=0
num_par=0
num_impar=0

while cont<5:
    os.system("cls") 
    num=int(input("Ingrese un número: "))
    if num%2==0:
        print("El número es par")
        num_par+=1
    else:
        print("El número es impar")
        num_impar+=1
    input()
    cont+=1
os.system("cls")
print("Números pares: ",num_par)
print("Números impares: ",num_impar)
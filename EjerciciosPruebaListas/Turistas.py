#Realice un programa que permita ingresar los datos de turistas que viajan a ciudades de distintos países
#1.- Ingresar Turista(Nombre, ciudad, país, sexo(Hombre o mujer)
#2.- Mostrar el nombre del turista que cumple con el siguiente criterio( ciudad a la que viaja y su sexo), 
#   ejemplo quienes y cuantas mujeres  viajaron a “Paris”
#3.- Crear una lista nueva con las personas que viajaron a un determinado pais

import os

turistas=[]
switch=0
cont=0


def menu():
    os.system('cls')
    print("Menu")
    print("1.- Ingrese Turista")
    print("2.- Mostrar coincidencia")
    print("3.- Crear lista nueva por país")
    print("4.- Salir")
    return int(input("\nIngrese opción: "))

def op1():
    os.system('cls')
    q_ingresos=int(input("Ingrese cantidad de turistas a ingresar: "))
    for i in range(q_ingresos):
        os.system('cls')
        nombre=str.upper(input("Ingrese nombre del turista: "))
        ciudad=str.upper(input("Ingrese ciudad a la que viaja: "))
        pais=str.upper(input("Ingrese país al que viaja: "))
        sexo=str.upper(input("Ingrese sexo del turista [M/F]: "))
        turistas.append([nombre,ciudad,pais,sexo])

def op2():
    os.system('cls')
    ciudad=str.upper(input("Ingrese ciudad: "))
    sexo=str.upper(input("Ingrese género: "))
    print("\nDatos consultados: ",ciudad,sexo,end=" ")    
    for i in range(len(turistas)):
        if ciudad in turistas[i][1] and sexo in turistas[i][3]:
            print("\nNombre: {}".format(turistas[i][0]))
            switch=1       
    input()
    if switch==0:
        input("No hay coincidencias")

def op3():
    lista=[]
    os.system('cls')
    pais=str.upper(input("Ingrese país para generar lista: ")) 
    for i in range(len(turistas)):
        if pais in turistas[i][2]:
            lista.append(turistas[i][0])
    print(lista)
    input()
        

while True:
    opcion=menu()
    if opcion==1:
        op1()
    elif opcion==2:
        op2()
    elif opcion==3:
        op3()
    elif opcion==4:
        input("Presione enter para salir")
        break
    else:
        input("Valor incorrecto, intente nuevamente...")

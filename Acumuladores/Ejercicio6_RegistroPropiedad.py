#Desarrolle un programa que permita ingresar 4 registros correspondiente a la compraventa de una propiedad.

import os

cont=0
acum_valor_prop=0
acum_casa=0
acum_dpto=0
impuesto_prop=0

#Se conoce los siguientes datos:
#     Nombre propietario
#     Tipo propiedad(C/D) Casa o departamento. Validar
#     Acción a realizar (V/C) Venta o compra
#     Monto de la propiedad

while cont<4:
    os.system("cls")
    nombre_prop=input("Ingrese nombre del propietario: ")
    tipo_prop=""
    while tipo_prop!="C" and tipo_prop!="D":
        tipo_prop=input("Ingrese tipo de propiedad (C/D): ").upper()
    gestion_prop=""
    while gestion_prop!="V" and gestion_prop!="C":
        gestion_prop=input("Ingrese acción a realizar (V/C): ").upper()
    valor_prop=int(input("Ingrese monto de la propiedad: "))
    
#Se pide determinar:
#Impuesto a cancelar por el propietario de acuerdo a lo siguiente:
#Si es venta cancela un impuesto de un 10% del monto de la propiedad
#Si es compra cancela un impuesto de un 5% del monto de la propiedad
    if gestion_prop=="V":
        impuesto_prop=valor_prop*0.1
    else:
        impuesto_prop=valor_prop*0.05        

#Se pide una vez ingresados lo datos del propietario, muestre por cada propietario
#Nombre propietario
#Tipo de propiedad en palabras
#Acción en palabras
#Monto de la propiedad
#Pago impuesto

    print("Nombre propietario: ",nombre_prop)
    if tipo_prop=="C":
        print("Tipo propiedad: Casa")
        acum_casa+=1
    else:
        print("Tipo propiedad: Departamento")
        acum_dpto+=1
    
    if gestion_prop=="V":
        print("Tipo gestión: Venta")
    else:
        print("Tipo gestión: Arriendo")
    print("Monto propiedad: ",valor_prop)
    print("Monto impuesto: ",round(impuesto_prop))
    acum_valor_prop=acum_valor_prop+valor_prop
    cont+=1
    input()
    

#Al finalizar debe mostrar: Monto total de las propiedades / Nª de casas registradas / Nª de deptos. registrados

os.system("cls")
print("Monto total de las propiedades: ",acum_valor_prop)
print("Número de casas registradas: ",acum_casa)
print("Número de departamentos registrados: ",acum_dpto)
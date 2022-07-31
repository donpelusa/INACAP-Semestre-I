#3.- Se tiene los datos de vehículos que han sido arrendados en el último mes, para esto Renta Car, 
# requiere un programa que lleve el control de los vehículos arrendados. Se conoce los siguientes datos: 

import os

ingreso="S"
while ingreso=="S" or ingreso=="s":
    #•	Nombre del Arrendatario
    nom_arrendatario=input("Ingrese nombre de arrendatario: ")

    #•	Modelo del vehículo (se ingresa S para el Sedán y un T para la Camioneta). Validar

    modelo_vehiculo=""
    while modelo_vehiculo!="S" and modelo_vehiculo!="s" and modelo_vehiculo!="T" and modelo_vehiculo!="t":
        modelo_vehiculo=input("Ingrese modelo del vehículo (S/T): ")

    #•	Kms. Inicio, corresponde el kilometraje al salir de la automotora
    kms_inicio=int(input("Ingrese kms inicio:"))

    #•	Kms. Final, corresponde al kilometraje al ingresar el vehículo a la automotora
    kms_final=int(input("Ingrese kms final:"))

    #•	N° de pasadas por los pórticos controlados por TAG (entre 1 y 10). Validar
    nro_tag=0
    while nro_tag<1 or nro_tag>10:
        nro_tag=int(input("Ingrese nro de pasadas por pórtico TAG: "))
        
    #Los vehículos pagan un arriendo por cada 10 Km recorridos a un valor de $1.000
    #Los vehículos sedan pagan un impuesto fijo de $5.000 y las camionetas un impuesto fijo de $7.500. 
    #Cada pórtico tiene un valor promedio de $377. 
    #Pago Pórtico = N° de pasadas * valor del Pórtico
    pago_portico=nro_tag*377

    #A.	Se pide realizar un programa que calcule y muestre los siguientes datos: 
    #•	Nombre del arrendatario 
    print("Nombre Arrendatario: ", nom_arrendatario)

    #•	Kms. Recorridos (diferencia entre Kms Final – Kms Inicio)
    kms_recorridos = kms_final-kms_inicio
    print("Kms Recorridos: ",kms_recorridos)

    #•	El valor a pagar del vehículo arrendado   = ((Kms. Recorridos/10) *$1.000) + impuesto fijo+ Pago Pórtico
    if modelo_vehiculo=="S" or modelo_vehiculo=="s":
        valor_pago =int(((kms_recorridos/10)*1000)+5000+pago_portico)
    else:
        valor_pago =int(((kms_recorridos/10)*1000)+7000+pago_portico)

    #•	Mensaje de acuerdo al valor a pagar. 
    print("El valor a pagar es: $",valor_pago)
    # Si el valor a pagar está sobre $500.000, 
    # se debe mostrar al final “Próximo arriendo recibe una oferta descuento”,
    # en caso contrario, “próximo arriendo recibe agradecimientos”
    if valor_pago>500000:
        print("Próximo recibe una oferta descuento")
    else:
        print("Próximo arriendo recibe agradecimientos")

    ingreso=input("Desea ingresar otro registro? (S/N): ")
    os.system('cls')

#El programa debe permitir ingresar más de un vehículo (Utilice el while para ingresar más de 1 vehículo)

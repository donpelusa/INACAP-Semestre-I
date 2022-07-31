#Ejercicio a resolver 
#Realice un programa en Python que interprete los resultados de los exámenes de sangre de 5 pacientes:

import os

cont=0
acum_fonasa=0
acum_isapre=0
acum_pago=0
acum_pago_fonasa=0
acum_pago_isapre=0
acum_riesgo=0
acum_riesgo_fonasa=0
valor_con_dcto=0

#Los datos que se ingresan al sistema son:
#	Nombre del paciente
#	Tipo de salud (F / I ) -  FONASA   ISAPRES. Validar los valores
#	Valor del bono
#	N° de Leucocitos (entre 4000 y 10000). Validar
#	Edad (Entre 15 y 75 años). Validar

while cont<5:
    os.system("cls")
    nombre_paciente=input("Ingrese nombre paciente: ")
    tipo_salud=""
    while tipo_salud!="F" and tipo_salud!="I":
        tipo_salud=input("Ingrese tipo salud (F/I): ").upper()
        if tipo_salud=="F":
            acum_fonasa+=1
        else:
            acum_isapre+=1
    valor_bono=int(input("Ingrese valor bono: "))
    num_leucocitos=0
    while num_leucocitos<4000 or num_leucocitos>10000:
        num_leucocitos=int(input("Ingrese n° de leucocitos: "))
    edad_paciente=0
    while edad_paciente<15 or edad_paciente>75:
        edad_paciente=int(input("Ingrese edad del paciente: "))
        
 #Mostrar por cada paciente
#•	Nombre del paciente:
#•	Tipo de Salud en palabras
#•	Valor del Bono a pagar (realizado el descuento):
#•	Observación correspondiente según N° Leucocitos:
#Condiciones o reglas del Negocio:
#El Rango Normal de Leucocitos es cuando está sobre los 7.000. Si se encuentra bajo los 7.000 leucocitos, 
#debe decir “Su salud se encuentra en riesgo”, en caso contrario colocar ”Su salud esta Normal”.

#Los bonos tendrán el siguiente descuento: (Fonasa – 25% de descuento del valor del bono, Isapres – 10% de descuento del valor del bono)


    os.system("cls")
    print("Nombre del paciente: ",nombre_paciente)
    
    if tipo_salud=="F":
        print("Tipo de salud: Fonasa")
        valor_con_dcto=round(valor_bono*0.75)
        acum_pago_fonasa=acum_pago_fonasa+valor_con_dcto
    else:
        print("Tipo de salud: Isapre")
        valor_con_dcto=round(valor_bono*0.9)
        acum_pago_isapre=acum_pago_isapre+valor_con_dcto
    acum_pago=acum_pago+valor_con_dcto
    print("Valor del Bono a pagar: ",valor_con_dcto)
    print("N° Leucocitos: ",num_leucocitos)
    if num_leucocitos<7000:
        acum_riesgo+=1
        print("Su salud se encuentra en riesgo")
        if tipo_salud=="F":
            acum_riesgo_fonasa+=1
    else:
        print("Su salud esta Normal")                   
    input()
    cont+=1
#Al finalizar debe mostrar los siguientes totales
#•	N° de pacientes por tipo de salud
#•	Monto total de pagos
#•	Monto total de pagos por tipo de salud
#•	Nª de pacientes que se encuentran en riesgo de salud
#•	Nª de pacientes de Fonasa en riesgos de salud
os.system("cls")
print("N° Pacientes Fonasa: ",acum_fonasa)
print("N° Pacientes Isapre: ",acum_isapre)
print("Monto total de pagos: ",acum_pago)
print("Monto pagos Fonasa: ",acum_pago_fonasa)
print("Monto pagos Isapre: ",acum_pago_isapre)
print("N° Pacientes Riesgo Salud: ",acum_riesgo)
print("N° Pacientes Riesgo Salud Fonasa: ",acum_riesgo_fonasa)
input()





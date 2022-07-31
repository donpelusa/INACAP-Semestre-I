#importo biblioteca para limpiar pantalla
import os
#Nombre del estudiante
ingreso="S"
while ingreso=="s" or ingreso== "S":
    nom_estudiante=input("Ingrese nombre del estudiante  :")
    #N° de Hojas impresas (entre 10 y 100). Validar
    #Debo inicializar el while 
    q_hojas_impresas=0
    while q_hojas_impresas<10 or q_hojas_impresas>100:
        q_hojas_impresas=int(input("Ingrese n° de hojas impresas :"))
    #Tipo hoja (C/O/A)- Carta – Oficio - A4. Validar  
    tipo_hoja=""
    while tipo_hoja!="C" and tipo_hoja!="c" and tipo_hoja!="O" and tipo_hoja!="o" and tipo_hoja!="a" and tipo_hoja!="A":
        tipo_hoja=input("Ingrese tipo de hoja C/O/A4 : ")
    #Entrega (N/U), donde N es Normal y U es Urgente. Validar
    tipo_entrega=""
    while tipo_entrega!="U" and tipo_entrega!="u" and tipo_entrega!="N" and tipo_entrega!="n":
        tipo_entrega=input("Ingrese tipo de Entrega (N/U) : ")
    #Tipo de carrera(T/P). Donde (T)écnica y (P)Profesional. Validar
    tipo_carrera=""
    while tipo_carrera!="T" and tipo_carrera!="t" and tipo_carrera!="p" and tipo_carrera!="P":
        tipo_carrera=input("Ingrese tipo de Entrega (T/P) : ")

    #Se conoce el valor impreso de la hoja:
    #Carta es de $120, Oficio es de $135 y el formato A4 es de $100
    #Todos los trabajos urgentes se les cobra un costo adicional de un 20% del valor de la impresión, cualquier otro tipo de trabajo se les asigna un costo adicional de un 2% del valor de la impresión
    #valor de la impresión = N° hojas impresas * Valor hoja 
    #Costo adicional = valor impresión * tasa de costo adicional (Según entrega)
    #Valor a pagar = Valor de la impresión + costo adicional
    
    if tipo_hoja=="C" or tipo_hoja=="c":
        valor_impresion=q_hojas_impresas*120
    elif tipo_hoja=="O" or tipo_hoja=="o":
        valor_impresion=q_hojas_impresas*135
    else:
        valor_impresion=q_hojas_impresas*100
    #Todos los trabajos urgentes se les cobra un costo adicional de un 20% del valor de la impresión, cualquier otro tipo de trabajo se les asigna un costo adicional de un 2% del valor de la impresión
    if tipo_entrega=="U" or tipo_entrega=="u":
        valor_pago=valor_impresion*1.2
    else:
        valor_pago=valor_impresion*1.02
    print("Estudiante: ", nom_estudiante)
    
    print=input("Desea ingresar otro registro :")    
    if tipo_carrera=="T" or tipo_carrera=="t":
        print ("Carrera: Técnico")    
    else:
        print ("Carrera: Profesional")
    if tipo_hoja=="C" or tipo_hoja=="c":
        print ("Hoja: Carta")
    elif tipo_hoja=="O" or tipo_hoja=="o":
        print ("Hoja: Oficio")    
    else:
        print ("Hoja: A4")

    print ("Valor a pagar: ", valor_pago)
        

    #Se pide Mostrar por cada ingreso:
    #•	Nombre del estudiante
    #•	Tipo Carrera (en palabra) 
    #•	Tipo hoja utilizada (en palabras) 
    #•	Valor a cancelar
    os.system("cls")

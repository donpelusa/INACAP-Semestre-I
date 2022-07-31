import os

menu = 0

while menu !=2:
    print ("")
    print ("Bienvenidos a Inacap impresiones")
    print ("")
    print ("Seleccione una opcion")
    print ("1.- Ingresar estudiante inacap")
    print ("2.- Salir")
    menu = int(input("Seleccione opcion: "))
    if menu == 1:
        # Las variables se inician en 0 y vacios dependiendo del tipo de dato
        nombre = ""
        Numero_de_hojas = 0
        tipo_hoja = ""
        entrega = ""
        carrera = ""
        valor = 0

        nombre = input("ingrese su nombre: ")
        
        while Numero_de_hojas < 10 or Numero_de_hojas >100:
            Numero_de_hojas = int(input("Ingrese numero de hojas (10/100): "))

        while tipo_hoja != 'C' and tipo_hoja != 'O' and tipo_hoja != 'A':
            tipo_hoja = input("Ingrese tipo de hoja (C/O/A): ")
            tipo_hoja = tipo_hoja.upper()
        
        while entrega != 'N' and entrega != 'U':
            entrega = input("Ingrese tipo de entrega (N/U): ")
            entrega = entrega.upper()

        while carrera != 'T' and carrera != 'P':
            carrera = input("Ingrese tipo de carrera (T/P): ")
            carrera = carrera.upper()

        if tipo_hoja == "C":
            valor = Numero_de_hojas*120
        elif tipo_hoja == "O":
            valor = Numero_de_hojas*135
        elif tipo_hoja == "A":
            valor = Numero_de_hojas*100

        if entrega == "N":
            valor = valor + int(valor * 0.02)
        elif entrega == "U":
            valor = valor + int(valor * 0.20) 

        if carrera == "T":
            carrera = "Tecnico"
        elif carrera == "P":
            carrera = "Profesional"

        if tipo_hoja == "C":
            tipo_hoja = "Carta"
        elif tipo_hoja == "O":
            tipo_hoja = "Oficio"
        elif tipo_hoja == "A":
            tipo_hoja = "A4"

        print ("") 
        print ("nombre: ",nombre)
        print ("carrera: ", carrera )
        print ("Tipo de hoja: ", tipo_hoja )
        print ("Valor: ", valor)
        print ("")

        continuar = input("Presione enter para continuar")
        os.system("cls")

    elif menu == 2:
        print ("")
        print ("Ha salido del programa Muchas gracias")
        print ("")
    else: 
        print ("Ha seleccionado una opcion incorrecta")
        continuar = input("Presione enter para continuar")
        os.system("cls")
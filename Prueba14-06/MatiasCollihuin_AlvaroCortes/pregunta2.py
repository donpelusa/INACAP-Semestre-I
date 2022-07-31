import os

lista_cliente=[]

def menu():
    os.system('cls')
    print("1.- Ingresar los datos de los clientes (Rut, Nombre, tipo de cuenta, saldo)")
    print("2.- Consultar por tipo de cuenta")
    print("3.- Operación (Depositar / Girar)")
    print("4.- Salir")
    return int(input("\nIngrese opción: "))

def op1():
    os.system('cls')
    cuenta=""
    rut=str.upper(input("Ingrese rut: "))
    nombre=str.upper(input("Ingrese nombre: "))
    while cuenta!="C" and cuenta!="A":
        cuenta=str.upper(input("Ingrese tipo cuenta [C]orriente/[A]horro: "))
    saldo=int(input("Ingrese saldo: "))
    lista_cliente.append([rut,nombre,cuenta,saldo])
    print("\n",lista_cliente,end=(" "))
    input("\nDato ingresado, presione enter para salir")

def op2():
    lista_tcuenta=[]
    acumulador=0
    switch=0
    tipo_cuenta=str.upper(input("Ingrese tipo de cuenta a buscar ([C] o [A]):"))
    for i in range(len(lista_cliente)):
        if tipo_cuenta in lista_cliente[i][2]:
            acumulador+=lista_cliente[i][3]
            lista_tcuenta.append(lista_cliente[i][1])
            switch=1
            
    if switch==0:
        input("No se encontraron coincidencias...")
    else:
        print("\nLista creada en base a coincidencia:")
        print(lista_tcuenta)
        print("El total acumulado es: ",acumulador)
        input("\nIngrese enter para continuar...")
        
def op3():
    os.system('cls')
    operacion=""
    switch=0
    monto_op=0
    rut_cli=str.upper(input("Ingrese rut a operar: "))
    indice=0
    for i in range(len(lista_cliente)):
        if rut_cli in lista_cliente[i][0]:
            indice=i
    
    if rut_cli in lista_cliente[indice][0]:
        switch=1
        while operacion!="D" and operacion!="G":
            operacion=str.upper(input("Ingrese operación [D]epósito/[G]iro: "))
        if operacion=="G":
            monto_op=int(input("Ingrese monto: "))
            if monto_op>lista_cliente[indice][3]:
                input("Monto a girar es mayor al disponible")
            else:
                lista_cliente[indice][3]-=monto_op
                print("Su nuevo saldo es: ",lista_cliente[indice][3])
                input("Giro realizado...")
        else:
            monto_op=int(input("Ingrese monto: "))
            lista_cliente[indice][3]+=monto_op
            print("Su nuevo saldo es: ",lista_cliente[indice][3])
            input("Depósito realizado...")
    if switch==0:
        input("No se encontraron coincidencias...")

while True:
    opcion=menu()
    if opcion==1:
        op1()
    elif opcion==2:
        op2()
    elif opcion==3:
        op3()
    elif opcion==4:
        os.system('cls')
        input("Hasta luego!")
        break
    else:
        print("Opción no válida, intente nuevamente...")


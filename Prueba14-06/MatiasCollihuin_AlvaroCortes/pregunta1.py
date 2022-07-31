import os
def agregar():
    numero=int(input("Ingrese el numero que quiere ingresar: "))
    lista.append(numero)
    return

lista=[]
switch=0
while True:
    os.system('cls')
    print("1.- Para crear la lista de 5 numeros o borrar la actual e ingresar una nueva.")
    print("2.- Para eliminar un numero de la lista.")
    print("3.- Para ordenar y mostrar la lista actual. ")
    print("4.- Salir.")
    print("-"*40)
    op=int(input("Seleccione la opcion que desea: "))
    if op==1:
        if lista == []:
            for i in range(5):
             agregar()
        else:
            lista=[]
            for i in range(5):
             agregar()
        print("La lista de numeros queda asi: ",lista)
        print("-"*40)
        input("Presione cualquier letra para volver al menu principal.")
        os.system('cls')
    elif op==2:
        if lista == []:
            print("Debe tener creada una lista, porfavor cree una con opcion 1.")
            print("-"*40)
            input("Presione cualquier letra para volver al menu principal.")
            os.system('cls')
            continue
        else:
            print("La lista de numeros es la siguiente: ",lista)
            elim_num=int(input("Ingrese el numero que desea eliminar: "))
            if elim_num in lista:
                lista.remove(elim_num)
                switch=1
            if switch == 0:
                print("El numero que desea eliminar no existe en la lista. Intente nuevamente ingresando otro numero.")
            switch = 0
            print("La lista de numeros es: ",lista)
            print("-"*40)
            input("Presione cualquier letra para volver al menu principal.")
            os.system('cls')
    elif op == 3:
        if lista == []:
            print("Debe tener creada una lista, porfavor cree una con opcion 1.")
            print("-"*40)
            input("Presione cualquier letra para volver al menu principal.")
            os.system('cls')
            continue
        else:
            print("La lista de numeros es la siguiente: ",lista)
            lista.sort()
            print("La lista de numeros ordenada es la siguiente: ",lista)
            print("-"*40)
            input("Presione cualquier letra para volver al menu principal.")
            os.system('cls')
    else:
        print("Adios.")
        break
os.system('cls')

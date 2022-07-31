import os

lista=[]
opcion=0

def menu():
    os.system('cls')
    print("Menu")
    print("1.- Agregar estudiante")
    print("2.- Eliminar estudiante")
    print("3.- Buscar estudiante")
    print("4.- Ordenar la lista")
    print("5.- Ver lista")
    print("6.- Salir")
    return input("\nIngrese opción: ")

def op1():
    os.system('cls')
    print("Lista:",lista,end=" ")
    ingreso=str(input("\nIngrese nombre de alumno: "))
    lista.append(ingreso)
    print("\nLista nueva:",lista,end=" ")
    input()

while True:
    opcion=int(menu())
    if opcion==1:
        op1()
    elif opcion==2:
        print("Lista:",lista,end=" ")
        lista.remove(str(input("Ingrese nombre a eliminar: ")))
        input()
    elif opcion==6:
        break
    else:
        input("Opción no válida, intente de nuevo...S")
        
        
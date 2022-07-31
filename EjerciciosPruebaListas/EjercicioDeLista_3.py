import os

lista=[2,4,6,8,10]
opcion=0

def menu():
    os.system('cls')
    print('Opción 1: Sumar la lista y entregar el resultado.')
    print('Opción 2: Eliminar algún número que se encuentre en la lista.')
    print('Opción 3: Agregar un nuevo numero a la lista.')
    print('Opción 4: Ordenar la lista y mostrarla.')
    print('Opción 5: Entregar número de elementos de la lista.')
    print('Opción 6: Salir')
    return input("\nIngrese opción: ")

def op1():
    suma=0
    for i in lista:
        suma+=i
    print("\nValores de lista:",lista,end=" ")
    print("\nLa suma de los números es: ",suma)
    input("Presione enter para volver...")

def op2():
    borrar_num=""
    while borrar_num not in lista:
        print("\nValores de lista:",lista,end=" ")
        borrar_num=int(input("\n\nIngrese el valor a eliminar: "))
    
        if borrar_num not in lista:
            print("\nNúmero no encontrado en la lista...")
            input("Presione enter para volver...")
        else:   
            lista.remove(borrar_num)
            print("\nLuego de borrar quedó asi:",lista,end=" ")
            input("\nPresione enter para volver...")
            break

def op3():
    print("\nValores de lista:",lista,end=" ")
    lista.append(int(input("\n\nIngrese el valor a agregar: ")))
    print("\nLista con valor agregado:",lista,end=" ")
    input("\nPresione enter para volver...")

def op4():
    print("\nValores de lista:",lista,end=" ")
    lista.sort()
    print("\nValores de lista ordenados:",lista,end=" ")
    input("\nPresione enter para volver...")

def op5():
    print("\nValores de lista:",lista,end=" ")
    print("\nNúmero de elementos: ",len(lista))
    input("\nPresione enter para volver...")

while True:
    opcion=int(menu())
    if opcion==1:
        op1()
    elif opcion==2:
        op2()
    elif opcion==3:
        op3()
    elif opcion==4:
        op4()
    elif opcion==5:
        op5()
    elif opcion==6:
        input("\n\nHasta la vista baby!")
        break
    else:
        input("\nOpción no válida, intente de nuevo...")
lista=[2,4,6,8,10]





while True:
    
    print("Opcion 1: Sumar la lista y entregar el resultado.")
    print("Opcion 2: Eliminar algún número que se encuentre en la lista.")
    print("Opción 3: Agregar un nuevo número a la lista.")
    print("Opción 4: Ordenar la lista y mostrarla.")
    print("Opción 5: Entregar número de elementos de la lista.")
    print("Opción 6: Salir")
    opcion=int(input("Ingrese opción (1-6): "))
    
    
    
    if opcion==1:
        suma=0
        for i in lista:
            suma+=i
        print("\nLa suma es: ")
    elif opcion==2:
        elimina=int(input("\nIngrese n° a eliminar: "))
        if elimina not in lista:
            print("No existe")
        else:
            lista.remove(numero)
            print("Eliminado")
            print("Asi queda: ",lista)
        os.system("pause")
    elif opcion==3:
        numero=int(input("Qué número de la lista quieres agregar: "))
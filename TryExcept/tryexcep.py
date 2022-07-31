import os

try:
    def crea():
        alumnos={}
        for i in range(4):
            rut=str(input("Ingrese rut del alumno: "))
            nombre=str.title(input("Ingrese nombre del alumno: "))
            alumnos[rut]=nombre
        print(alumnos)
        print("que rut busca:")
        rut=str(input("Ingrese rut del alumno: "))
        print("El alumno es: ",alumnos[rut])
except KeyError:
    print("Error de clave")


def saludos():
    print("HOLA")


def despedida():
    os.system("cls")
    print("*********")
    print("*                       *")
    print("*                       *")
    print("*NOS VEMOS EN  PRI 2022 *")
    print("*                       *")
    print("*                       *")
    print("*********")
    exit()

cont=False

while cont:
    try: 
        print("Vamos a dividir 2 valores")
        a=int(input("ingrese un dividendo: "))
        b=int(input("Ingrese un divisor: "))
        print("Resultado: ",a/b)
    except ValueError:
            print("Ingreso un valor erróneo")
    except ZeroDivisionError:
            print("No se puede dividir por cero")
            cont=False
            os.system("pause")

while True:
    print("1.- Saludos")
    print("2.- Crear un diccionario" )
    print("3.- Despedida")
    op=int(input("Opcion: "))
    if op==1:
        saludos()
    elif op==2:
        crea()
    else:
        despedida()
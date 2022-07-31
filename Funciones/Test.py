

def caca(abc,n2):
    resul=abc+n2
    return resul






num1=int(input("Ingrese num1: "))
num2=int(input("Ingrese num2: "))


print("Elija:")
print("1: Suma:")
print("2: Resta:")
print("3: Multiplicación:")
print("4: Dividir:")

opcion=int(input("Elija una opción"))

if opcion==1:
    suma(num1,num2)
elif opcion==2:
    resta(num1,num2)
elif opcion==3:
    resultado=caca(num1,num2)
elif opcion==4:
    div(num1,num2)
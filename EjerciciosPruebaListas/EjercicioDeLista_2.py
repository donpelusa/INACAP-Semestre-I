import os

n=int(input("Indique el número de valores a ingresar en la lista: "))
lista_n=[]

for i in range(n):
    x=int(input("Ingrese el valor: "))
    lista_n=lista_n+[x]
print("lista de números: ",lista_n)

lista_dos=[]
for numero in lista_n:
    if numero not in lista_dos:
        lista_dos=lista_dos+[numero]
        
lista_dos.sort()
print("lista dos: ",lista_dos)
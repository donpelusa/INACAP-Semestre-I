
n=int(input("Indique el número de valores a ingresar en la lista: "))
lista_n=[] #contendrá la lista de números ingresados por parte de usuario

#realizar un ciclo para ingresar los números

for i in range(n):
    x=int(input("Ingrese el valor: "))
    lista_n=lista_n+[x] # Es lo mismo que lista_n.append(x)

print("Lista de números: ",lista_n)

#depurar la lista
lista_dos[]

for numero in lista_n:
    if numero not in lista_dos:
        lista_dos=lista_dos+[numero]

lista_dos.sort()
print("Lista dos: ",lista_dos)
import os
frutas={}
total=0
pago=0

for i in range(2):
    fruta=input("Ingrese nombre de fruta: ")
    precio=input("Ingrese precio: ")
    frutas[fruta]=precio
    
print(frutas)
cont=True

while cont:
    fruta=input("Qué fruta quieres?: ")
    kilos=float("Cuantos kilos quieres: ")
    
    if fruta in frutas:
        total=frutas[fruta]*kilos*1.19
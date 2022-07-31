import os

lista1=[2,10,40,20,9]
lista2=[1,2,3,4,5,6,7,8,9,10]
lista3=[]

for i in lista1:
    if i not in lista1:
        lista3.append(i)
        
for i in lista2:
    if i not in lista1:
        lista3.append(i)
        
lista3.sort()
print(lista3)
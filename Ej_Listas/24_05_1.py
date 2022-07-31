
vocales=0

frase_sv=[]

frase=str.upper(input("Ingrese una frase: "))

for i in frase:
    if i in "aeiou".upper():
        vocales+=1
    else:
        frase_sv.append(i)

print("Nro vocales: ", vocales)

print("Frase sin vocales: ", frase_sv)

print("".join(frase_sv))

#print(frase_sv.join(frase))
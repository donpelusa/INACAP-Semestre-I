
cadena = "Hola"
rotada = ""

rotaciones = 1

for letra in cadena:
    # Sacar su número
    representacion_entera = ord(letra)
    # Concatenar
    rotada += chr(representacion_entera + rotaciones)
    
print("La cadena {} al ser rotada {} posiciones, se convierte en {}".format(
    cadena, rotaciones, rotada))
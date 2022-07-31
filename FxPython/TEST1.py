
cadena = "Soy un mensaje"

codificado = []

for letra in cadena:
	codificado.append(ord(letra))

print("El mensaje '{}' se convierte en {}".format(cadena, codificado))
#El supermercado  “La Vega Central” requiere un programa que calcule el pago final a cancelar por el cliente sabiendo 
#que se aplica un descuento según su tipo de pago. Se ingresan al sistema los siguientes datos:
import os

valida_ingreso=""
pago_final=0

while valida_ingreso=="S":
    
#•	Nombre del cliente
    nom_cliente=str(input("Ingrese nombre del cliente: "))
#•	Monto a pagar
    monto_pago=int(input("Ingrese monto a pagar: "))
#•	Tipo de Cliente (A/G-    A es adulto mayor y G es público en general) Validar
    tipo_cliente=""
    while tipo_cliente!="A" and tipo_cliente!="G":
        tipo_cliente=str(input("Ingrese tipo de cliente (A/G): ")).upper()
#•	Forma de Pago (Débito -  Efectivo - Cheque). Validar
    forma_pago=""
    while forma_pago!="D" and forma_pago!="E" and forma_pago!="C":
        forma_pago=str(input("Ingrese forma de pago (D/E/C): ")).upper()

#Según la forma de pago se hará un descuento sobre el monto a pagar:
#Débito hace un descuento de un 10% -  Pago Efectivo hace un descuento de un 20%  - Cheque hace un  descuento  de un 5%
#Monto descuento = monto a pagar * tasa de descuento



#Pago Final = Monto a Pagar – monto descuento
#Se pide mostrar por cada cliente:
#•	Nombre
#•	Forma de pago en palabra
#•	Monto Descuento
#•	Monto a cancelar

#Se pide mostrar al final
#•	Monto Total cancelado
#•	Monto total cancelados por tipo de cliente
#•	Número de adultos mayores que cancelan en efectivo
#•	Número de personas por tipo de cliente

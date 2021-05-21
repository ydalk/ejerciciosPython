print(" *** Programa Credito *** ")
print("")

nombre = input(" Ingrese su nombre: ")
telefono = input(" Ingrese su teléfono: ")
monto = float(input(" Ingrese el monto a solicitar $: "))
cuotas = int(input(" Ingrese la cantidad de cuotas: "))
interes = float(input(" Ingrese el valor del interes: "))


cuota_base = monto / cuotas
interes = cuota_base * 0.1
cuota_total = cuota_base + interes
ganancia_total = interes * cuotas
total_credito = monto + ganancia_total


print(f" { nombre} tiene un credito por {monto} diferido a {cuotas} cuotas, con una cuota base de ${cuota_base} con un interes del {interes} para un total del credito po ${ total_credito } ")

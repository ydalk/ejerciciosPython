
""" Inicio cultivo número 1 """
# definicion y captura de datos
print("")
print(" Datos cultivo # 1 ")
nom1 = input("ingrese el nombre del cultivo #1: ")
cant1 = input("ingrese la cantidad del cultivo: ")
meses1 = input("ingrese el tiempo, en meses, que ha estado cultivado: ")
problemas1 = input("¿existe algún problema con el cultivo? escriba NO o SI: ")

# proceso
cantidad1 = int(cant1)
meses_cultivado1 = float(meses1)
if problemas1 == "NO":
    problemas1 = "no"
elif problemas1 == "SI":
    problemas1 = "si"
print("")
""" Fin cultivo número 1 """

""" Inicio cultivo número 2 """
# definicion y captura de datos
print("")
print(" Datos cultivo # 2")
nom2 = input("ingrese el nombre del cultivo #2: ")
cant2 = input("ingrese la cantidad del cultivo: ")
meses2 = input("ingrese el tiempo, en meses, que ha estado cultivado: ")
problemas2 = input("¿existe algún problema con el cultivo? escriba NO o SI: ")

cantidad2 = int(cant2)
meses_cultivado2 = float(meses2)
if problemas2 == "NO":
    problemas2 = "no"
elif problemas2 == "SI":
    problemas2 = "si"
print("")
""" Fin cultivo número 2 """


""" Información cultivo número 3 """
# definicion y captura de datos
print("")
print(" Datos cultivo # 3 ")
nom3 = input("ingrese el nombre del cultivo #3: ")
cant3 = input("ingrese la cantidad del cultivo: ")
meses3 = input("ingrese el tiempo, en meses, que ha estado cultivado: ")
problemas3 = input("¿existe algún problema con el cultivo? escriba NO o SI: ")


cantidad3 = int(cant3)
meses_cultivado3 = float(meses3)
if problemas3 == "NO":
    problemas3 = "no"
elif problemas3 == "SI":
    problemas3 = "si"
print("")
""" Fin cultivo número 3 """

# imprimir datos, mensaje final al usuario
print(" Consolidado final de los cultivos ")
print("")
print(f"La huerta {nom1} tiene {cantidad1} cultivos, durante {meses_cultivado1}  meses y {problemas1}  presenta problemas, actualmente.")
print("")
print(f"La huerta {nom2} tiene {cantidad2} cultivos, durante {meses_cultivado2}  meses y {problemas2}  presenta problemas, actualmente.")
print("")
print(f"La huerta {nom3} tiene {cantidad3} cultivos, durante {meses_cultivado3}  meses y {problemas3}  presenta problemas, actualmente.")

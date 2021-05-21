print("ingresa tu altura: ")
altura = input()
altura = float(altura)
print("ingresa tu peso: ")
peso = input()
peso = float(peso)

imc = peso /altura ** 2
if imc < 18.5:
    print("tiene que ir al medico por desnutrición")
elif imc >=18.5 and  imc< 24.9:
    print("esta bien de peso")
elif imc >= 25 and imc <= 29.9:
    print(" tiene sobrepeso")
else:
    print("debe ir al médico por obesidad")

print("Tu IMC es: ", imc)
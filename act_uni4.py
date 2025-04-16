# 1 programa que imprima todos los numeros enteros desde 0 hasta 100.
for i in range (0, 101):
 print(i)



# 2 programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene.
numero = int(input("Ingrese un número entero: "))
cant_digitos = len(str(abs(numero)))  # Se usa abs para ignorar el signo negativo
print("El número tiene ", cant_digitos, " digitos." )



# 3 programa que sume todos los numeros enteros entre dos valores dados por el usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

menor = min(num1, num2)
mayor = max(num1, num2)

suma = sum(range(menor + 1, mayor))
print("La suma de", menor, "y", mayor, "es:", suma)



# 4 programa que permita al usuario ingresar numeros enteros y los sume en secuencia. 
suma = 0
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)



# 5 juego en el que el usuario deba adivinar un nunmero aleatorio entre 0 y 9.
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")



# 6 programa que imprima en pantalla todos los nnmeros pares comprendidos entre 0 y 100,en orden decreciente.
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)



# 8 programa que calcule la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario.
limite = int(input("Ingrese un número entero positivo: "))

if limite < 0:
    print("El número debe ser positivo.")
else:
    suma = sum(range(limite + 1))  # Incluye el número ingresado
    print("La suma de los números desde 0 hasta", limite, "es:", suma)



# 9 programa que permita al usuario ingresar 100 numeros enteros y luego calcule la media de esos valores.
cantidad = 100  # Puedes cambiar este valor para hacer pruebas, por ejemplo: 10

suma = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad
print("La media de los números es:", media)



# 10 programa que invierta el orden de los digitos de un numero ingresado por el usuario.
numero = input("Ingrese un número entero: ")

if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]

print("Número invertido:", invertido)


# 7 programa que permita al usuario ingresar 100 numeros enteros.
cantidad = 100  # Cambia este valor a uno menor para pruebas, por ejemplo: 5

pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
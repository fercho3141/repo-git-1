print("1) Hola Mundo!")
imprimir_hola_mundo = "Hola Mundo!"
print(imprimir_hola_mundo)

print("---------------------------------------------------------------")

print("2) funcion saludar_usuario(nombre)")

def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

nombre = input("¿Cuál es tu nombre? ")
print(saludar_usuario(nombre))

print("---------------------------------------------------------------")

print("3) función informacion_personal(nombre, apellido,edad, residencia)")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Pedir datos al usuario
nombre = input("Ingresae su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("¿Dónde vives? ")

informacion_personal(nombre, apellido, edad, residencia)

print("---------------------------------------------------------------")

print("4) funciones: calcular_area_circulo(radio) y calcular_perimetro_circulo(radio)")

import math 

def calcular_area_circulo(radio):
 return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

print("---------------------------------------------------------------")

print("5) función segundos_a_horas(segundos)")

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

print("---------------------------------------------------------------")

print("6) función tabla_multiplicar(numero)")

def tabla_multiplicar(numero):
    print(f"Esta es la tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número: "))

tabla_multiplicar(numero)

print("---------------------------------------------------------------")

print("7) función operaciones_basicas(a, b)")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

print("---------------------------------------------------------------")

print("9) función celsius_a_fahrenheit(celsius)")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

print("---------------------------------------------------------------")

print("10) función calcular_promedio(a, b, c)")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio:.2f}")

print("---------------------------------------------------------------")

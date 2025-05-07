# imprimir_hola_mundo 
def imprimir_hola_mundo():
    """Imprime un saludo en pantalla."""
    print("Hola Mundo!")

imprimir_hola_mundo()



# saludar_usuario
def saludar_usuario(nombre):
    
    return f"Hola {nombre}! Buen día!"
# Solicita el nombre al usuario
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)



# informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Solicita los datos al usuario
nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
edad = input("¿Cuántos años tienes?: ")
residencia = input("¿Dónde vives?: ")

informacion_personal(nombre, apellido, edad, residencia)



# calcular_area_ciruclo 
import math  # Importa la librería para funciones matemáticas

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    #Devuelve el área de un círculo dado su radio
    return math.pi * radio ** 2

# Función para calcular el perímetro (circunferencia) del círculo
def calcular_perimetro_circulo(radio):
    #Devuelve el perímetro de un círculo dado su radio
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círuclo es de {area:.2f}")
print(f"El perímetro del círculo es de {perimetro:.2f}")



# segundos_horas
def segundos_a_horas(segundos):
    #Convierte segundos a horas
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")



# operaciones_basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"

    return (suma, resta, multiplicacion, division)


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(a, b)

print(f"Estos son los resultados de las operaciones:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")



# calcular_imc
# el IMC es una medida que relaciona el peso de una persona con su estatura
def calcular_imc(peso, altura):
    #Devuelve el IMC a partir del peso y la altura
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")



# celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    #Convierte grados Celsius a Fahrenheit 
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")



# calcular_promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio:.2f}")
# 1) Factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input("Ingrese un número entero positivo: "))

if numero < 1:
    print("ERROR. Ingrese un número mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

print("########################################")

# 2) Fibonacci

def fibonacci(x): 
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    
posicion = int(input("Ingrese la posición hasta la que deseas ver la serie: "))

if posicion < 0:
    print("ERROR. Introduce un número entero mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
    
print("########################################")


# 3) Potencia

def potencia(base, exponente):
    if exponente == 0:
        return 1 
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese una base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente < 0:
    print("ERROR. Ingrese un exponente mayor o igual a 0.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

print("########################################")

# 4) Decimal a Binario

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero: "))

if numero < 0:
    print("ERROR. Ingrese un número mayor o igual a 0.")
elif numero == 0:
    print("El número 0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

print("########################################")

# 5)

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo de uso
palabra = input("Ingrese una palabra: ").lower()

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
if palabra == "":
    print("ERROR. Ingrese una palabra.")
else:
    print(f"'{palabra}' no es un palíndromo.")

print("########################################")

# 6)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingreses un número entero positivo: "))

if numero < 0:
    print("ERROR. Ingrese un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

print("########################################")

# 7)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo: "))

if nivel_base < 1:
    print("ERROR. Ingrese un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Total de bloques necesarios: {total}")

print("########################################")

# 8)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("ERROR. Ingrese un número positivo entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")


#1) Programa que solicita la edad al usuario

#Solicita la edad al usuario 
edad = int(input("Ingrese su edad: "))

#Luego verifica si es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#2) Programa que solicita la nota del usuario

#Solicita la nota del usuario
nota = float(input("Ingrese su nota: "))

# Verifica si la nota es mayor, menor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Programa que permite ingresar números pares

#El programa pide un número para ver si es par, si es impar sigue pidiendo un número hasta que el usuario ponga un número par
#el break es para generar un bucle hasta que se ponga la información pedida

while True: 
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
        break 
else:
    print("Por favor, ingrese un número par")

#4) Progama que indica a que categoría de edad pertenece el usuario 


#Solicita al edad al usuario (otra vez)
edad2 = int(input('Ingrese su edad: '))

#Verifica la edad e indica en que rango de edad se encuentra el usuario 
if edad2 < 12:
    print("Eres un niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Eres un adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Eres un adulto/a joven")
else:
    print("Eres un/a adulto/a")

#5) Programa que permite introducir contraseñas de entre 8 y 14 caracteres

while True:
    contraseña = input("Por favor, ingresa una contraseña: ")

    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
        break
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Programa que hace algo? 

#No me molestaré en dejar una nota acá (no entiendo que hice o que hizo ChatGPT)

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Distribución con sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("Distribución con sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("Distribución sin sesgo.")
else:
    print("No se puede determinar un sesgo claro.")

#7)  Programa que solicita una frase o palabra al usuario y le pone un ! al final


#El programa pide una frase
#Si termina en aeiou le pone un ! al final
texto = input("Ingrese una frase o palabra: ")

#Esto sirve para que el programa verifique si la frase termina en aeiou
if texto[-1].lower() in 'aeiou':
    texto += "!"
print("Resultado:", texto)

#8)  Programa que solicita al usuario que ingrese su nombre y que indique como quiere que se escriba

nombre = input("Ingrese su nombre: ")

print("Elige una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción no válida."

print("Resultado:", resultado)

#9) Chile 

#El programa pide la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Clasifica según Dios, la magnitud y la escala Ritcher del terremoto en categorías 
if magnitud < 3:
    categoria = "Es muy leve y casi imperceptible"
elif magnitud < 4:
    categoria = "Es leve y ligeramente perceptible"
elif magnitud < 5:
    categoria = "Es moderado y puede ser sentido por personas, generealmente no causa daños"
elif magnitud < 6:
    categoria = "Es fuerte y puede causar daños en estructuras débiles"
elif magnitud < 7:
    categoria = "Es muy Fuerte  y puede causar daños significativos"
else:
    categoria = "Es extremo y puede causar graves daños a gran escala"

# Muestra el resultado :D
print("Clasificación:", categoria)

#10) Programa que pregunta al usuario en cuál hemisferio se encuentra e indica en que estación se encuentra 
#Es un montón, solo diré gracias ANGELINA SOLEDAD BRUZONI por haber pasado el código en el foro B)

hemiferio= input("Ingrese en que hemiferio se encuentra (N/S): ");
mes = int(input("Ingrese en que mes se encuentra (1/2/3/4/5/6/7/8/9/10): "));
dia= int(input("Ingrese el dia en que se encuentra: "));

if hemiferio == 'N' :
        
    if (mes==12 and 21<=dia<=31 )or (mes== 1 and (1<=dia<=31)) or ((mes== 2 and 1<=dia<=28) or (mes== 2 and 1<=dia<=29)) or (mes==3 and 1<=dia<=20) :
       
       print("Usted se encuentra en Invierno.");

    elif  (mes==3 and 21<=dia<=31 )or (mes== 4 and (1<=dia<=30)) or ((mes== 5 and 1<=dia<=31) or (mes== 6 and 1<=dia<=20)) :
        
        print("usted se encuentra en Primavera.");

    elif (mes==6 and 21<=dia<=30 )or (mes== 7 and (1<=dia<=31)) or ((mes== 8 and 1<=dia<=31) or (mes== 9 and 1<=dia<=20)) :
        
        print("Usted se encuentra en Verano.");
    
    else:
       
       print("Usted se encuentra en Otoño."); 

else:
     
    if (mes==12 and 21<=dia<=31 )or (mes== 1 and (1<=dia<=31)) or ((mes== 2 and 1<=dia<=28) or (mes== 2 and 1<=dia<=29)) or (mes==3 and 1<=dia<=20) :
       
       print("Usted se encuentra en Verano.");
    
    elif (mes==3 and 21<=dia<=31 )or (mes== 4 and (1<=dia<=30)) or ((mes== 5 and 1<=dia<=31) or (mes== 6 and 1<=dia<=20)) :
        
        print("Usted se encuentra en Otoño.");

    elif (mes==6 and 21<=dia<=30 )or (mes== 7 and (1<=dia<=31)) or ((mes== 8 and 1<=dia<=31) or (mes== 9 and 1<=dia<=20)) :
        
        print("Usted se encuentra en Invierno.");
    
    else:
       print("Usted se encuentra en Primavera."); 
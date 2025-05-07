print("1) Crear una lista con los numeros del 1 al 100 que sean multiplos de 4")

multiplos = list(range(4, 101, 4))

print(multiplos)
print("---------------------------------------------------------------")

print("2) Crear una lista con cinco elementos y mostrar el penúltimo")

lista_cinco = ["Messi", 10, "River", "Minecraft", 2018]
posicion_lista = lista_cinco [3]

print(posicion_lista)
print(type(posicion_lista))
print("---------------------------------------------------------------")

print("3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista")

num = []

num.append("hola")
num.append("como")
num.append("estas")

print(num)

print("---------------------------------------------------------------")

print("4) Reemplazar el segundo y último valor de la lista “animales”")

lista_animales = ["perro", "gato", "conejo", "pez"]

lista_animales[1] = "loro"
lista_animales[3] = "oso"

print(lista_animales)

print("---------------------------------------------------------------")

print("5) Analizar el siguiente programa y explicar")

print("Este programa lo que hace es remover el número más alto de la lista. Con la función max encuentra el valor más alto, el cual es 22, y luego imprime la lista sin ese valor")

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

print("---------------------------------------------------------------")

print("6) Crear una lista con números del 10 al 30")

Barsa_al_PSG = list(range(10, 31, 5))
print(Barsa_al_PSG)
print(Barsa_al_PSG[:2])

print("---------------------------------------------------------------")

print("7) Reemplazar los dos valores centrales")

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "tesla"
autos[2] = "lamgorgini"

print(autos)

print("---------------------------------------------------------------")

print("8) Crear una lista vacía llamada dobles y agregar el doble de 5, 10 y 15")

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print("---------------------------------------------------------------")

print("9) compras")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print("---------------------------------------------------------------")

print("10 Elaborar una lista anidada")

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)

print("---------------------------------------------------------------")




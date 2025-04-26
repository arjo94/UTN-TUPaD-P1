# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else: 
    print("No eres mayor de edad")

# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota=float(input("ingrese su nota: "))
if nota >= 6 and nota <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero=int(input("ingrese su numero por favor: "))
if numero % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("no es un numero par")

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad=int(input("ingrese su edad: "))
if edad >= 30:
    print("Adulto/a")
elif edad >= 18 and edad < 30:
    print("Adulto/a")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad < 12:
    print("Niño/a")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje
#  "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
#  que tiene un iterable tal como una lista o un string.

#Solicitar a un usuario la contraseña
contraseña=input("ingrese su contraseña: ")
#Verificar si la longitud esta entre los 8 y 14 caracteres
if 8 <= len(contraseña) <= 14:
    print("ha ingresado un contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
# negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean, StatisticsError

# Generar lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

# Calcular la moda, controlando si hay más de una
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "No única"

# Mostrar los resultados
print("Lista de números aleatorios:")
print(numeros_aleatorios)
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el sesgo
if isinstance(moda, str):
    print("\nNo se puede determinar el sesgo porque no hay una moda única.")
else:
    if media > mediana > moda:
        print("\nDistribución con sesgo positivo (a la derecha).")
    elif media < mediana < moda:
        print("\nDistribución con sesgo negativo (a la izquierda).")
    elif media == mediana == moda:
        print("\nDistribución sin sesgo.")
    else:
        print("\nNo se puede determinar un sesgo claro con estos valores.")

# Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación 
# al final e imprimir el string resultante por pantalla; en caso contrario,
#  dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicitar una frase o palabra al usuario
texto = input("Ingresá una frase o palabra: ")

# Verificar si termina en vocal (minúscula o mayúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"
    
# Imprimir el resultado
print("Resultado:", texto)

# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitar el nombre del usuario
nombre = input("Ingresá tu nombre: ")

# Mostrar opciones
print("Elige una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la Primera Letra en mayúscula")

# Solicitar la opción al usuario
opcion = input("Ingresá 1, 2 o 3 según tu elección: ")

# Procesar según la opción
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida.")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, pri
#mavera o verano.

# Pedir datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Función para determinar estación
def obtener_estacion(mes, dia, hemisferio):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        return "Fecha inválida"

    return estacion_norte if hemisferio == "N" else estacion_sur

# Calcular estación
estacion = obtener_estacion(mes, dia, hemisferio)

# Mostrar resultado
print(f"Estás en {estacion}.")









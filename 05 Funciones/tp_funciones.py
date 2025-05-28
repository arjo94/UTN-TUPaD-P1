#1 Crear una función llamada imprimir_hola_mundo que imprima por 
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal
#Definicion de Funciones    
def Imprimir_hola_mundo():
    print("Hola Mundo!") 

#Programa Principal
Imprimir_hola_mundo()

#2 Crear una función llamada saludar_usuario(nombre) que reciba 
# como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: 
# “Hola Marcos!”. Llamar a esta función desde el programa 
# principal solicitando el nombre al usuario.
#Definicion de Funciones 
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#3 Crear una función llamada informacion_personal(nombre, apellido, 
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy 
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir 
# los datos al usuario y llamar a esta función con los valores ingresados.

#Definicion de funciones     
def informacion_personal(nombre,apellido,edad,residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} "

#Programa principal
nombre=input("ingrese su nombre ")
apellido=input("ingrese su apellido ")
edad=input("ingrese su edad ")
residencia=input("ingrese su residencia ")
presentacion=informacion_personal(nombre,apellido,edad,residencia)
print(presentacion)


#4 Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados
import math
#Definicion de Funciones
def calcular_area_circulo(radio):
    return   math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
    return    2*math.pi*radio

#Programa Principal
radio=float(input("ingrese el radio"))
mostrar_resultados=calcular_area_circulo(radio)
mostrar_resultados2=calcular_perimetro_circulo(radio)
                                        
print(f"el area del circulo es: ",mostrar_resultados)
print(f"el perimetro del circulo es: ",mostrar_resultados2)

#5 Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

#Definicion de Funciones
def segundos_a_horas(segundos):
    return segundos/3600

#Programa principal
segundos=float(input("ingrese los segundos: "))
resultados=segundos_a_horas(segundos)
print(f"los segundos equivalen a {resultados} horas")

#6 Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Definicion de Funciones
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
numero_usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)

#7 Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

#Definicion de Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultado = operaciones_basicas(a, b)

print("\nResultados de las operaciones:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")

#8 Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

#Definicion de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#Definicion de funciones
def celsius_a_fahrenheit(celisius):
    return 9/5 * grados + 32

#Programa principal
grados=float(input("ingrese la temperatura en celsius: "))
conversion=celsius_a_fahrenheit(grados)
print(f"la temperatuta en fahrenheit es: {conversion} ")

#10 Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

#Definicion de Funciones
def calcular_promedio(a,b,c):
    return (a + b + c)/3


#Programa principal
a=float(input("ingrese su primer numero: "))
b=float(input("ingrese su segundo numero: "))
c=float(input("ingrese su tercer numero: "))
resultado=calcular_promedio(a,b,c)
print(f"el promedio es: {resultado}")
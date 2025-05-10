#1) Crea un programa que imprima en pantalla todos los números enteros 
# desde 0 hasta 100
#(incluyendo ambos extremos),
#  en orden creciente, 
# ostrando un número por línea.

#Utilizo for ya que tengo la cantidad solicitada
for i in range(0,101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
#Solicito al usuario un numero
num=int(input("ingrese un numero: "))
#Convierte los numeros negativos en positivos
num=abs(num)
#Inicializa el contador en 0
cont=0
#Verifico si el numero es mayor o igual 0
if num == 0:
    cont = 1
else:
    while num > 0:
        num = num // 10
        cont += 1
print(f"el numero tiene: {cont} digitos")


#3) Escribe un programa que sume todos los números enteros comprendidos
#  entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Solicito a el usuario 2 numeros"
num1=int(input("ingrese su primer numero: "))
num2=int(input("ingrese su segundo numero: "))

if num1 > num2:
    num1,num2 = num2,num1
#inicializo el contador
sumatoria=0
for i in range(num1+1,num2):
    sumatoria += i
print(f"la suma entre el primer numero y el segundo numero es: ",sumatoria)

#4) Elabora un programa que permita al usuario ingresar números enteros 
# y los sume en secuencia. El programa debe detenerse y
#  mostrar el total acumulado cuando el usuario ingrese un 0.
num=int(input("ingrese su numero(ingrese 0 para detener): "))
acu=0
while num != 0:
    acu += num
    num=int(input("ingrese otro numero(ingrese 0 para detener): "))
print("la suma total es: ",acu)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio
#  entre 0 y 9. Al final, el programa debe mostrar cuántos intentos
#  fueron necesarios para acertar el número.

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto!")
        adivinado = True
    else:
        print("Incorrecto, intenta de nuevo.")

print(f"Lo lograste en {intentos} intento(s).")

#6) Desarrolla un programa que imprima en pantalla todos
#  los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,0,-2):
     print(i)

#7) Crea un programa que calcule la suma de todos
#  los números comprendidos entre 0 y un número entero positivo
#  indicado por el usuario.

#Solicito numero positivo al usuario"
numer=int(input("ingrese su numero: "))
#Inicializo el acumulador"
sumatoria=0
#Inicializo el ciclo"
if numer < 0:
    print("ingrese un numero positivo")
elif numer != 0:
    for i in range(0,numer):
        sumatoria += i
print(f"la suma total es: ",sumatoria)

#8) Escribe un programa que permita al usuario ingresar 100 números
#  enteros. Luego, el programa debe indicar cuántos de estos números
#  son pares, cuántos son impares, cuántos son negativos y cuántos son
#  positivos. (Nota: para probar el programa puedes usar una cantidad
#  menor, pero debe estar preparado para procesar 100 números con
#  un solo cambio).


# Puedes cambiar este valor para pruebas más rápidas
cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números
#  enteros y luego calcule la media de esos valores.
#  (Nota: puedes probar el programa con una cantidad menor, pero debe
#  poder procesar 100 números cambiando solo un valor).

#Puedes cambiar este valor 
cantidad_numeros = 100
suma = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de
#  un número ingresado por el usuario. Ejemplo: si el usuario
#  ingresa 547, el programa debe mostrar 745.

n=int(input("ingrese un numero: "))
numero_negativo = n < 0
n=abs(n)
# Invertimos el número
digitos=0
inver=0
while n != 0:
    digitos=n % 10
    inver=inver * 10 + digitos
    n = n // 10
if numero_negativo:
    inver = -inver

print(f"Número invertido: {inver}")
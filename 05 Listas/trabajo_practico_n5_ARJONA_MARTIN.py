#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
lista=list(range(4,101,4))
print(lista)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
#  ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
lista1=[2,3,5,6,10]
print(f"la penultima posicion es:  {lista1[-2]}")

#3) Crear una lista vacía, agregar tres palabras con append e
#  imprimir la lista resultante por pantalla.
#  Pista: para crear una lista vacía debes colocar los corchetes
#  sin nada en su interior. Por ejemplo:

lista2=[]
lista2.append("maquina")
lista2.append("auto")
lista2.append("iphone")
print(f"lista: ",lista2)

#4) Reemplazar el segundo y último valor de la lista “animales”
#  con las palabras “loro” y “oso”, respectivamente.
#  Imprimir la lista resultante por pantalla.
#  ¡Puedes hacerlo como se muestra en los videos o bien investigar
#  cómo funciona el indexing con números negativos! animales
#  = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[3]="oso"
print(animales)

#5) Analizar el siguiente programa y
#  explicar con tus palabras qué es lo que realiza.

#el programa del ejercicio elimina o remueve el
#  numero maximo de la lista que es en este caso el numero 22

#6) Crear una lista con números del 10 al 30 (incluído),
#  haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros

lista4=list(range(10,31,5))
print(lista4)

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista
#  “autos” por dos nuevos valores cualesquiera

autos=["sedan","polo","suran","gol"]
autos[1]="nivus"
autos[2]="corolla"
print(autos)

#8) Crear una lista vacía llamada "dobles" y
#  agregar el doble de 5, 10 y 15 usando append directamente.
#  Imprimir la lista resultante por pantalla.
#creo lista vacia
dobles=[]
# Agrego el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los
#  productos comprados por diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo
#  cliente. 
# c) Eliminar "pan" de la lista del primer cliente. 
# d) Imprimir la lista resultante por pantalla

# Lista original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente (índice 1)
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

# c) Eliminar "pan" del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que
#  contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.

# Crear la lista anidada con los valores indicados
lista_anidada = [
    15,                     # lista_anidada[0]
    True,                  # lista_anidada[1]
    [25.5, 57.9, 30.6],    # lista_anidada[2][0], [2][1], [2][2]
    False                  # lista_anidada[3]
]

# Imprimir la lista resultante
print(lista_anidada)
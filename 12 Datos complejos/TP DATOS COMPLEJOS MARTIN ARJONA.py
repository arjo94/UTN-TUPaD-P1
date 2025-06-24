#1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas['Naranja']= 1200
precios_frutas['Manzana']= 1200
precios_frutas['Pera']= 1200

# print(precios_frutas) ya se actualizo el diccionario y por ese motivo se retiro el print

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#  actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

#print(precios_frutas) se realizo el siguiente ejercicio y por ese motivo se retiro el print

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#  crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas.keys()
print(precios_frutas.keys())

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.


print("Bienvenido a su almacen de contactos")
#Primer contacto
nombre1=input("ingrese su primer contacto: ")
clave1=int(input("ingrese la clave del primer contacto: "))
#Segundo contacto
nombre2=input("ingrese su segundo contacto: ")
clave2=int(input("ingrese la clave del segundo contacto: "))
#Tercer contacto
nombre3=input("ingrese su tercer contacto: ")
clave3=int(input("ingrese la clave del tercer contacto: "))
#Cuarto contacto
nombre4=input("ingrese su cuarto contacto: ")
clave4=int(input("ingrese la clave del cuarto contacto: "))
#Quinto contacto
nombre5=input("ingrese su quinto contacto: ")
clave5=int(input("ingrese la clave del quinto contacto: "))

contactos={nombre1:clave1,nombre2:clave2,nombre3:clave3,nombre4:clave4,nombre5:clave5}

consulta=(input("ingrese el contacto deseado: "))

if consulta in contactos:
    print("El número es:", contactos[consulta])
else:
    print("Ese contacto no existe.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.split()

# Palabras únicas
unicas = set(palabras)
print("Palabras únicas:", unicas)

# Contador de palabras
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(conteo)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#  Luego, mostrá el promedio de cada alumno.

# Alumno 1
nombre1 = input("Nombre del primer alumno: ")
nota1_1 = float(input("Nota 1: "))
nota1_2 = float(input("Nota 2: "))
nota1_3 = float(input("Nota 3: "))
promedio1 = (nota1_1 + nota1_2 + nota1_3) / 3
print(f"{nombre1} tiene las notas {nota1_1}, {nota1_2}, {nota1_3} y un promedio de {round(promedio1, 2)}")

# Alumno 2
nombre2 = input("\nNombre del segundo alumno: ")
nota2_1 = float(input("Nota 1: "))
nota2_2 = float(input("Nota 2: "))
nota2_3 = float(input("Nota 3: "))
promedio2 = (nota2_1 + nota2_2 + nota2_3) / 3
print(f"{nombre2} tiene las notas {nota2_1}, {nota2_2}, {nota2_3} y un promedio de {round(promedio2, 2)}")

# Alumno 3
nombre3 = input("\nNombre del tercer alumno: ")
nota3_1 = float(input("Nota 1: "))
nota3_2 = float(input("Nota 2: "))
nota3_3 = float(input("Nota 3: "))
promedio3 = (nota3_1 + nota3_2 + nota3_3) / 3
print(f"{nombre3} tiene las notas {nota3_1}, {nota3_2}, {nota3_3} y un promedio de {round(promedio3, 2)}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# sets con alumnos que aprobaron cada parcial
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

# 1. Alumnos que aprobaron ambos parciales (intersección)
ambos = parcial1.intersection(parcial2)
print("Alumnos que aprobaron ambos parciales:", ambos)

# 2. Alumnos que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1.symmetric_difference(parcial2)
print("Alumnos que aprobaron solo uno de los dos parciales:", solo_uno)

# 3. Alumnos que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1.union(parcial2)
print("Alumnos que aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos = {}

accion = ""

while accion != "salir":
    accion = input("¿Qué querés hacer? (consultar/agregar/salir): ").lower()

    if accion == "consultar":
        producto = input("Ingresá el nombre del producto: ")
        if producto in productos:
            print(f"El stock de {producto} es {productos[producto]}")
        else:
            print(f"{producto} no está en el sistema.")

    elif accion == "agregar":
        producto = input("Ingresá el nombre del producto: ")
        cantidad = int(input("Ingresá la cantidad a agregar: "))
        if producto in productos:
            productos[producto] += cantidad
        else:
            productos[producto] = cantidad
        print(f"Stock actualizado: {producto} = {productos[producto]}")

    elif accion == "salir":
        print("¡Adiós!")

    else:
        print("Acción no válida, intentá de nuevo.")

#9)Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

# Creo la agenda con algunos eventos
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de matemáticas",
    ("miércoles", "09:00"): "Consulta médica",
}
# Pedir día y hora para consultar
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (ej: 10:00): ")

# Buscar evento 
clave = (dia, hora)
if clave in agenda:
    print(f"El evento para {dia} a las {hora} es: {agenda[clave]}")
else:
    print(f"No hay eventos para {dia} a las {hora}.")


#10) Dado un diccionario que mapea nombres de países con sus capitales,
#  construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales = {}
for pais in paises:
    capitales[paises[pais]] = pais

print(capitales)
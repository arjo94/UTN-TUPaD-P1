# Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla 
# el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Función recursiva que calcula el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Pedimos un número al usuario
num = int(input("Ingrese un número entero positivo: "))

# Calculamos y mostramos el factorial de todos los números desde 1 hasta num
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    # Caso base: si n es 0 o 1, devuelve n
    if n == 0 or n == 1:
        return n
    # Llamada recursiva: suma de los dos valores anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario hasta qué posición quiere la serie
pos = int(input("Ingrese la posición hasta la que quiere la serie Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()

# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * base^(exponente-1)
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")

# Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    # Caso base: si n es 0, devolvemos cadena vacía (para construir desde el último bit)
    if n == 0:
        return ""
    else:
        # Dividimos n entre 2 y guardamos el resto, luego concatenamos recursivamente
        return decimal_a_binario(n // 2) + str(n % 2)

# Función para manejar el caso cuando el número es 0 (porque la función devuelve "")
def convertir(n):
    if n == 0:
        return "0"
    else:
        return decimal_a_binario(n)

numero = int(input("Ingrese un número entero positivo: "))
binario = convertir(numero)
print(f"El número {numero} en binario es: {binario}")

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena 
# de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Pedir al usuario que ingrese una palabra sin espacios ni tildes
entrada = input("Ingrese una palabra sin espacios ni tildes: ").lower()

if es_palindromo(entrada):
    print(f"La palabra '{entrada}' es un palíndromo.")
else:
    print(f"La palabra '{entrada}' NO es un palíndromo.")

# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero 
# positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Pedimos al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validamos que sea positivo
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.

def contar_bloques(n):
    # Caso base: si n es 1, solo hay un bloque
    if n == 1:
        return 1
    else:
        # Suma el nivel actual (n) más la suma recursiva de los niveles restantes (n-1)
        return n + contar_bloques(n - 1)

print(contar_bloques(1))  # Output: 1
print(contar_bloques(2))  # Output: 3
print(contar_bloques(4))  # Output: 10

# Para que el usuario pueda ingresar un número y ver el resultado:
n = int(input("Ingrese el número de bloques del nivel más bajo: "))
if n <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    total = contar_bloques(n)
    print(f"Total de bloques para la pirámide: {total}")

# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero 
# positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no quedan dígitos por contar
    if numero == 0:
        return 0
    else:
        # Contamos 1 si el último dígito es igual al digito buscado, sino 0
        cuenta = 1 if (numero % 10) == digito else 0
        # Llamada recursiva con el número sin el último dígito
        return cuenta + contar_digito(numero // 10, digito)

# Para que el usuario ingrese los datos
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9) a contar: "))

if 0 <= digito <= 9 and numero >= 0:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
else:
    print("Por favor, ingrese un número positivo y un dígito válido entre 0 y 9.")
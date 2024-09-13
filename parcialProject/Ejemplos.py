#convertir entero a decimal
int_num = 10
decimal_num = float(int_num)
print(decimal_num)

# Convertir decimal a entero
Valor = 4.31
integer = int(Valor)
print(integer)

# Convertir cadena a entero
string = "7"
Valor = int(string)
print(Valor)

# Convertir cadena a decimal
string = "5.12"
decimal = float(string)
print(decimal)

# Convertir entero a cadena
Valor = 9
string = str(Valor)
print(string)

# Convertir decimal a cadena
decimal = 4.13
string = str(decimal)
print(string)

#Multilíneas de cadenas.
name = "John"
multiline_string = f"This is a multiline string\nthat spans across multiple lines.\nHello, {name}!"
print(multiline_string)

#Función len().
my_string = "Hello, World!"
print(len(my_string))

#Sub cadenas:
def obtener_subcadena(cadena, inicio, fin):
  """
  Obtiene una subcadena de una cadena dada.

  Args:
    cadena: La cadena de la que se extraerá la subcadena.
    inicio: El índice inicial de la subcadena (incluido).
    fin: El índice final de la subcadena (excluido).

  Returns:
    La subcadena extraída.
  """
  return cadena[inicio:fin]

# Ejemplo de uso
cadena = "Esta es una cadena de ejemplo."
subcadena_inicio = obtener_subcadena(cadena, 0, 5)
subcadena_medio = obtener_subcadena(cadena, 5, 15)
subcadena_final = obtener_subcadena(cadena, 15, len(cadena))

print(f"Subcadena inicial: {subcadena_inicio}")
print(f"Subcadena del medio: {subcadena_medio}")
print(f"Subcadena final: {subcadena_final}")

#Función upper().
my_string = "hello world"
print(my_string.upper())  # Output: "HELLO WORLD"

#Función lower()
# Ejemplo de uso de la función lower() en Python

# Ingreso de datos por el usuario
cadena = input("Ingrese una cadena de texto: ")

# Convertir la cadena a minúsculas
cadena_minusculas = cadena.lower()

# Mostrar el resultado
print("La cadena en minúsculas es:", cadena_minusculas)

# Multilíneas de cadenas de caracteres.
cadena_multilinea = """Esta es una cadena multilínea.
Se puede extender a varias líneas."""
print(cadena_multilinea)

# Función strip()
cadena_con_espacios = "  Hola Mundo  "
cadena_sin_espacios = cadena_con_espacios.strip()
print(cadena_sin_espacios)

# Función replace()
cadena_original = "Hola Mundo"
cadena_reemplazada = cadena_original.replace("Mundo", "Python")
print(cadena_reemplazada)

# Función split()
cadena_separada = "Hola,Mundo"
lista_palabras = cadena_separada.split(",")
print(lista_palabras)

# Formato de cadenas F-String.
nombre = "Juan"
edad = 30
mensaje = f"Hola {nombre}, tienes {edad} años."
print(mensaje)

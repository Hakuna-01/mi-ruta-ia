# ¿Qué es una función?
# Una función es un bloque de código con nombre que puedes reutilizar. En lugar de repetir el mismo código 10 veces, lo escribes una vez dentro de una función y lo llamas cuando lo necesitas.
# Sin función — código repetido (malo)
print("Hola, David")
print("Hola, Maria")
print("Hola, Carlos")

# Con función — código reutilizable (bueno)
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("David")
saludar("Maria")
saludar("Carlos")


# return — devolver un resultado
# return hace que la función devuelva un valor que puedes guardar o usar. Sin return, la función hace algo pero no entrega nada.
# Función que devuelve un valor
def sumar(a, b):
    resultado = a + b
    return resultado

# Guardamos lo que devuelve
total = sumar(10, 5)
print(total)               # 15
print(sumar(100, 200))   # 300

# Función sin return — solo ejecuta, no devuelve
def mostrar_bienvenida():
    print("Bienvenido al sistema")

resultado = mostrar_bienvenida()
print(resultado)   # None — no devuelve nada

#Parámetros por defecto y argumentos con nombre
#Puedes definir valores por defecto para los parámetros. Si no se pasa ese argumento, usa el valor por defecto. Esto hace tus funciones mucho más flexibles.

# Parámetro con valor por defecto
def crear_usuario(nombre, rol="cliente", activo=True):
    return {
        "nombre": nombre,
        "rol": rol,
        "activo": activo
    }

# Usando solo el parámetro obligatorio
user1 = crear_usuario("David")
print(user1)

# Pasando argumentos con nombre (keyword arguments)
user2 = crear_usuario("Maria", rol="admin")
print(user2)

# Pasando todos los argumentos
user3 = crear_usuario("Carlos", rol="editor", activo=False)
print(user3)
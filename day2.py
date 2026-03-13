nombre = "David"
edad = 28
altura = 1,75
es_estudiante = True

#print () muestra el valor en pantalla
print(nombre)
print(edad)
print(es_estudiante)

#Los 4 tipos básicos que más usarás
#Python tiene varios tipos de datos. Estos 4 los usarás en el 90% de tu código.

# int - numeros enteros
edad = 28
precion = 1500

# float - numeros con decimales
temperatura = 36.5
pi = 3.14159

# str - texto (siempre siempre entre comillas)
nombre = "David Quintana"
ciudad = 'Caracas'

# bool - verdadero o falso

activo = True
apagado = False

# type() te dice el tipo de cualquier variable
print(type(edad))
print(type(nombre))
print(type(activo))

nombre = "David"
edad = 28
print(f"Hola, soy {nombre} y tengo {edad} años")

a = 10
b = 3

print(a + b)    # 13   suma
print(a - b)    # 7    resta
print(a * b)    # 30   multiplicacion
print(a / b)    # 3.333... division normal
print(a // b)   # 3     dicision entera (sin decimales)
print(a ** b)   # 1000  potencia

#Operadores de comparación
#Comparan dos valores y devuelven True o False. Son la base de todos los if que escribirás.

edad = 20

print(edad == 20)   # True  -   igual a
print(edad != 18)   # True  → distinto de
print(edad > 18)    # True  → mayor que
print(edad < 18)    # False → menor que
print(edad >= 20)   # True  → mayor o igual
print(edad <= 15)   # False → menor o igual

#Listas — colecciones ordenadas
#Una lista guarda varios valores en orden. Se crea con corchetes []. Es el tipo de dato más usado en Python.

#Crear una lista

habilidades = ["Python", "FastAPI", "Git"]

# Acceder por indice (empieza en 0)

print(habilidades[0])   #   Python
print(habilidades[1])   #   FastAPI
print(habilidades[-1])  #   Git (ultimo elemento)

# Agregar elementos

habilidades.append("Docker")
print(habilidades)

# Longitud de la lista

print(len(habilidades)) #   4

# Recorrer la lista

for skill in habilidades:
    print(f"Se usar: {skill}")

#Diccionarios — datos con nombre
#Un diccionario guarda pares clave:valor. Es como un formulario. En FastAPI, cada petición y respuesta es básicamente un diccionario.

#Crear un diccionario

usuario = {
    "nombre": "David",
    "edad": 28,
    "activo": True,
    "habilidades": ["Python", "FastAPI"]
}

# Acceder por clave

print(usuario["nombre"])        # David
print(usuario["habilidades"])   # ["Python", "FastAPI"]

# Agregar o modificar

usuario["ciudad"] = "Caracas"
usuario["edad"] = 29

# Ver todas las claves y valores

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")


mi_perfil = {
    "nombre": "David Quintana",
    "edad": 30,
    "ciudad": "Valencia",
    "habilidades": ["analisis de datos", "pensamiento logico", "matematicas", "tecnologia"],
    "disponible_freelance": True
}

print(f"Mi nombre es {mi_perfil['nombre']} y vivo en {mi_perfil['ciudad']}")
print(f"Tengo {mi_perfil['edad']} años")
print(f"Disponible para freelance: {mi_perfil['disponible_freelance']}")
print("Mis habilidades:")
for habilidad in mi_perfil["habilidades"]:
    print(f"  - {habilidad}")
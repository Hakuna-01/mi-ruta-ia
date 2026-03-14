#Slicing — cortar listas
#El slicing te permite extraer partes de una lista usando la sintaxis [inicio:fin:paso]. Es una de las herramientas más poderosas de Python.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])    # [2, 3, 4]       del índice 2 al 4
print(numeros[:4])     # [0, 1, 2, 3]    desde el inicio hasta el 3
print(numeros[6:])     # [6, 7, 8, 9]    desde el 6 hasta el final
print(numeros[::-1])   # [9,8,7,6,5,4,3,2,1,0] lista al revés
print(numeros[::2])    # [0, 2, 4, 6, 8] cada 2 elementos

# Métodos esenciales de listas
# Los métodos que más usarás en proyectos reales y en APIs.
frutas = ["mango", "pera", "uva", "pera"]

# Buscar y contar
print("pera" in frutas)        # True
print(frutas.index("uva"))      # 2
print(frutas.count("pera"))     # 2

# Modificar
frutas.insert(1, "kiwi")        # inserta en posición 1
frutas.remove("pera")           # elimina la primera "pera"
ultimo = frutas.pop()             # elimina y devuelve el último

# Ordenar
numeros = [5, 2, 8, 1, 9]
numeros.sort()                    # ordena en su lugar
ordenados = sorted(numeros, reverse=True)  # devuelve nueva lista
print(ordenados)                  # [9, 8, 5, 2, 1]


#List comprehensions — la forma Pythónica
#Las list comprehensions crean listas nuevas en una sola línea. Son más rápidas y más elegantes que un for loop tradicional. Las verás en todo código Python profesional.
# Forma tradicional — 4 líneas
cuadrados = []
for n in range(1, 6):
    cuadrados.append(n ** 2)
print(cuadrados)   # [1, 4, 9, 16, 25]

# List comprehension — 1 línea, mismo resultado
cuadrados = [n ** 2 for n in range(1, 6)]
print(cuadrados)   # [1, 4, 9, 16, 25]

# Con condición — solo los pares
pares = [n for n in range(1, 11) if n % 2 == 0]
print(pares)   # [2, 4, 6, 8, 10]

# Transformar strings
nombres = ["david", "maria", "carlos"]
mayusculas = [n.upper() for n in nombres]
print(mayusculas)  # ['DAVID', 'MARIA', 'CARLOS']

# Dict comprehensions
# Lo mismo pero para crear diccionarios. Muy útil para transformar datos en APIs.
# Crear diccionario desde una lista
productos = ["laptop", "mouse", "teclado"]
precios = {producto: 0.0 for producto in productos}
print(precios)
# {'laptop': 0.0, 'mouse': 0.0, 'teclado': 0.0}

# Invertir un diccionario (claves ↔ valores)
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(invertido)   # {1: 'a', 2: 'b', 3: 'c'}

# Métodos avanzados de diccionarios
# Más allá de acceder por clave, los diccionarios tienen métodos poderosos para manejar datos que usarás constantemente en APIs.
usuario = {
    "nombre": "David",
    "edad": 30,
    "ciudad": "Valencia"
}

# get() — acceso seguro sin KeyError
print(usuario.get("nombre"))          # David
print(usuario.get("email"))           # None (no lanza error)
print(usuario.get("email", "N/A"))   # N/A (valor por defecto)

# update() — fusionar diccionarios
datos_nuevos = {"email": "david@gmail.com", "edad": 31}
usuario.update(datos_nuevos)
print(usuario)

# pop() — eliminar y obtener valor
ciudad = usuario.pop("ciudad")
print(ciudad)    # Valencia
print(usuario)   # ya no tiene "ciudad"

# keys(), values(), items()
print(list(usuario.keys()))    # ['nombre', 'edad', 'email']
print(list(usuario.values()))  # ['David', 31, 'david@gmail.com']

# Diccionarios anidados — la estructura de las APIs
# Las respuestas de APIs reales son diccionarios dentro de diccionarios. Necesitas saber navegarlos.
respuesta_api = {
    "status": "ok",
    "data": {
        "usuario": {
            "id": 1,
            "nombre": "David",
            "habilidades": ["Python", "FastAPI"]
        }
    }
}

# Navegar la estructura anidada
nombre = respuesta_api["data"]["usuario"]["nombre"]
primera_habilidad = respuesta_api["data"]["usuario"]["habilidades"][0]

print(nombre)             # David
print(primera_habilidad)  # Python


# 1. Crear lista de al menos 5 usuarios
usuarios = [
    {
        "id": 1,
        "nombre": "Ana García",
        "edad": 28,
        "activo": True,
        "habilidades": ["Python", "JavaScript", "SQL"]
    },
    {
        "id": 2,
        "nombre": "Carlos López",
        "edad": 35,
        "activo": False,
        "habilidades": ["Java", "Spring", "MySQL"]
    },
    {
        "id": 3,
        "nombre": "María Rodríguez",
        "edad": 42,
        "activo": True,
        "habilidades": ["Python", "Django", "PostgreSQL", "AWS"]
    },
    {
        "id": 4,
        "nombre": "Juan Martínez",
        "edad": 31,
        "activo": True,
        "habilidades": ["React", "JavaScript", "CSS", "HTML"]
    },
    {
        "id": 5,
        "nombre": "Laura Sánchez",
        "edad": 29,
        "activo": False,
        "habilidades": ["Python", "Flask", "MongoDB"]
    }
]

# Función 1: Obtener usuarios activos
def obtener_activos(usuarios):
    """Devuelve lista de usuarios donde activo es True usando list comprehension"""
    return [usuario for usuario in usuarios if usuario["activo"]]

# Función 2: Buscar usuario por ID
def buscar_por_id(usuarios, id):
    """Devuelve el usuario con ese id o None si no existe"""
    # Versión 1: Usando next() con generator expression (más eficiente)
    return next((usuario for usuario in usuarios if usuario["id"] == id), None)
    
    # Versión alternativa con get() de forma segura:
    # for usuario in usuarios:
    #     if usuario.get("id") == id:
    #         return usuario
    # return None

# Función 3: Agregar habilidad a un usuario
def agregar_habilidad(usuarios, id, habilidad):
    """Agrega una habilidad al usuario con ese id. Si ya la tiene, no la agrega de nuevo"""
    usuario = buscar_por_id(usuarios, id)
    
    if usuario:
        if habilidad not in usuario["habilidades"]:
            usuario["habilidades"].append(habilidad)
            return f"Habilidad '{habilidad}' agregada a {usuario['nombre']}"
        else:
            return f"El usuario {usuario['nombre']} ya tiene la habilidad '{habilidad}'"
    else:
        return f"No se encontró usuario con id {id}"

# Función 4: Resumen de usuarios
def resumen_usuarios(usuarios):
    """Devuelve un diccionario con total, activos y habilidad más común"""
    total = len(usuarios)
    activos = len(obtener_activos(usuarios))
    
    # Obtener todas las habilidades usando list comprehension anidada
    todas_habilidades = [habilidad for usuario in usuarios for habilidad in usuario["habilidades"]]
    
    # Encontrar la habilidad más común
    if todas_habilidades:  # Verificar que no esté vacía
        habilidad_comun = max(set(todas_habilidades), key=todas_habilidades.count)
    else:
        habilidad_comun = None
    
    return {
        "total_usuarios": total,
        "usuarios_activos": activos,
        "habilidad_mas_comun": habilidad_comun
    }

# ===== PRUEBAS =====
print("=== SISTEMA DE GESTIÓN DE USUARIOS ===\n")

# Probar obtener_activos
print("1. Usuarios activos:")
activos = obtener_activos(usuarios)
for usuario in activos:
    print(f"   - {usuario['nombre']} (ID: {usuario['id']})")
print()

# Probar buscar_por_id
print("2. Búsqueda por ID:")
usuario = buscar_por_id(usuarios, 3)
print(f"   Buscando ID 3: {usuario['nombre'] if usuario else 'No encontrado'}")
usuario = buscar_por_id(usuarios, 10)
print(f"   Buscando ID 10: {usuario['nombre'] if usuario else 'No encontrado'}")
print()

# Probar agregar_habilidad
print("3. Agregar habilidades:")
print(f"   {agregar_habilidad(usuarios, 1, 'Django')}")
print(f"   {agregar_habilidad(usuarios, 1, 'Python')}")  # Intento de agregar duplicado
print(f"   Habilidades de Ana ahora: {usuarios[0]['habilidades']}")
print()

# Probar resumen_usuarios
print("4. Resumen de usuarios:")
resumen = resumen_usuarios(usuarios)
print(f"   Total de usuarios: {resumen['total_usuarios']}")
print(f"   Usuarios activos: {resumen['usuarios_activos']}")
print(f"   Habilidad más común: {resumen['habilidad_mas_comun']}")
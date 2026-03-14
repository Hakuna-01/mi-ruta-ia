#Condicionales — el código toma decisiones
#Un condicional le dice a Python: "si esto es verdad, haz esto. Si no, haz otra cosa." Es la base de toda lógica de programación.

#   Estructuras basicas

edad = 20

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")

temperatura = 28
llueve = False

if temperatura > 25 and not llueve:
    print("Buen dia para salir")
elif temperatura > 25 and llueve:
    print("Calor pero con paraguas")
else:
    print("Mejor quedarse en casa")

#Bucle for — repetir para cada elemento
#El for recorre una colección y ejecuta código por cada elemento. Ya lo usaste ayer con listas — hoy lo profundizamos.

#   Recorrer una lista
habilidades = ["Python", "FastAPI", "Git"]

for skill in habilidades:
    print(f"Estoy aprendiendo {skill}")

#   range() genera una secuencia de numeros
for i in range(5):
    print(i)

#   range(inicio,fin, paso)
for i in range(1, 11, 2):
    print(i)    #1, 3, 5, 7, 9


# for + if combinados
#La combinación más poderosa para filtrar datos — la usarás constantemente en APIs.

numero = [1,2, 3, 4, 5, 6, 7, 8]

for n in numero:
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

tareas = ["Aprender Python", "Hacer FastAPI", "Subir a GitHub"]

for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")

# Bucle while — repetir mientras una condición sea verdadera
# El while repite un bloque de código mientras una condición sea True. A diferencia del for, no necesita una lista — solo una condición.

# Cuenta regresiva

contador = 5

while contador > 0:
    print(f"Faltan {contador} segundos")
    contador -= 1

print("¡Despegue!")


# break y continue
# break sale del bucle inmediatamente. continue salta a la siguiente iteración.

# break — salir cuando encontramos lo que buscamos
numeros = [3, 7, 2, 9, 4]

for n in numeros:
    if n == 9:
        print(f"Encontré el 9, detengo la búsqueda")
        break
    print(f"Revisando: {n}")

# continue — saltar números pares
for n in range(1, 8):
    if n % 2 == 0:
        continue
    print(n)  # Solo imprime impares
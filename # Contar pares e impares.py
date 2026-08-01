# Contar pares e impares
cantidad = int(input("¿Cuántos números quieres ingresar? "))

numeros = []
for i in range(cantidad):
    valor = int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(valor)

pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)

print("Pares:", pares)
print("Impares:", impares)

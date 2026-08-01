# Encontrar mayor y menor
cantidad = int(input("¿Cuántos números vas a ingresar? "))
numeros = []

for i in range(cantidad):
    valor = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(valor)

mayor = max(numeros)
menor = min(numeros)

print("Mayor:", mayor)
print("Menor:", menor)
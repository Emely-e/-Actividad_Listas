# Suma de elementos
cantidad = int(input("¿Cuántos números quieres sumar? "))

numeros = []
for i in range(cantidad):
    valor = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(valor)

suma = sum(numeros)
print("Suma de los elementos:", suma)

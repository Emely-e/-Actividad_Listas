# Invertir elementos
cantidad = int(input("¿Cuántos elementos vas a ingresar? "))
numeros = []

for i in range(cantidad):
    valor = input(f"Ingresa el elemento {i + 1}: ")
    numeros.append(valor)

invertidos = list(reversed(numeros))

print("Original:", numeros)
print("Invertido:", invertidos)
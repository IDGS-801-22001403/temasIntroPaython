
lista1 = ["Mario", 33, 9, 5, True, "German", 20.0]

print(lista1)

print(lista1[3])  # Elemento en el índice 3
print(lista1[2])  # Elemento en el índice 2
print(lista1[-1])  # Último elemento de la lista

# print(lista1[9])

# Agregar un elemento al final
lista1.append("vargas")
print(lista1)

# Insertar un elemento en una posición específica
lista1.insert(2, "Nada")
print(lista1)

# Agregar múltiples elementos usando extend
lista1.extend(["uno", 1.1, True])
print(lista1)

# Eliminar un elemento específico
# .remove() elimina el valor que indiques; aquí eliminamos el número 33.
if 33 in lista1:
    lista1.remove(33)
print(lista1)

# Eliminar el último elemento con pop
lista1.pop()
print(lista1)

# Combinar dos listas
lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2 
print(lista3)


print(lista2 * 0)  # Devuelve una lista vacía


lista4 = [2, 1, 5, 4, 3]
lista4.sort()  # Ordena la lista en lugar
print(lista4)

del lista4[0]  # Borra el primer elemento (índice 0)
print(lista4)

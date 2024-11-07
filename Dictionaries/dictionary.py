dictionary = {"name":"Leo","age": 19}

# Mostramos el diccionario
print(dictionary)
# Obtenemos un valor por el identificador
print(dictionary["name"])
# Agregamos un nuevo identificador 
dictionary["id"] = 1 

print(dictionary)
# vaicamos el diccionario
# dictionary = {}
# dictionary["id"] = 1

# print(dictionary)

for thing in dictionary:
    print(f"{thing} : {dictionary[thing]}")
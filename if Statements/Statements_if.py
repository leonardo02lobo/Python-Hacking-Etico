#Pedimos 2 numeros al usuario
x = input("what is first number: ")
y = input("what is second number: ")

# Con una condicion evaluamos si el primer numero es mayor al segundo
# La condicion se realiza colocando la palabra reservada if y seguido de un espacio la condicion, se cierra con dos puntos (:) 
# y se sigue con las instrucciones en la parte posterior 
# Cuando se trata de mas condiciones se utiliza el elif que hace referencia al else if de los demas lenguajes
# Termina con un else siempre y cuando sea necesario
if x > y:
    print("the first number is big")

elif y > x:
    print("the second number is big")
else:
    print("the number are the same")
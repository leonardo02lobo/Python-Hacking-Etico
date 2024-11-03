# Definimos una funcion la cual a llamamos function
# Muestra el mensaje de 'Hello'

import time 

number = int(input("what number in is range?: "))

def function(number):
    for i in range(1,number):
        if i % 3 == 0 & i % 5 == 0:
            print(f"{i}= Fizz-Buzz")
        elif i % 3 == 0:
            print(f"{i}= Fizz")
        elif i % 5 == 0:
            print(f"{i}= Buzz")
        else:
            print(i)


print("I see now")
time.sleep(5)
# Llamamos a la funcion
function(number)
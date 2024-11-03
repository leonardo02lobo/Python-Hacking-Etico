# Codificacion del fizz-buzz 
# Escribe una secuencia de numeros que cumpla lo siguiente
# divisibles entre 3 fizz
# divisibles entre 5 buzz
# divisibles entre 3 y 5 fizz-buzz

for i in range(1,100):
    if i % 3 == 0 & i % 5 == 0:
        print(f"{i}= Fizz-Buzz")
    elif i % 3 == 0:
        print(f"{i}= Fizz")
    elif i % 5 == 0:
        print(f"{i}= Buzz")
    else:
        print(i)
alum = {}

off = False
while not off:
    name = input("What is your name?: ")
    grade = input("What is your grade?: ")

    alum[name] = grade
    print(alum)
    proccess = input("Continue? Y or N: ").lower()

    if proccess != "y":
        off = True
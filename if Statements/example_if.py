note = int(input("what is your note?: "))

if note >= 90:
    age = int(input("what is your age?: "))

    if age < 10:
        print("GRADE A+")
    else:
        print("GRADE A")
elif note >= 80:
    print("GRADE B")
elif note >= 70:
    print("GRADE C")
elif note >= 60:
    print("GRADE D")
else:
    print("GRADE E")
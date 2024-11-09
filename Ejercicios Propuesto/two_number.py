list = [3,4,1,5,4,3,5,7,9,2,3,2,4]

num = 9

def two_number(num,list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)-1):
            # print(f"{i} == {j}")
            # print(f"{list[j] + list[j+1]} == {num}")
            if list[i] + list[j+1] == num:
                return f"{i},{j}"

print(two_number(num,list))
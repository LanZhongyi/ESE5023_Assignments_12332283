a = float(input("Please write down the first number: "))
b = float(input("Please write down the second number: "))
c = float(input("Please write down the third number: "))

def Print_values():

    if a > b:
        if b > c:
            return a, b, c
        elif a > c:
            return a, c, b
        else:
            return c, a, b
    elif b > c:
        if a > c:
            return b, a, c
        else:
            return b, c, a
    else:
        return c, b, a
    
print(Print_values())

def Least_moves(x):
    n = 0
    while x > 1:
        if x %2 == 0:
            x = x / 2
        else:
            x = x - 1
        n = n + 1
    return n

print(Least_moves(5))
print(Least_moves(60))
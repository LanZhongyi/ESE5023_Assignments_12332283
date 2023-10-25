# 定义一个用于计算阶乘的函数
def factorial(n):
    y = 1
    for i in range(1, n+1):
        y = y * i        
    return y


def Pascal_triangle(k):
    for i in range(1, k+1):
        # 第k行第i个数的值
        x_ki = factorial(k-1) / (factorial(i-1) * factorial(k-i))
        print(x_ki)

print(Pascal_triangle(100))
print(Pascal_triangle(200))
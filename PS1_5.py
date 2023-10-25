# PS1_5.1
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '']
def Find_expression(x):
    import itertools
    for op1, op2, op3, op4, op5, op6, op7, op8 in itertools.product(operators, repeat=8):    # 对8个空位进行operators的全排列
        expression = digits[0]+op1+digits[1]+op2+digits[2]+op3+digits[3]+op4+digits[4]+op5+digits[5]+op6+digits[6]+op7+digits[7]+op8+digits[8]
        if eval(expression) == x:    # eval()函数用于执行一个字符串表达式，并返回表达式的值
            print(expression+'='+str(x))
    return expression
Find_expression(50)


# PS1_5.2
import itertools
Total_solutions = []
for i in range(1, 101):
    n = 0
    for op1, op2, op3, op4, op5, op6, op7, op8 in itertools.product(operators, repeat=8):
        expression = digits[0]+op1+digits[1]+op2+digits[2]+op3+digits[3]+op4+digits[4]+op5+digits[5]+op6+digits[6]+op7+digits[7]+op8+digits[8]
        if eval(expression) == i:
            n += 1
    Total_solutions.append(n)
print(Total_solutions)

import matplotlib.pyplot as plt
i_list = list(range(1, 101))
# 创建一个图形  
plt.figure()
# 在图形上绘制折线图  
plt.plot(i_list, Total_solutions)
# 添加标题和轴标签  
plt.title('Plot the list Total_solutions')  
plt.xlabel('i')  
plt.ylabel('Total solutions')
# 显示图形  
plt.show()

for i in range(100):
    if Total_solutions[i] == max(Total_solutions):
        maximum = i + 1
        print(str(maximum) + ' yields the maximum of Total_solutions.')
    elif Total_solutions[i] == min(Total_solutions):
        minimum = i + 1
        print(str(minimum) + ' yields the minimum of Total_solutions.')
    else:
        pass
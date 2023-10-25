import numpy as np

arr1 = np.random.randint(0, 51, 50)
arr2 = np.random.randint(0, 51, 50)
M1 = arr1.reshape(5, 10)
M2 = arr2.reshape(10, 5)
print(M1)
print(M2)

def Matrix_multip():
    M = np.zeros((5, 5))
    for m in range(5):
        for l in range(5): 
            for n in range(10):            
                M[m,l] += M1[m,n]*M2[n,l]
    return M

print(Matrix_multip())

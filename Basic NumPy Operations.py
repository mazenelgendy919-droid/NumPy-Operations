import numpy as np
A = np.array([10,20,30,40,50])
B = np.array([5,4,3,2,1])

print("addition of two arrays is :"+ str(A+B))
print("subtraction of two arrays is :"+ str(A-B))
print("multiplication of two arrays is :"+ str(A*B))
print("division of two arrays is :"+ str(A/B))

print(A.mean())
print(A.max())
print(A.min())

#dot_product = np.dot(A, B)
#print(dot_product)
print("dot product of two arrays is :"+ str(np.dot(A, B)))

#reshaped_A = A.reshape(5,1)
#print("reshaped array1 is :\n"+ str(reshaped_A))
print("reshaped array1 is :\n"+ str(A.reshape(5,1)))
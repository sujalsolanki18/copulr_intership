import numpy as np
a2=np.array([[4,5,6],[7,8,9],[12,15,18]])
print("max is :",a2.max())
print("min is :",a2.min())

print("shape of array rows,columns :",a2.shape)

print("element:",a2[1,2])

sum=0
for x in a2:
    for y in x:
        sum+=y
print("sum is :",sum)

a=np.array([[1,2,3],[4,5,6]])                    
b=np.array([[56,75,92],[643,596,832]])
print("addition is ",a+b)                               #performing mathematical operation
print("subtraction is",a-b)                                   #both should be of same length
print("multiplication is ",a*b)
print("dividation is ",a/b)
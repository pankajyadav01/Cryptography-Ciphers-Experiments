
# coding: utf-8

# In[13]:


def gf(m,op):
    matrix=[]
    n=2**m
    for i in range(n):
        matrix.append([0]*n)
    l=m-1
#     l=len(bin(n)[2:])-1
#     m=int('1011',2)
    for i in range(n):
        for j in range(n):
            a=eval(str(i)+op+str(j))
            b=int(a)
            c=b%n
            d=bin(c)[2:]
            matrix[i][j]=d
    return matrix

n=int(input("enter modulo: "))
print("\nAddition table \n")
print(gf(n,'+'))
print("\nMultiplication table \n")
print(gf(n,'*'))


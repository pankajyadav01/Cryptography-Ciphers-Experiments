
# coding: utf-8

# In[20]:


s=[[9,4,'A','B'],
  ['D',1,8,5],
  [6,2,1,0],
  ['C','E','F',7]]
x=[]
y=[]
n=1
def conv(a):
    z=str(a)
    return (s[int(z[0]+z[3],2)][int(z[1]+z[2],2)])
    
print("Enter an Input Matrix")
for i in range(4):
    x.append([])
    y.append([])
    for j in range(4):
        a=int(input("Enter Element "+str(n)))
        n=n+1
        if(a<0 or a>16):
            print("invalid Input")
            break
        else:
            x[i].append(hex(a))
            y[i].append(conv(bin(a)[2:].rjust(4,'0')))
print("Input Matrix :\n")    
for row in x:
    print(row)
    print()
print("Output Matrix :\n")
for row in y:
    print(row)
    print()


# ## 3## 

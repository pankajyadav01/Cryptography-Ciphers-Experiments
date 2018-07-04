
# coding: utf-8

# In[1]:


def matrix(key):
    matrix=[]
    for i in key.upper():
        if i not in matrix:
            matrix.append(i)
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for i in alphabet:
        if i not in matrix:
            matrix.append(i)
    matrix2=[]
    j=0
    for i in range(5):
        matrix2.append([])
    for i in range(5):
        matrix2[i]=matrix[j:j+5]
        j=j+5
    return matrix2

def newText(text):
    msg=[]
    for i in text:
        msg.append(i)
    i=0
    for j in range(int(len(msg)/2)):
        if msg[i]==msg[i+1]:
            msg.insert(i+1,'X')
        i=i+2
    if len(msg)%2==1:
        msg.append("X")
    i=0
    new=[]
    for x in range(1,int(len(msg)/2)+1):
        new.append(msg[i:i+2])
        i=i+2
    return new
def newText2(cipher):
    i=0
    new=[]
    for x in range(int(len(cipher)/2)):
        new.append(cipher[i:i+2])
        i=i+2
    return new

def pos(matrix,n):
    a=b=0
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j]==n.upper():
                a=i
                b=j
    return a,b

def crypt(text,matrix,n):
    cipher=[]
    c=1
    if n==0:
        c=-c
    for i in text:
        
        i1,j1=pos(matrix,str(i[0]))
        i2,j2=pos(matrix,str(i[1]))
        if i1==i2:
            if n==0:
                if j1==0:
                    j1=5
                if j2==0:
                    j2=5
            else:
                if j1==4:
                    j1=-1
                if j2==4:
                    j2=-1
            cipher.append(matrix[i1][j1+c])
            cipher.append(matrix[i1][j2+c])
        elif j1==j2:
            if n==0:
                if i1==0:
                    i1=5;
                if i2==0:
                    i2=5;
            else:
                if i1==4:
                    i1=-1;
                if i2==4:
                    i2=-1;
            cipher.append(matrix[i1+c][j1])
            cipher.append(matrix[i2+c][j2])
        else:
            cipher.append(matrix[i1][j2])
            cipher.append(matrix[i2][j1])
    return cipher

text = input("Enter a Plain Text : ")
text = text.replace(" ", "")
s1 = (input("Enter a Key value : "))
matrix = matrix(s1)
print("Key Matrix :")
print(matrix)
text1 = newText(text)
print("plain text blocks : ")
print(text1)
cipher = crypt(text1,matrix,1)
print()
print ("Plain Text : " + text.lower())
print ("Key : " + str(s1))
print ("Cipher Text: ")
print (cipher)
print ("Plain Text(Decryption): ")
text2 = newText2(cipher)
print ( crypt(text2,matrix,0))


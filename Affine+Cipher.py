
# coding: utf-8

# In[8]:


def inverse(a):
    a = a % 26;
    for x in range(1, 26) :
        if ((a * x) % 26 == 1) :
            return x
    return -1

def encrypt(text, a, b):
    result = ""; 
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result +=  chr((((a * (ord(char)-65) ) + b) % 26) + 65)
        else:
            result +=  chr((((a * (ord(char)-97) ) + b) % 26) + 97)    
    return result

def decrypt(text, a, b):
    b= -b
    a= inverse(a)
    if a== -1:
        return "No Inverse Present"
    result = ""; 
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result +=  chr(((((ord(char)-65) + b ) * a) % 26) + 65)
        else:
            result +=  chr(((((ord(char)-97) + b ) * a) % 26) + 97)    
    return result


text = input("Enter a Plain Text : ")
text = text.replace(" ", "")
s1 = int(input("Enter a Key1 value : "))
s2 = int(input("Enter a Key2 value : "))
cipher = encrypt(text,s1,s2).upper()
print()
print ("Plain Text : " + text.lower())
print ("Key1 : " + str(s1))
print ("Key2 : " + str(s2))
print ("Cipher Text: " + cipher)
print ("Plain Text(Decryption): " + decrypt(cipher,s1,s2).lower())



# coding: utf-8

# In[16]:


def crypt(text,s,n):
    result = ""
    if n==0:
        s= -s
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

text = input("Enter a Plain Text : ")
text = text.replace(" ", "")
s = int(input("Enter a Key value : "))
cipher = crypt(text,s,1).upper()
print()
print ("Plain Text : " + text.lower())
print ("Key : " + str(s))
print ("Cipher Text: " + cipher)
print ("Plain Text(Decryption): " + crypt(cipher,s,0).lower())



# coding: utf-8

# In[ ]:


Pankaj Yadav (15-CSU-145)


# # DES Key-Generation

# In[5]:


parity=[[57,49,41,33,25,17,9,1],
       [58,50,42,34,26,18,10,2],
       [59,51,43,35,27,19,11,3],
       [60,52,44,36,63,55,47,39],
       [31,23,15,7,62,54,46,38],
       [30,22,14,6,61,53,45,37],
       [29,21,13,5,28,20,12,4]]

compression=[[14,17,11,24,1,5,3,28],
            [15,6,21,10,23,19,12,4],
            [26,8,16,7,27,20,13,2],
            [41,52,31,37,47,55,30,40],
            [51,45,33,48,44,49,49,56],
            [34,53,46,42,50,36,29,32]]

key='AABB09182736CCDD'

def lshift(key,rno):
    temp1=key[:28]
    temp2=key[28:]
    temp11=temp1[rno:] + temp1[:rno]
    temp22=temp2[rno:] + temp2[:rno]
    temp=temp11+temp22
    return temp

print('Initial Key(64bit) :\t\t\t'+key)
key_int = int(key, 16)
key_bin = bin(key_int)[2:]
str_key_bin=str(key_bin)
# key_hex = key_int + 0x200
# print(hex(key_hex)[2:])
print('Initial Key in Binary :\t\t\t'+str_key_bin)

key1=''
for i in range(7):
    for j in range(8):
        key1+=str_key_bin[parity[i][j]-1]

print('Binary Key after Parity Drop :\t\t'+key1)
key1_int = int(key1, 2)
key1_hex = key1_int + 0x200
print('Key(Hex) after Parity Drop(56bit) :\t'+ hex(key1_hex)[2:])
round_no=1
n=2
a1=[]
round_keys=[]
for i in range(16):
    if (round_no==1 or round_no==2 or round_no==9 or round_no==16):
        n=1
    else:
        n=2
    key1 = lshift(key1,n)
    round_no+=1
#     print('\t\t\t\t\t'+key1)
    for j in range(6):
        for k in range(8):
            a1+=key1[compression[j][k]-1]
    a=''.join(a1)
    round_keys.append(a)
    del a
    a1=[]
print('\n\n')
for i in range(16):
    print('Binary Key for round '+str(i+1)+' is :'+str(round_keys[i]))
    
print('\n\n')
for i in range(16):
    round_key_int = int(round_keys[i], 2)
    round_hex = round_key_int + 0x200
    print('Key(Hex) for round '+str(i+1)+' is :'+ hex(round_hex)[2:])


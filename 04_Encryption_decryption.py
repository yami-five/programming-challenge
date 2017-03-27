#from random import randint
alphabet="abcdefghijklmnopqrstuwvxyz"
cipher="lsavwipezjyrgdtqocnxuhkfbm"
str1=input("Write password: ")
str2=""
for x in range(0,len(str1)):
    if str1[x]==' ':
        str2+=' '
    else:
        str2+=cipher[alphabet.index(str1[x])]
print("Encryption: ",str2)
str1=""
for x in range(0,len(str2)):
    if str2[x]==' ':
        str1+=' '
    else:
        str1+=alphabet[cipher.index(str2[x])]
print("Dencryption: ",str1)
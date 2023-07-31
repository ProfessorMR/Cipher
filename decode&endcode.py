# Cipher algorithm for those who are interested in encode and decryption

import string 
# import os

# os.system("cls")
print("!program is running!")
print("=================================================")

EnDecode = input("choose between encode and decode? ")
print("-----------------------------------------------")


stringlower = string.ascii_lowercase + string.ascii_lowercase
stringupper = string.ascii_uppercase + string.ascii_lowercase

data = []

if EnDecode == "encode":
    key = int(input("Enter a key for encode (Between 1 and 25): "))
    print("-----------------------------------------------")

    if 1 <= key <= 25:
        name = input("Enter a name for encode: ")
        for i in name:
            if i in stringlower:
                
                data.append(stringlower[string.ascii_lowercase.index(i) + key])
            elif i in stringupper:
                data.append(stringupper[string.ascii_uppercase.index(i) + key])
            else:
                data.append(i)
    else:
        print("Out of the range:(")
        exit(0)
                
elif EnDecode == "decode":
    key = int(input("Enter a key for decode (Between 1 and 25): "))
    print("-----------------------------------------------")
    if 1 <= key <= 25:
        name1 = input("Enter a name for decode: ")
        for i in name1:
            if i in stringlower:
                data.append(stringlower[string.ascii_lowercase.index(i) - key])
            elif i in stringupper:
                data.append(stringupper[string.ascii_uppercase.index(i) - key])
            else:
                data.append(i)
    else:
        print("Out of the range:(")
        exit(0)
else:
    print("Wrong input!")
    exit(0)

print("-----------------------------------------------")    
print("your anwser is qual:","".join(data))
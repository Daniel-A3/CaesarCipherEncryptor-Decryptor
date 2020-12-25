encryptedString = input("Enter the encrypted string : ")
shift = input("Enter the shift : ")

for i in encryptedString:
    num = ord(i)
    num += int(shift)
    newChar = chr(num)
    print(newChar, end='')
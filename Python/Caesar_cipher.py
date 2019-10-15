s=int(input("Select 1 for Encrypting select 2 for Decrypting : "))
if s==1:

    x=[i for i in input("Enter String to Encrypt : ").split(" ")]
    y=int(input("Enter Shifting Number : "))
    for i in x:
        print("".join(chr(ord(j)+y) for j in i))

elif s==2:
    x=[i for i in input("Enter String to Decrypt : ").split(" ")]
    y=int(input("Enter Shifted Number : "))
    for i in x:
        print("".join(chr(ord(j)-y) for j in i))

else:
    print("INVALID SELECTION")

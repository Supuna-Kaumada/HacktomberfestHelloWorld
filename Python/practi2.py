x=int(input("EnterSubject Mark 1;"))
y=int(input("EnterSubject Mark 2;"))
z=int(input("EnterSubject Mark 3;"))
a=x+y+z
b=a/3
if(b>80):
    print("your grade is A")
elif(b>60):
    print("your grade is B")
elif(b>40):
    print("your grade is c")
else:
    print("your are fail")

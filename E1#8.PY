def compare(a,b,c):
    if a>b and a>c:
        print("the greatest number is: ",a)
    elif b>a and b>c:
        print("the greatest number is: ",b)
    else:
        print("the greatest number is: ",c)


a=int(input("input first number: "))
b=int(input("input second number: "))
c=int(input("input third number: "))
if (a==b==c):
    print("numbers are equal")

elif(a==b or b==c or c==a):
    print ("two numbers are equal")
    compare(a,b,c)

else:
    compare(a,b,c)
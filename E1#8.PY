a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

if a == b == c:
    print("Numbers are equal")

elif a == b or a == c or b == c:
    print("Two numbers are equal")

greatest = max(a, b, c)
print("The greatest number is:", greatest)
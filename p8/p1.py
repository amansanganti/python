a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

def greatest(a , b, c):
    if (a> b and a>c ):
        print(a) # can also be written as "RETURN A"
    elif(b>a and b>c ):
        print(b)
    else:
        print(c)

print(greatest (a, b, c))



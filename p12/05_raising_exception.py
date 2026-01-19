
a = int(input("Enter a number: "))
b = int(input("Enter secomd  number: "))

if (b == 0):
    raise ZeroDivisionError("Our programm is not ment to divide the number by zero")

else:
    print(f"The division of the number is {a/b}")




'''
factorial (1)= 1
factorial (2)= 2x 1
factorial (3)= 3x2x1
factorial (4)= 4x3x2x1
factorial (5)= 5x4x3x2x1


factorial (n) = nx n-1 x.......x 3x2x1

Therefore 
factorial n = n* factorial (n-1)
'''


def factorial(n):
    
    if (n==1 or n==0):
        return 1
    
    return n * factorial (n-1)
n = int(input("Enter the number to factorise: "))
print(f"Factorial of the number is: ", factorial(n))



# print(f"The factorial of this number is: "{factorial(n)})
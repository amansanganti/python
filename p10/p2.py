class calculator:
    def  square(self , x):
        return x*x
    x= int(input("Enter a number to find its square: "))
    print("The square of the number is: ", x*x)
    def cube(self , y):
        return y*y*y
    y= int(input("Enter a number to find its cube: "))
    print("The cube of the number is: ", y*y*y)

    def root(self , z):
        return z**0.5
    z= int(input("Enter a number to find its square root: "))
    print("The square root of the number is: ", z**0.5)
    

# CAN be done by this method also


#     class Calculator:
#     def __init__(self, n):
#         self.n = n 
    
#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()
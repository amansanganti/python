class demo :
    a = 4
    

o = demo()
print(o.a) #Prints the class attribute because the instance attributes is not present
o.a= 0
print(o.a) #Prints the instance attributes because the instance attribute is present
print(demo.a) # prints the class attributes


# This means thatit does not chane the class attributes 

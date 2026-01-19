class employee:
    a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3


o = employee()
print(o.a) # prints the attribute of a
# print(o.b)     #It shows an error because c is not included in the employee class



o = programmer()
print(o.a) # prints the attribute of a
print(o.b) # prints the attribute of b
#  print(o.c).    #It shows an error because c is not included in the programmer class


o = manager()
print (o.a )
print (o.b )
print (o.c )
# prints the attribute of a,b and c because manager class inherits both employee and programmer class
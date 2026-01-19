f = open ("file.txt")

print(f.read())


print(f.close())


# the same can be done using the with statement like this:

with open("file.txt") as f:
    print(f.read())

    # There is no need to explicitly close the file when using 'with' statement

    

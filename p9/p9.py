with open("this.txt", "r") as f:
    data1= f.read()

with open ("copy.txt", "r") as f:
    data2 = f.read()

    if (data1 == data2):
        print("The files are identical")

    else:
        print("The files are not identical")
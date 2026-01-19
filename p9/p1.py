f = open("poems.txt")

data = f.read()

if ("Twinkle"in data):
    print("Yes, Twinkle is prsent")
    print(data)
else:
    print(data)
    f.close()


f.close()
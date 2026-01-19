words = ["donkey", "Aman","Vedant", "Aryan"]

with open ("replace.txt", "r") as f:
    data = f.read()

for word in words:
    data = data.replace (word, "######")

with open ("replace.txt", "w") as f:
    f.write(data)
    print(data)

    

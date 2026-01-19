with open ("this.txt") as f:
    content = f.read()


with open ("new.txt", "w") as f:
    f.write(content)

    import os
    os.remove("this.txt")
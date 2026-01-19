
def remove(l, word):
    n = []
    for item in l:
        if item in l:
            if not(item == n):
                n.append(item.strip(word))
    for item in l:
        l.remove(word)
        return l
    
l = ["harry", "larry", "carry", "ry"]


print(remove(l, "ry"))
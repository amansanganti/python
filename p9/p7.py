with open ("log.txt", "r") as f :
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python " in line:
        print(f"Yes, Python is there in line {lineno}: {line}")
        break
    lineno += 1
    
else:
     print(f"No, Python is not there in line")
    
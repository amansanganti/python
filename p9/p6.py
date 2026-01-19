with open ("log.txt", "r") as f:
    content = f.read()
    if "python" in content:
        print("Yes, Python is there in the content", "On the line: " )
    else:
        print("No, Python is not there in the content")




    


    
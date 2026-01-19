
# with open ("replace.txt", "r") as f:
#     data = f.read()
#     import os
#     def replace(old, new):
#         return data.replace(old, new)

# with open ("replace.txt", "w") as f:
#     data = replace("donkey", "######")
#     f.write(data)
#     print(data)



with open ("replace.txt", "r") as f:
    data = f.read ()

with open ("replace.txt", "w") as f:
    data = data.replace("donkey", "######")
    f.write(data)
    print(data)






    

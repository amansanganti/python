try:
    a = int(input("Hey enter the number: "))
    print(a)

except ValueError as v:
    print("Heyyyyy")
    print(v)

except Exception as e:
    print(e)
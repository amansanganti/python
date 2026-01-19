try:
    a = int(input("Hey enter the number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else") #Agar try succesfully run hogaya tho else ke andar aata he nhi hua run tho except ke andar jaake waha par hi ruk jaaata he
    
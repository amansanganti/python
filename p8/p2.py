# Convert the following into celcius to fahrenite
#  formula c/5 = (f-32)/9

def f_to_c(f):
    return 5*(f-32)/9

f= int (input("Enter the temperature to be converted : "))
c = f_to_c(f)
print(f"{(c, 2)}°C")
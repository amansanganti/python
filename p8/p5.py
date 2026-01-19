def pattern(n):
    if (n==0):
        return #return ka matlab agr ye function run hua tho age ke function ko test karne ko nhi jayega
    print("*" * n )
    pattern(n-1)
n = int(input("Enter the number : "))

pattern(n)
class employee:
    Language = "Python"   # This is a class attributes
    salary = 24000000   
    Company = "Google"

    def __init__(self, name, language , salary , company):  #This is known as a dunder method which is automatically called
        self.name = name
        self.Language = language
        self.salary = salary
        self.Company = company
        print("He is an employee of Google")

    def getInfo(self):
        print(f"The language is {self.Language}.The salary is {self.salary}. The company name is {self.Company}")


    @staticmethod
    def greet():
        print("Hello Good Morning!!")

Aman = employee("Aman", "Java", 130000, "Amazon")
# Aman.Language = "Java Script" # This is an instance attributes
# employee.getInfo(Aman)
# employee.greet()
print(Aman.name, Aman.salary, Aman.Company)




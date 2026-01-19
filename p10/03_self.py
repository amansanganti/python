class employee:
    Language = "Python"   # This is a class attributes
    salary = 24000000   
    Company = "Google"

    def getInfo(self):
        print(f"The language is {self.Language}.The salary is {self.salary}. The company name is {self.Company}")


    @staticmethod
    def greet():
        print("Hello Good Morning!!")

        




Aman = employee()
Aman.Language = "Java Script" # This is an instance attributes


employee.getInfo(Aman)
employee.greet()



class employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class programmer(employee):
#     company = "YouTube"
    
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlang(self):
#         print(f"The name is {self.name} and the language is {self.language}")

class programmer(employee):
    company = "YouTube"
    def showlang(self):
        print(f"The name is {self.name} and the language is {self.language}")


a = employee()
b = programmer()

print(a.company , b.company)


class employee:
    company = "Google"
    def show(self):
        name = "Default name"
        print(f"The name is {self.company} and the salary is {name}")

class coder:
    language = "python"
    def printlang(self):
        print(f"The langauge is {self.language}")

class programmer(employee , coder):
    company = "YouTube"
    def showlang(self):
        print(f"The name is {self.company} and the language is {self.language}")


a = employee()
b = programmer()


b.show()
b.printlang()
b.showlang()


class programmer:
    company = "Microsoft"


    def __init__(self , name , salary, language):
        self.name = name
        self.language = language
        self.salary = salary



p = programmer("Aman", 100000, "Python")
print(p.name , p.salary, p.language , p.company)

r = programmer("Rohan", 120000, "Java")
print(r.name , r.salary, r.language , r.company)



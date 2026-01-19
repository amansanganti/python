class employee:
    salary = 441
    increment = 20
    @property
    def Salaryafterincrement(self):
        return(self.salary + self.salary*(self.increment/100))
    @Salaryafterincrement.setter
    def Salaryafterincrement(self, salary):
        self.increment = ((salary/ self.salary)-1)*100
        # increment = new salry /old salry -1 multiply by 100







e = employee()
e.Salaryafterincrement = 1222
print(e.increment)





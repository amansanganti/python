# class employee:
#     a = 1
#     def show(self):
#         print(f"The class attribute of a is {self.a}")


# e = employee()
# e.a = 10
# e.show()
# In this this will show 10 because we have changed the value of a for this object only but we want only the class attribute to print so by this method we can print it

class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = employee()
e.a = 10
e.show()
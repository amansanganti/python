class Animals:
    def kutta():
        print("This is a kutta")

class pets(Animals):
    def pet():
        print("mujhe patltu janwar kaha jata he ")


class dog(pets):
    @staticmethod
    def bark():
        print("Kutta hu bhonkunga hi na ")


d = dog
d.kutta()
d.bark()
d.pet()
        



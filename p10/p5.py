import random
class Train:
    def __init__(sef, trainNo):
        sef.trainNo = trainNo

    def book(sef, fromStation, toStation):
        print(f"Ticket has been book in the train number{sef.trainNo} to travel from {fromStation} to {toStation}")

    def status(sef):
        print(f"Train number{sef.trainNo} is running on time")

    def fare(sef, fromStation, toStation):
        print(f"The fare of the train number{sef.trainNo} to travel from {fromStation} to {toStation} is {random.randint(300, 5555)}")


t = Train(55611)

t.book("Delhi", "Mumbai")
t.status()
t.fare("Delhi", "Mumbai")
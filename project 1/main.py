"""
We are going to make a game called Rock, Paper, Scissors.
here,
rock : 1
paper : 2
scissors : 3

"""
import random
computer = random.choice([1,2,3])
youstr = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

youdict = { 1: "rock", 2: "paper", 3: "scissors" }
you = youdict[youstr]


if (computer ==1 and youstr==1):
    print("Both players selected rock. It's a tie!")

else:
    if (computer ==1 and youstr==2):
        print("Paper covers rock! You win!")
    elif (computer ==1 and youstr==3):
        print("Rock smashes scissors! You lose.")
    elif (computer ==2 and youstr==1):
        print("Paper covers rock! You lose.")
    elif (computer ==2 and youstr==2):  
        print("Both players selected paper. It's a tie!")
    elif (computer ==2 and youstr==3):
        print("Scissors cuts paper! You win!")
    elif (computer ==3 and youstr==1):
        print("Rock smashes scissors! You win!")
    elif (computer ==3 and youstr==2):
        print("Scissors cuts paper! You lose.")
    elif (computer ==3 and youstr==3):
        print("Both players selected scissors. It's a tie!")

        


                                    

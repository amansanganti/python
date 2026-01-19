import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses+=1
    a = int(input("Try your luck to guess the number: "))

    if (a> n):
        print("Try guessing a lowr number")
    else:
        print("Try guessing a higher number")

print(f"You have guessed the number in just {guesses} attempts!!!")






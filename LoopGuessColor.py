import random

color = ["voilet", "indigo", "blue", "green", "yellow", "orange", "red"]

while True:
    color = color[random.randint(0,len(color) -1)]
    guess = input("Guess Color From VIBGYOR: ")

    while True:
        if (color == guess.lower()):
            break
        else:
            guess = input("You Guessed Wrong, Try Again: ")
    
    print("Good Job ! You Won!!!!", color)

    again = input ("Wanna Test Your Chances One More (Press no to Exit): ")

    if again.lower() == 'no':
        break





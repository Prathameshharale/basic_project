import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Enter your choice: "))
    if(a > n):
        print("This number is high....Think about a lower one")
    elif(a < n):
        print("This number is low....Think about a higher one")
    else:
        print(f"Yes!! That's the number\nYou took {guesses} guesses to guess the correct number")



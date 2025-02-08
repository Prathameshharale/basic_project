8
import random # for randomly choosing answer for computer

computer = random.choice([1, -1, 0])
youstr= input("Enter your choice: ")
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissors"}#made for additional info

you = youDict[youstr]
# by now we have 2 variables i.e you and computer

print(f"your choice: {reverseDict[you]}\ncomputer choice: {reverseDict[computer]}") # additional info

if (computer == you):
    print("you both chose same")

else:
    if(computer == 1 and you == -1):
          print("You won")

    elif(computer == -1 and you == 1):
            print("You lose")

    elif(computer == 1 and you == 0):
          print("You lose")

    elif(computer == 0 and you == 1):
          print("You won")

    elif(computer == -1 and you == 0):
          print("You lose") 

    elif(computer == 0 and you == -1):
          print("You won")           



      
     








      
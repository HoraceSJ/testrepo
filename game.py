#DEVLOP A SIMPLE GAME 
import random # importing module with funtions 
computervalue = random.randrange(1,10) # pick num between 1 and 10 
playervalue = int(input("Guess a number between 1 and 10: "))
numberoftries = 1
trylimit = 3

#while playervalue != computervalue or numberoftries < trylimit:
    #playervalue = int(input("Wrong guess, Try again: "))
    #numberoftries = numberoftries + 1

num_of_tries= 0
player_guess=int(input("Guess number from 1 to 10:"))
while player_guess != computervalue:
    num_of_tries+=1
    player_guess = int(input("Wrong guess try again: "))
    if num_of_tries==3:
        print("Out of tries")
print("You won")

#for x in range(2):
   # if playervalue != computervalue:
     #   playervalue = int(input("Wrong guess, try again: "))
   # else: 
   #     print("You won!")
#print("No more tries left!")




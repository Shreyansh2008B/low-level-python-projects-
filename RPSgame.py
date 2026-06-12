#rock paper scissor
import random
play = True
wins =  {   ("rock","scissor"),("paper","rock"),("scissor","paper")}
while(play):
    user_input = input("choose[rock,paper,scissor]").lower()
    computer = random.choice(["rock","paper","scissor"])
    print("User: " +str(user_input))
    print("computer: " +str(computer))
    if (user_input,computer) in wins:
        print("You won")
    elif(user_input == computer):
        print("Draw")
    else:
        print("you lose")
    play_again= input("Do You Want to play Again(y/n)")  
    if(play_again =="y"):
            play =True
           
            
    elif(play_again=="n"):
            
            play =False
    else:
            print("No valid input Quitting....")
            play = False





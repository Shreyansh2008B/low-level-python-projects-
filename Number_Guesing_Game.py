#number guessing game

import random  
x  = random.randint(1,101)  #generates a random number in range()
#print(x)
count =0 #keep track of trials
play = True
while(play): #keep the loop on till the game is finished
    user_number = int(input("Guess The number bewteen[1-100]: "))
    if(user_number > x):
        print("go lower")
        count+=1
    elif(user_number<x):
        print("go higher")
        count+=1
    else:
        print("congratulations you guessed the correct number! in " + str(count+1)+" trials")
        play_again= input("Do You Want to play Again(y/n)")
       
        if(play_again =="y"):
            play =True
            x  = random.randint(1,101)
            count =0
            #print(x)
            
        elif(play_again=="n"):
            
            play =False
        else:
            print("No valid input Quitting....")
            play = False

print("Thanks for playing")

        

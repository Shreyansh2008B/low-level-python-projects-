import random
import string
password=""
generate = True
while(generate):
    user_input = int(input("Enter Password lenght: "))

    Random_words = string.digits + string.ascii_letters +string.punctuation

    for i in range(user_input):
        password =   password + random.choice(Random_words)
    print("Your password is : " + password)
    user_input = input("Do you want new one(Y/N): ").upper()
    if(user_input =="Y"):
        user_input = int(input("Enter Password lenght: "))

        Random_words = string.digits + string.ascii_letters +string.punctuation

        for i in range(user_input):
            password +=  random.choice(Random_words)
        print("Your password is : " + password)
    elif(user_input=="N"):
        generate=False

print("Your password is Saved as : " + password)


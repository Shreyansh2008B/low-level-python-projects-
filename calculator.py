#calculator

Number_input = int(input("Enter A number: "))
number = Number_input # store initail value and modify it later

calculate  = True
def Add(number1 ,number2):   # this all functions to perform on numbers
    return number1+number2
def Subtract(number1 ,number2):
    return number1-number2
def Multiply(number1 ,number2):
    return number1*number2
def Divide(number1 ,number2):
    return number1/number2
op1 =[" Added to "," Subtracted "," Multiplied by "," Divided by "," Power to "] #list used for text
op = ["1","2","3","4","5"] #used to keep loop true 
print("select a operation to perform on Number")
operation = input("1)Add\n2)Subtract\n3)Multiply\n4)Divide\n5)power : ")
while(calculate):
    
    
    Number_input = int(input("Enter A number :")) #enter 2nd number
    text = str(number)
    if operation == "1":
        number = Add(number,Number_input)
       
    elif operation=="2":
        number = Subtract(number,Number_input)
    elif operation=="3":
        number = Multiply(number,Number_input)
    elif operation=="4":
        number = Divide(number,Number_input)
    elif operation=="5":
        number = pow(number,Number_input)
    else:
         print("No valid operation was entered ")
         print("Exiting....")
         quit()
        
    text =  text + op1[int(operation)-1] + str(Number_input) + " is " +str(number)
    
    print(text)

   
    operation = input("Press x to exit or select a opeartion[1 2 3 4 5 ] to continue: ")
    if(operation =="x" or operation =="X"): #if u want to exit
        calculate = False
    elif(operation in op): #if u want to continue on current number
        calculate=True
    else:
        print("No valid operation was entered ")
        print("Exiting....")
        quit()
        







    


   










    

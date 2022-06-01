#Josiah Jethro M. Paquiz
#Ian Bautista

import random
import os

def num(): #Generate a random number for given variable
    num = float(random.randrange(0,9))
    return num

#Function of every Operators 
def addition(a,b): #For addition operator that user enter 1
    return float(a + b)

def subtraction(a,b): #For subtraction operator that user enter 2
    return float(a - b)

def multiplication(a,b):#For multiplication operator that user enter 3
    return float(a * b)

def division(a,b):#For division operator that user enter 4
    return round(float(a / b),2)

Stop = 0
while Stop != 1: #When the user enter 0 or 5 in choosing operator the program will end
    correct = 0 #for how many times the user gets the coorect answer
    start = 1 # starting point of the problem to solved
    
    #Instruction on how it proceed
    print("Welcome to Math Tutor")
    print("The process is simple, you going to pick 4 operator and enter how many problems you want to solved")
    print("Answer them correclty, the result will be determined to your correct answer")
    print("HAVE FUN!!!")

    #Selcting operator menu
    print("1. Addition          +")
    print("2. Subtraciton       -")
    print("3. Multiplication    *")
    print("4. Division          /")
    print("5. Exit")

    Operators = int(input("Enter your choice operator: ")) #Input operator
    
    if Operators == 5:#When user enter 5, the program end
            Stop = Stop + 1
            print("Thank you for your time, Bye Bye sayonara")
    else:
        rounds = int(input("Enter your desired amount of problem: ")) #When user select 4 operator, it ask how many problem the user wants
        while start <= rounds: #Loop continues till it reach the limit.
           
            #2 variable are random generated from num() function
            a = num()
            b = num()
            
            #if-else statement of operators and goes to operator function when specific select operator will proceed
            #The word will be dictate depending on selecting operator
            if Operators == 1:
                word = "Sum"
                CorrectAns = addition(a,b)
            
            elif Operators == 2:
                word = "Difference"
                CorrectAns = subtraction(a,b)
                
            elif Operators == 3:
                word = "Product"
                CorrectAns = multiplication(a,b)
                
            elif Operators == 4:
                word = "Quotient"
                CorrectAns = division(a,b)
            
            #Ask the problem and the user will answer and the word, a and b variable will be attach to the question
            print("What is the " + word + " of " + str(a) + " and " + str(b) + "? ") 
            if CorrectAns == float(input("Answer: ")):# When user is correct gets an increement of correct value
                print("Correct")
                correct = correct + 1
            else:
                print("Wrong, Correct answer is " + str(CorrectAns)) #Tells the right answer
                
            if start == rounds: #When the round is done it shows the result and tell the user to play again or not
                while True:
                        print("Your score: " + str(correct) + "/" + str(rounds))
                        print("Do you want to try again?")
                        Try = input("type 1 = yes, 0 = no:  ")
                        if Try == "1":
                            os.system('cls')
                            break
                        elif Try == "0":
                            Stop = Stop + 1
                            print("Thank you for your time, Bye Bye sayonara")
                            break
                        else:
                            continue
                break
            else: # When the answer is done, it proceed to another problem and start will be increement
                start = start + 1
            


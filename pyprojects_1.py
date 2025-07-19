print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")

#######################
import random as r
#print(help(random))
#######################
random_number=0
v=0
def randy():
    global random_number
    random_number=r.randint(0,999)
    random_number=str(random_number)
    return random_number
Ladybug=0

def compare(number):
    global Ladybug
    if number==random_number:
        print("You got it!")
        z=input("Do you want to play again? (yes or no)")
        if z == "yes":
            return
        else:
            print("Thanks for playing!")
    else:
        return
    position(number)
    if Ladybug==0:
        digit(number)
     
def position(number):
    global Ladybug
    count=0
    for i in range(0,2):
        if random_number[i]==number[i]:
            count=count+1
            Ladybug=count
    print("Fermi"*count)
def digit(number):
    count=0
    for i in range(0,2):
        for j in range(0,2):
            if random_number[i]==number[j]:
                count=count+1
    if count==0:
        print("Bagels")
    else:
        print("Pico"*count)
def Play(number):
    global v
    if number==random_number:
        print("You got it!")
        z=input("Do you want to play again? (yes or no)")
        if z == "yes":
            v=1
            return
        else:
            print("Thanks for playing!")
            
            

while True:
    randy()
    for v in range(1,10):
        number=input(f"Guess #{v}:")
        Play(number)
        compare(number)
        if v == 10:
            z=input("Do you want to play again? (yes or no)")
            if z == "yes":
                v=1
            elif z=="no":
                print("Thanks for playing!")
                break
    break






            

            
        
    


    
                





    

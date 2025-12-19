def Happy_Birthday(x,y):
    print (f'Happy birthday to you {x}\nyou are {y} years old') # block belonging to the function
    # End of function


Happy_Birthday("Brandon",46) # call the function
#order of the parameters defined matters also when function is called it must be of the data type

def display_invoice(username,amount,due_date):
    print(f"hello {username}")
    print(f"your bill is of ${amount:.2f} is due: {due_date}") # ":.2f" is added to make sure 2 decimal places are printed

display_invoice("jennie",42.50156,"01/02")




def add(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def mul(x,y):
    z=x*y
    return z

z=add(1,2)
print(z)
z=sub(1,2)
print(z)
z=mul(1,2)
print(z)
#or
print(add(35,56)) 

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+""+last

full_name = create_name("bro","code")
print(full_name)



def func(x):
    print ('x is', x)
    x = 2 #local variable local to the function
    print ('Changed local x to', x)
x = 50 #global variable throughout the code
func(x)  #the function was called after the variable x was defined
print ('x is still', x)


def say(message, times = 1):
    print (message * times)

say('Hello')
say('World', 5)#as long we dont manually put the paramenter 2 its default value is used making the attribute not mandatory


def func(a, b=5, c=10):
    print ('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)#No order needed also u can just ommit the parameter by mentioning the next or mention all

def printMax(x, y):
    '''Prints thee maximum of two numbers.
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
printMax(3, 5)
print (printMax.__doc__)

#docstrings havent learned

def hello() -> str:
    """Says hello."""
    print("Hello!")

# Output: Says hello.
print(hello.__doc__)   
help(hello) 



difit = "canberra"
print(difit.capitalize())

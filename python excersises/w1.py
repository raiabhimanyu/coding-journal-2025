import string


letters     = string.ascii_letters
digits      = string.digits
punctuation = string.punctuation


def main():
    print("""Request a custom vanity plate for your car but keep these rules in mind:
          1.)All vanity plates must start with 2 letters
          2.)Vanity plates must contain max of 6 and min of 2 characters
          3.)Numbers cant be used in the middle of characters but at the end
          4.)No punctuations and spaces allowed
          """)
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")


def is_valid(plate):
    a=b=c=d=0
    if is_fchar(plate):
        print("Yes Rule 1 is obeyed")
        a=1
    if is_length(plate):
        print("Yes Rule 2 is obeyed")
        b=1
    if is_numend(plate):
        print("Yes Rule 3 is obeyed")
        c=1
    else:
        print("error#3")
    if is_nopunc(plate):
        print("Yes Rule 4 is obeyed")
        d=1
    if a==b==c==d==1:
        return True
    else:
        return False
    

def is_fchar(plate):
    if len(plate) > 2:
        if (plate[0] in letters) and (plate[1] in letters):
                return True
    else:
        if plate[0] in letters:
            return True
        else:
            return False
            
            

def is_length(plate):
    if 2<=len(plate)<=6:
        return True


def is_nopunc(plate):
    for s in plate:
        for i in punctuation:
            if s == i:
                return False
            else:
                return True
            

def is_numend(plate):
    if number(plate[-1]):
        if number(plate[-2]):
            if (not number(plate[-4])):
                return True
            else:
                return False
        else:
            if (not number(plate[-3])) and (not number(plate[-4])):
                return True
            else:
                return False

        
    
def number(plate):
        for i in plate:
            if i in digits:
                return True
            else:
                return False
   

command_user = input("Do u want to make a custom vanity plate:")
if command_user.lower() == "yes":
    main()
else:
    print("Bye")

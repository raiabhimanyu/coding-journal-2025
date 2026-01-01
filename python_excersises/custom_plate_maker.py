import string

letters     = string.ascii_letters
digits      = string.digits
punctuation = string.punctuation

def main():
    """Checks if the name plate is valid"""
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
    return all([is_fchar(plate),is_length(plate),is_numend(plate),is_nopunc(plate)])
def is_fchar(plate):
    """Checks if the name plate obeys Rule#1"""
    return len(plate)>=2 and plate[:2].isalpha()
def is_length(plate):
    """Checks if the name plate obeys Rule#2"""
    return 2<=len(plate)<=6
def is_nopunc(plate):
    """Checks if the name plate obeys Rule#4"""
    return all([char not in punctuation for char in plate])
def is_numend(plate):
    """Checks if the name plate obeys Rule#3"""
    if plate[-1].isdigit():
        if plate[-2].isdigit():
            if (not plate[-4].isdigit()):
                return True
            else:
                return False
        else:
            if (not plate[-3].isdigit()) and (not plate[-4].isdigit()):
                return True
            else:
                return False
   
command_user = input("Do u want to make a custom vanity plate:")

if command_user.lower() == "yes":
    main()
else:
    print("Bye")

#Project success 

#Write a Python function that takes two lists and returns True if they have at least one common member.
list_1=[1,2,3,4]
list_2=[4,5,6,7]

def function(x,y):
    for item in x:
        for items in y:
            if item==items:
                return True

print(function(list_1,list_2))
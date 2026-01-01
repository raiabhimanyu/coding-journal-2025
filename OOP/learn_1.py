class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner
    def Bark(self):
        print("whoof whoof")


class Owner():
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
        
owner1=Owner("Abhi","NYC","1243")
dog1=Dog("Jack","Labrador",owner1)
print(dog1.owner.name)
print("hi")
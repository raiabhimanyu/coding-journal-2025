class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says Meow!")

    def describe(self):
        print(f"{self.name} is a {self.color} cat.")

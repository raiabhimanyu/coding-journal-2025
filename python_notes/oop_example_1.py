class Ball:

    def __init__(self,type,color,material):
        self.type = type
        self.color = color
        self.material = material

    def roll(self):
        print(f"This {self.type} is rolling")

    def spinning(self):
        print(f"This {self.type} is spinning")
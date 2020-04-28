class Car():

    def __init__(self, model=None, color=None, company=None, speed=None):
        self.model = model
        self.company = company
        self.color = color
        self.speed = speed

    def start_car(self):
        print("the speed is: ", self.speed)
        return

c = Car("Mustang", "Black", "Ford", 300)
c.start_car()

class Windows:
    def __init(self, id):
        self.id = id

    def open(self):
        print("Windows opening")
    
    def close(self):
        print("Windows closing")

class Door:
    def __init__(self, id):
        self.id = id

    def open(self):
        print("Door opening")

    def close(self):
        print("Door closing")

class House:
    def __init__(self, price, area):
        self.price = price
        self.area = area
        self.windows = []
        self.doors = []

h1 = House(15000, 200)
w1 = Windows("W 1")
d1 = Door("D 1")

w1.open()



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(self.name, "is walking")

    def stop(self):
        print(self.name, "stoped walking.")

    def birthday(self):
        self.age += 1
    
    def senior(self):
        return self.age > 50

h1 = Human("Carlos", 56)
h1.walk()
h1.stop()
h1.birthday()
print(h1.age)
print(h1.senior())
# print(sen)


class Testing:
    def __init__(self,sound, age):
        self.sound = sound
        self.age = age

    def make_sound(self):
        print(self.sound)
    
    def print_age(self):
        print("My age is ", self.age)


dog = Testing("woof", 10)

dog.make_sound()

dog.print_age()

    

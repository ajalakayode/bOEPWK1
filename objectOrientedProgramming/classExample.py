class Dog:
    legs = 4
    def __init__(self, specie):
        self.specie = specie

    def sound(self): # instance method: methods that has self attatched to it.
        self.type = "woof"
        return "Bark"
    
    def dog_says(self):
        total = self.sum(1,1)
        return f"I am dog, but i know maths. One plus one is equal to {total}"

    @classmethod # decorator
    def print_legs(cls): 
        return f"I have {cls.legs} legs"
    
    @staticmethod # utils function
    def sum(a,b):
        return a + b



fluffy = Dog("German Caucasian") 

# del fluffy.specie -- attribute deleted

# del fluffy.dog_says -- method deleted

# del fluffy -- Object or instance deleted 

# print(fluffy.dog_says())



# Inheritance
class Father:
    def __init__(self):
        self.surname = "Nnanna"
        self.net_worth = 65000000

    def description(self):
        return f"The family of {self.surname}"


class Daughter(Father):
    def __init__(self):
        super().__init__()


maria = Daughter()

print(maria.description())

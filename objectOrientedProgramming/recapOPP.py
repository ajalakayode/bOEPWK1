#     pass
# # the above pass helps prevent error

class Dog:
    def __init__(self, specie):
        self.specie =specie
legs = 4
    
def sound(self): #instance method have self attached to them
    self.type = "whoof"
    return "bark"
    
    
    
fluffy = Dog("german bull")

print(fluffy.specie)



# @classmethod #have decorators this is the at symbol. class method handless class attribute or class related have cls property
# def print_legs(cls):
#     return f"I have {cls.legs} legs" 

# @staticmethod #utility function, thry dont take any self or cls but can take the instance values
# def sum(a,b):
    
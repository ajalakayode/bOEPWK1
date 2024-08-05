'''''
    OOP - Object oriented programming
'''''

# self.name = "kay" class attribute, they are unique
# netWorth = 0 instance attribute, they are general not unique
# methods are used to pass functions into a class 



# class person():
#     # def speak():
#     #     return "I am a software developer"
    
#     pass
# kayode = person

# print(person())



# class person():
#     def __init__(self): #this is a constructor, it creates the attribute of a person
#         self.name = "kayode"
#         self.age = 29
#         self.profession = "software developer"
 

# # # METHOD
#     def speak(self):
#         print(f"Hi I am {self.name} and it's nice to be here")
#         # either the below or above syntax is correct. however, the below wont return none as a value
#         # return f"Hi I am {self.name} and it's nice to be here"
        
# kayode = person()
# print(kayode.speak())
 
#  #method2
# class person():
#     def __init__(self, name, age, profession): #this is a constructor, it creates the attribute of a person
#         self.name = name
#         self.age = age
#         self.profession = profession
 

# # # METHOD
# # instance attributes
#     def speak(self):
#         # print(f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here.")
#         # either the below or above syntax is correct. however, the below wont return none as a value
#         return f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here."
        
        
# kayode = person("kayode", 29, "software developer") #this are called instance
# fadeke = person("fadeke", 33, "farmer")
# print(kayode.speak())
# print(fadeke.speak())


# # CLASS ATTRIBUTES DONT USE self attribute
# # class attribute usually written above the init, and used for common object example is country

# class person():
#     country = "Nigeria" #a class attribute
#     def __init__(self, name, age, profession): #this is a constructor, it creates the attribute of a person
#         self.name = name
#         self.age = age
#         self.profession = profession
 

# # # METHOD
 
#     def speak(self):
#         # print(f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here.")
#         # either the below or above syntax is correct. however, the below wont return none as a value
#         return f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here."
        
        
# kayode = person("kayode", 29, "software developer") #this are called instance
# fadeke = person("fadeke", 33, "farmer")
# print(kayode.speak())
# print(fadeke.speak())
# print(fadeke.country)



# # INSTANCE ATTRIBUTE
# class person():
#     def __init__(self, name, age, profession): #this is a constructor, it creates the attribute of a person
#         self.name = name
#         self.age = age
#         self.profession = profession
 

# # METHOD
 
#     def speak(self):
#         # print(f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here.")
#         # either the below or above syntax is correct. however, the below wont return none as a value
#         return f"Hi I am {self.name}, a {self.age} years old, {self.profession} and it's nice to be here."
        
        
# kayode = person("kayode", 29, "software developer") #this are called instance
# fadeke = person("fadeke", 33, "farmer")
# print(kayode.speak())
# print(fadeke.speak())



    
# class Animal():
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
    
    
#     def speak(self):
#         return f"I am {self.name} and I make {self.sound}"
        
        
# jBull = Animal("jBull", "hwooof")
# print(jBull.speak())



    

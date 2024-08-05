# class Automobile():
#     def __init__(self):
#         self.store = []
        
#     def add_a_car(self):
#         return "Benz"
    
# Benz = Automobile()
# print(Benz.add_a_car())
        
        


# class Automobile():
#     def __init__(self):
#         self.store = []
        
#     def add_a_car(self, carName, model, color, price=0):
#         self.store.append({"carName":carName, "model":model, "color":color, "price":price})
        
    
# Benz = Automobile()
# print(Benz.add_a_car("Lambo", "L5", "Black", 1000000))
# print(Benz.store)



class Automobile():
    store = []
    netWorth = 0
    def __init__(self, name, founded, ceo):
        self.name = name
        self.founded = founded
        self.ceo = ceo
        
    def add_a_car(self, carName, model, color, price=0):
        self.store.append({"carName":carName, "model":model, "color":color, "price":price})
        
        # to do: view cars & update netWorth
        
        def runCompany(self):  #methods or number function
            #while loop
            while True:
                command = input("enter" 'add' to add a car, 'view' to see cars)
            return True
        
    
uniGloball = Automobile("uniGloball, "2005", "Mr.Kayode")
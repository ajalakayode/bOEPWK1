# class Automobile():
#     store = []
#     net_worth = 0
#     def __init__(self, name, founded, ceo):
#         self.name = name
#         self.founded = founded
#         self.ceo = ceo

#     def add_a_car(self, car_name, model, color, price=0):
#         self.store.append({"car_name":car_name, "model":model, "color":color, "price":price})

#     # View Cars
#     def view_cars(self):
#         if len(self.store) == 0:
#             print("No net worth")
#         else:
#             for car in self.store:
#                 print(
#                     "==" * 8,
#                     f"name: {car['car_name']}",
#                     f"model: {car['model']}",
#                     f"color: {car['color']}",
#                     f"price: {car['price']}",
#                     "==" * 8,
#                     sep="\n"
#                 )

#     # update net_worth
#     def update_net_worth(self, price):
#         self.net_worth += int(price)


#     def run_company(self): # methods or member functions
#         while True:
#             command = input("Enter 'add' to add a car, 'view' to to see cars, 'quit', to exit: ")
#             if command == "add":
#                 car_name = input("What is the name of the car: ")
#                 model = input("What is the model: ")
#                 color = input("What is the color the car: ")
#                 price = input("What is the price: ")

#                 self.add_a_car(car_name, model, color, price)
#                 self.update_net_worth(price)
#                 print(f"Car Added. Your net worth is {self.net_worth}")

#             elif command == "view":
#                 self.view_cars()
#             elif command == 'quit':
#                 print(f"Your net worth is {self.net_worth}. Thank you for your services")
#                 break
#             else:
#                 print("Invalid command")


# uni_global = Automobile("Uni Global", "2005", "Mr. Kayode")

# print(uni_global.run_company())








# TRIAL 2 USING INHERITANCE METHOD

class Automobile():
    store = []
    net_worth = 0
    def __init__(self, name, founded, ceo):
        self.name = name
        self.founded = founded
        self.ceo = ceo

    def add_a_car(self, car_name, model, color, price=0):
        self.store.append({"car_name":car_name, "model":model, "color":color, "price":price})

    # View Cars
    def view_cars(self):
        if len(self.store) == 0:
            print("No net worth")
        else:
            for car in self.store:
                print(
                    "==" * 8,
                    f"name: {car['car_name']}",
                    f"model: {car['model']}",
                    f"color: {car['color']}",
                    f"price: {car['price']}",
                    "==" * 8,
                    sep="\n"
                )

    # update net_worth
    def update_net_worth(self, price):
        self.net_worth += int(price)


    def run_company(self): # methods or member functions
        while True:
            command = input("Enter 'add' to add a car, 'view' to to see cars, 'quit', to exit: ")
            if command == "add":
                car_name = input("What is the name of the car: ")
                model = input("What is the model: ")
                color = input("What is the color the car: ")
                price = input("What is the price: ")

                self.add_a_car(car_name, model, color, price)
                self.update_net_worth(price)
                print(f"Car Added. Your net worth is {self.net_worth}")

            elif command == "view":
                self.view_cars()
            elif command == 'quit':
                print(f"Your net worth is {self.net_worth}. Thank you for your services")
                break
            else:
                print("Invalid command")


# uni_global = Automobile("Uni Global", "2005", "Mr. Kayode")

# print(uni_global.run_company())

# APPLY THE INHERITANCE METHOD


# print("Hello")
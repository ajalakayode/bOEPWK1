
# print("Start class work2!!!")

# list_of_numbers = [20, 75, 1, 42, 93, 4, 5]
# print(list_of_numbers)

# largest_number = list_of_numbers[0]

# # for list_of_numbers in list_of_numbers:
# for z in list_of_numbers:
#     if z > largest_number:
#         largest_number = z
    
    
# print(largest_number)


number = [10, 90, 20, 100]
class largest_number:
    def __init__ (self, numbers):
        self.number = numbers
    def find_largest_number(self):
        if not self.numbers:
            return None
        largest_number = self.find_largest_numbers[0]
        for number in self.numbers:
            if number > largest_number:
                largest_number = number
                
            return largest_number
        
print("this is the largest_number")

finder = largest_number(numbers)
print(f"the largest number is {finder.find_largest_number ()}")
        

    
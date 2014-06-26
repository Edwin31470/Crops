import random

class Animal:
    """A Generic Animal"""
    #constructor
    def __init__(self,growth_rate, food_need, water_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = ""

    def needs(self):
        return {"food need":self._food_need,"water need":self._water_need}

    def report(self):
        return {"Type":self._type,"Status":self._status,"Weight":self._weight,"Days Growing":self._days_growing}

    def _update_status(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight>10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Middle age"
        elif self._weight> 0:
            self._status = "Young"
        elif self._weight == 0:
            self._status = "Baby"
        
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()


def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value between 1-10: "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered is not valid, please enter a value between 1-10")
        except ValueError:
            print("Value entered is not valid, please enter a value between 1-10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value between 1-10: "))
            print()
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is not valid, please enter a value between 1-10")
        except ValueError:
            print("Value entered is not valid, please enter a value between 1-10")
    animal.grow(food,water)

def display_menu():
    print("1. Grow Manually Over 1 Day")
    print("2. Grow Automatically Over 30 Days")
    print("3. Report Status")
    print("0. Exit Test Program")
    print()
    print("Please select a menu option: ")

def menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0<= choice <= 4:
                option_valid = True
            else:
                print("please enter a valid option:")
        except ValueError:
            print("Please enter a valid option")
        return choice

def manage_animal(animal):
    print("This is the animal manaagement program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")

def main():
    #instantiation
    new_animal = Animal(23,6,5)
    manage_animal(new_animal)
    
if __name__ == "__main__":
    main()

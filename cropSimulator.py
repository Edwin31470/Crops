import random

class Crop:
    """A generic food crop"""
    def __init__(self,growthRate,lightNeeded,waterNeeded):
        self._growth = 0
        self._daysOld = 0
        self._growthRate = growthRate
        self._lightNeeded = lightNeeded 
        self._waterNeeded = waterNeeded
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        return{"Light Needed":self._lightNeeded,"Water Needed":self._waterNeeded}

    def report(self):
        return{"Type":self._type,"Status":self._status,"Days old":self._daysOld}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._lightNeeded and water >= self._waterNeeded:
            self._growth += self._growthRate
        self._daysOld += 1
        self._update_status()

def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <=10:
                valid = True
            else:
                print("Value entered was not valid - please enter a value between 1 and 10.")
        except ValueError:
             print("Value entered was not valid - please enter a value between 1 and 10.")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <=10:
                valid = True
            else:
                print("Value entered was not valid - please enter a value between 1 and 10.")
        except ValueError:
             print("Value entered was not valid - please enter a value between 1 and 10.")
    crop.grow(light,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 10 days")
    print("3. Report Status")
    print("0. Exit test program")
    print("\nPlease select an option from the menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option\n")
        except ValueError:
            print("Please enter a valid option\n")
    return choice

def manage_crop(crop):
    print("This is the crop management program\n")
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        if option == 2:
            auto_grow(crop,10)
            print()
        if option == 3:
            print(crop.report())
            print()
        if option == 0:
            noexit = False
    print("Thank you for playing crop management!")


def main():
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()

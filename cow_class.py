from animal_class import *

class Cow(Animal):
    """ A Cow"""

    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 23
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 22
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def main():
    cow = Cow()
    print(cow.report())
    manual_grow(cow)
    print(cow.report())
    manual_grow(cow)
    print(cow.report())


if __name__ == "__main__":
    main()
    

from animal_class import *

class Sheep(Animal):
    """ A Sheep """

    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 14
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 13
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def main():
    sheep = Sheep()
    print(sheep.report())
    manual_grow(sheep)
    print(sheep.report())
    manual_grow(sheep)
    print(sheep.report())



if __name__ == "__main__":
    main()
    

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



    
def main():
    new_crop = Crop(1,4,3)
    print(new_crop.report())
    auto_grow(new_crop,10)
    print(new_crop.report())

if __name__ == "__main__":
    main()

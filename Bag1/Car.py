from Bag1.Vechile import Vehicle


class car(Vehicle):

    def maxlimit(self):
        print("max speed is 300")

    def manufacturer(self):
        print("Lambogini")
        print("manufactured on 2022")

obj=car()
obj.maxlimit()
obj.manufacturer()
obj.Co2EmissionTest()
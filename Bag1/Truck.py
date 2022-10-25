from Bag1.Vechile import Vehicle


class Truck(Vehicle):

    def maxlimit(self):
        print("max limit is 100")

    def truckinfo(self):
        print("TN07 BP345")
        print("Purchased on 2021")

obj=Truck()
obj.truckinfo()
obj.maxlimit()
obj.Co2EmissionTest()
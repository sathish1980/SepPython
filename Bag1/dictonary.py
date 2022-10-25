class dictonary():

    def dictonaryimplementation(self):
        car={"name":"Honda","make":"2022","engine":"1800cc"}
        bike={"name":"yamaha","Model":"R15","showroom":["chennai","mumbai","Bangalore","Kerala"]}
        print(car)
        print(car.get("name"))
        print(car.get("names"))
        print(len(car))
        print(bike)
        print(bike.get("showroom"))
        sroom=bike.get("showroom")
        print(sroom[1])
        print(car.keys())
        for eachvalue in car.keys():
            print(car.get(eachvalue))
        print(car.values())
        print(car.items())
        if "names" in car:
            print("yes")
        car["make"]="2000"
        print(car)
        car["enginetype"] = "petrol"
        print(car)
        car.update({"make":"1990"})
        print(car)
        car.update({"color": ["red","blue","greeen","black"]})
        print(car)
        car.pop("engine")
        print(car)
        car.popitem()
        print(car)
        del car["make"]
        print(car)
        #del car
        #car.clear()
        print(car)
        newvar=car.copy()
        print(newvar)
        car.setdefault("enginetype","petrol")
        print(car)

obj = dictonary()
obj.dictonaryimplementation()
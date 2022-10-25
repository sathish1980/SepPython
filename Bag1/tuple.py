class Tuple():

    def tupleimplementation(self):
        fruits=("apple","orange","Banana","Grapes","apple")
        print(fruits)
        print(fruits[1])
        for eachvalue in fruits:
            print(eachvalue)
        print(fruits[1:2])
        print(fruits.count("apples"))
        print((fruits.index("Banana")))
        print(len(fruits))
        veg=("brinjal",)
        print(veg)
        print(type(veg))
        print(fruits[-2])
        if "Grapes" in fruits:
            print("Yes")

        newfruits=list(fruits)
        print(newfruits)
        newfruits.append("Cherry")
        newfruits=tuple(newfruits)
        print(newfruits)
        #del newfruits
        print(newfruits)
        for eachvalue in range(0,len(newfruits)):
            print(newfruits[eachvalue])
        

obj=Tuple()
obj.tupleimplementation()
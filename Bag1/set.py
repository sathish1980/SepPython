class set():

    def setimplementation(self):
        fruits={"apple","banana","orange","apple"}
        newfruits = { "banana", "pineapple"}
        count=[1,2,4,5]
        print(fruits)
        print(count)
        #print(fruits[1])
        for eachvalue in fruits:
            print(eachvalue)
        if "orange" in fruits:
            print("Yes")
        #fruits.add("plums")
        print(fruits)
        #fruits.update(count)
        print(fruits)
        #fruits.remove(4)
        print(fruits)
        fruits.discard("banana")
        print(fruits)
        fruits.pop()
        print(fruits)
        #print(fruits.clear())
        #del fruits
        print(fruits)
        oldfruits = {"apple", "banana", "orange", "apple"}
        newfruits = {"banana", "orange"}
        diffvar=oldfruits.difference(newfruits)
        print(diffvar)
        print(oldfruits)
       # delediff=oldfruits.difference_update(newfruits)
        print(oldfruits)
        print(oldfruits.intersection(newfruits))
        print(oldfruits)
        #print(oldfruits.intersection_update(newfruits))
        print(oldfruits)
        print(oldfruits.issubset(newfruits))
        print(oldfruits.issuperset(newfruits))
        print(oldfruits.symmetric_difference(newfruits))
        print(oldfruits)
        #print(oldfruits.symmetric_difference_update(newfruits))
        print(oldfruits)
        print(oldfruits.union(newfruits))


obj=set()
obj.setimplementation()
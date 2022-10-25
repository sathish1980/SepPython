class listexample():

    def listimplementation(self):
        a=10
        name="sathish"
        print(a)
        print(name)
        fruits=["apple","orange","banana","apple"]
        print(fruits)
        print(fruits[0])
        print(fruits[-2])
        for eachvalue in fruits:
            print(eachvalue)
        print(len(fruits))
        age=[1,34,54,23,56]
        avaialbe=[True,False,True]
        print(fruits[1:4])
        if "strawberry" in fruits:
            print("It exist")
        else:
            print("it doesnot exist")
        print(fruits)
        fruits[1]="strawberry"
        print(fruits)
        fruits[1:3]=["cherry","Mango"]
        print(fruits)
        fruits.insert(1,"canberry")
        print(fruits)
        fruits.insert(4,"grapes")
        print(fruits)
        fruits.append("jackfruit")
        print(fruits)
        fruits.append("chiku")
        print(fruits)
        #fruits.extend(age)
        print(fruits)
        fruits.remove("chiku")
        print(fruits)
        fruits.pop(3)
        print(fruits)
        fruits.pop()
        print(fruits)
        #del fruits
        #fruits.clear()
        print(fruits)
        for eachvalue in fruits:
            print(eachvalue)
        for eachindex in range(0,len(fruits)):
            print(fruits[eachindex])
        i=0;
        while(i<len(fruits)):
            print(fruits[i])
            i=i+1

        fruits.sort()
        print(fruits)
        fruits.sort(reverse=True)
        print(fruits)
        newfruits=fruits.copy()
        print(newfruits)


obj=listexample()
obj.listimplementation()
class stringconcept():

    def stringconceptimplementation(self):
        name=" sathish Kumar .R "
        lasname="kumar"
        print(name)
        print(lasname)
        print(name[0])
        count=0
        for eachvalue in name:
            print(eachvalue)
            if(eachvalue=="a"):
                count+=1
        print(count)
        print(len(name))
        print("Kumar" in name)
        print("Kumar" not in name)
        if "Kumar" not in name :
            print("You are not kumar")
        else:
            print("You are kumar")

        print(name[1:5])
        print(name.upper())
        print(name.lower())
        print(name.lstrip())
        print(name.rstrip())
        print(name.strip())
        print(name.replace(" ",""))
        print(name.split("a")) # it will converted in to a list
        print(name+lasname)
        print(name.isnumeric())
        print(name.isalpha())
        print("this is sathish \"kumar\" .R ")
        print(name.count("a"))
        print(name.find("K"))
        print(name.join(lasname))
        print(name.startswith(" sathish"))
        print(name.endswith("kumar"))

obj=stringconcept()
obj.stringconceptimplementation()
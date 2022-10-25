import re
class regex():

    def regeximplementaion(self):
        name="sathish kumar"
        x=re.search("[1-9]",name)
        print(x)
        sp = re.split("a", name)
        print(sp)

obj = regex()
obj.regeximplementaion()
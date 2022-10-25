class Twelth: #class
    a=100 #global variable
    b=50
    def add(self): #functions
        name="sathish"
        lasname="kumar"
        a=50 #local variable
        b=20
        c=a+b
        print("The addition of ",a,"+",b,"number is : ",c)
        print("The addition of " +str(a) + "+" +str(b) + "number is : " +str(c))
        print(a+b)
        print(name+lasname)

    def sub(self):
        a = 10
        b = 20
        c = a - b
        print("The subtraction of 2 number is : ", c)

    def mul(self,a,b):
        c=a*b
        print("The multiply of 2 number is: ",c)

    def category(self,DOByear):
        a=20
        print(self.a)
        actualage=classobj.age(DOByear)
        print(actualage>18,"You are senior")

    def age(self,DOByear):
        curentage=2022-DOByear
        return curentage

    def comparision(self):
        d=15
        print(self.a!=self.b)
        name="sathish"
        lastname="sathish"
        print(name==lastname)
        age=20
        country="IND"
        state="TN"
        print(age<20 and country=="IN" and state=="TN")
        print(age<20 or country=="IN" )
        print(not(age < 20 or country == "IN"))
        print(age <= 20 and country == "IN" or state == "TN")
        a="sathish"
        b="sathisH"
        print(a is not b)
        a="orange"
        fruits=["apple","orange","banana"]
        print("oranges" in fruits)
        print("orange" not in fruits)

    def voterid(self,age,country):
        if age>18 and country=="IN":
            print("You are eligible to apply voter id")
            if age >65:
                print("You are eligible for senio citizen")
                if age>80:
                    print("you are super senior citizen")

        elif age>15:
            actualwaitperiod=18-age
            print("You will be  eligible to apply voter id in next ",actualwaitperiod ,"years")
        elif age>12:
            actualwaitperiod=18-age
            print("You will be  eligible to apply voter id in next ",actualwaitperiod ,"years" ,"Please be wait")
        else:
            print("You are not eligible to apply voter id")

# Function with out parameter /argument
# Function with parameter /arguments
# Function with return type
# Function with out Return Type

classobj = Twelth()
classobj.add()
classobj.sub()
classobj.mul(4,5)
classobj.category(2020)
classobj.comparision()
classobj.voterid(90,"IN")



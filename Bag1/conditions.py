def trafficlight(lightcolor,vehicle):

    if (lightcolor=="Red"):
        print("You have to stop")
        if (vehicle == "ambulance"):
            print("you have to go now .Please give a way")
    elif (lightcolor=="Green"):
        print("You are good to go")
    elif (lightcolor=="Yellow"):
        print("You are about to go")
    else:
        print("The given color is : " + lightcolor)

trafficlight("Red","ambulance")

def eligibilty(age,state):
    if (age>18):
        print("You are eligible pertaining to age")
    elif (state=="TamilNadu"):
        print("You are eligible pertaining to State")
    else:
        print("You need to wait till you are 18 years old")

eligibilty(18,"TamilNadu")


def conditions(gender):
    if gender=="Male":
        pass
conditions("Male")

def logicaloperators(gender,ticket):
    if not((gender == "Male") and ticket>5) or ticket<5:
        print("You are eligible")
    else:
        print("You are naot elgigible")

logicaloperators("FeMale",4)

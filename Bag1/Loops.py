
def whileloop(number):
    next10number=number+10
    while(number<next10number):
        print(number)
        number+=1

def forloop(number):
    next10number=number+10
    for eachvalu in range(number,next10number):
        print(eachvalu)
        if eachvalu==105:
            break
    fruits=["apple","banana","mango","strawberry"]
    print(fruits)
    for eachfruit in fruits:
        if eachfruit=="mango":
            continue
        print(eachfruit)
def rangefunction(intialvalue,number):
    for value in range(intialvalue,number):
        print(value)


def nestedloop():
    for eachvalu in range(0,10):
        print(eachvalu)
        fruits = ["apple", "banana", "mango", "strawberry"]
        for eachval in fruits:
            print(eachval)
nestedloop()
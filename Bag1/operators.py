def airthmeticoperator():
    print(2+3)
    print(2 - 3)
    print(2 * 3)
    print(2 / 3)
    print(2 % 3)
    print(2 ** 3)
    print(2 // 3)

def assignmentoprator():
    a=10
    #a+=10 # a=a+10
    #a-=10 # a=a-10
    #a*=10 # a=a*10
    #a/=10
    #a%=10
    #a&=10 # a=a&10
    #a|=7 # 10 /7
    a^=5

    print(a)

def comparision():
    a=10
    b=20
    print(a==b)
    print(a!=b)
    print(a>b)
    print(a<b)
    print(a>=b)
    print(a<=b)

def logical():
    a=10
    b=20
    print((a>1 and b<=20))
    print((a > 1 or b < 20))
    print(not (a==10 and b==15))

def identity():
    a=18
    b=11
    print((a is b))
    print( (a is not b))

def membership():
    a=[1,2,5,6]
    b=[1,2,5,6]
    print((a in b))

membership()
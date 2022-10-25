class classname:
    a=10
    def __init__(self): #constuctor
        pass
    def __init__(self,a):
        print("this is construcor"+str(a))

    def add(self,b,a):
        print("add"+str(self.a))
    def add(self,b,a):
        print("sub"+str(self.a))
    def div(self):
        try:
            a=10
            b=0
            if b>0:
                c=a/b
                print(c)
        except ZeroDivisionError:
            print("Ths is exception")
        except:
            print("general error")
        #ZeroDivisionError
        finally:
            print("this is finally")

objname=classname(2)
objname.div()
objname.add(3,4)

class textfile():

    def textfileread(self):

        file=open("C:\\Users\\sathishkumar\\PycharmProjects\\SepPythonBasiconline\\Input\\Testdata.txt","r")
        writefile=open("C:\\Users\\sathishkumar\\PycharmProjects\\SepPythonBasiconline\\Input\\output.txt","w")
        #print(file.read(10))
        #print(file.readline())
        #print(file.readline())
        #print(file.readlines())
        alllines = file.readlines()
        writefile.write("This is entred automatically")

        for eachstring in alllines:
            writefile.write(str(eachstring))
        print("Write comlpeted")

obj=textfile()
obj.textfileread()
from Bag1.School import school


class exams(school):

    def quartely(self):
        print(self.schoolname)
        science=30
        maths=55
        englich=43
        tamil=77
        social=67
        minmar=obj.minimummarks()
        obj.Status(science, maths, englich, tamil, social, minmar)
        Totalmarks=science+maths+englich+tamil+social
        print("totalmarks in quartely",Totalmarks)
        return Totalmarks

    def Status(self,science,maths,englich,tamil,social,minmar):
        if science >= minmar and maths >= minmar and englich >= minmar and tamil >= minmar and social >= minmar:
            print("you passed in all subjectes")
        else:
            print("you fialed in one of the subjectes")

obj=exams()

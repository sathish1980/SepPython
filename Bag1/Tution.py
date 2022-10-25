from Bag1.exams import exams


class tuttion(exams):

    def Grade(self,percentage):
        if percentage>95:
            print("You belongs to grade A")
        elif percentage>85:
            print("You belongs to grade B")
        elif percentage>65:
            print("You belongs to grade C")
        elif percentage>35:
            print("You belongs to grade D")
        else:
            print("You belongs to grade E")

    def percentage(self,totalmark,totalsubject):
        actualpercentage=totalmark/totalsubject
        return actualpercentage

obj=tuttion()
totalmark=obj.quartely()
overallpercentage=obj.percentage(totalmark,5)
obj.Grade(overallpercentage)

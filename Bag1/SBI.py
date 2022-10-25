from Bag1.Bank import Bank


class SBI(Bank):

    def EducationLoan(self):
        print("WElcome to education loan")
        print("interest rate is 5%")

sbi=SBI()
sbi.EducationLoan()
sbi.interestrate()
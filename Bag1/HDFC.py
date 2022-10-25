from Bag1.Bank import Bank


class HDFC(Bank):

    def address(self):
        print("HDFC Address")
        print("chennai")

    def loans(self):
        print("housingloan")
        print("carloan")


hdfc=HDFC();
hdfc.address()
hdfc.loans()
hdfc.interestrate()
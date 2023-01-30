class Calc:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        return self.num1 + self.num2

class SuperCalc(Calc):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.num3 = c

    def addition(self):
        #super(SuperCalc, self).addition()
        print("This is over ridden addition.")

    def log(self):
        print("This is work of super calc",self.num3,self.num1)

calc = Calc(20,10)
print(calc.addition())

superCalc = SuperCalc(50,40,30)
superCalc.log()
superCalc.addition()

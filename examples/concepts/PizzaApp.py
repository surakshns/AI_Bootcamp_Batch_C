#1.Asking for menu
#2.Asking qunatity
#3.Calculating bill
#4.Show the total Bill

class Pizza:

    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def info(self):
        print("Sno--",self.id,"--",self.name,"--",self.price)

p1 = Pizza(1,'Margharita',250)
p2 = Pizza(2,'Chees',150)
p3 = Pizza(3,'Farmhouse',350)

pizzaList = [p1,p2,p3]

def menuSelect():
    if choiceNum== 1:
        return p1
    elif choiceNum== 2:
        return p2
    elif choiceNum== 3:
        return p3


print("Hello Sir, Please select your choice of Pizza?")
print("$$$$$$-------MENU------$$$$$$$")

for i in pizzaList:
    print(i.info())

choiceNum = int(input())
print("congratulation, good choice, ",choiceNum)
print("How many quantity would you like to order?")
choiceQuantity = int(input())
print("congratulation, good choice, ",choiceNum, " good quantity ",choiceQuantity)
selectedPizza = menuSelect()
selectedPizza.info()
totalBill = choiceQuantity*selectedPizza.price
print("Your Total bill will be ", totalBill)




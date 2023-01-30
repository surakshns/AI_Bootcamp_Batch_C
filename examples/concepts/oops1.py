

class Employee:

    #id = 111
    #name = 'Rajesh'
    dept = 'Compliance'

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def myintro(self,i):
        print(i)

    def myintro(self,i=10):
        print("Hello from new my intro", i)


employee1 = Employee(111,'Rajesh')
employee1.myintro()
employee1.myintro(60)

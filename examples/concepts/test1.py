

class Employee:

    #id = 111
    #name = 'Rajesh'
    dept = 'Compliance'

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def myintro(self,i):
        print("Hey this is your coolest Employee Mr ", self.name, "! and my id is ",self.id, i)

    def myintro(self,i=10):
        print("Hey this is your coolest Employee Mr ", self.name, "! and my id is ",self.id, i)


employee1 = Employee(111,'Rajesh')
employee1.myintro()
employee1.myintro(10)

employee2 = Employee(222,'Suraj')
employee2.myintro()
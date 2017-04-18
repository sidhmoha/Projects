class Person:
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def printFullName(self):#self is a pointer to the class instance.It is mandatory for a function of a class
        print(self.firstName," ",self.lastName)


personName=Person()#creates object of Class Person
personName.setFullName("Programming","Knowledge")
personName.printFullName()


class Person:
    def __init__(self,id):#Defination of costructor.member function is automatically called when instance is created
        self.id = id;
        print("Our Class is created")
    def __del__(self):#destructor
        print(self.id,"Our Class Object is destroyed")
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def printFullName(self):  
        print(self.firstName," ",self.lastName)


#p=Person()
personName=Person(5)#constructor is called when a object is created
personName.setFullName("Programming","Knowledge")
personName.printFullName()
#personName.__del__() #desctructor is called

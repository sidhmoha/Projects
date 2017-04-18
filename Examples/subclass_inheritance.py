#inheritance allows us to define a class in
#terms of another class which makes it easier
#to create and maintain an application.

class Parent:#superclass
    value1="this is value 1"
    value2="this is value 2"
    
class Child (Parent):#subclass
    pass #pass is a placeholder.It wont do anything and will skip it

parent_= Parent()
print(parent_.value1)
print(parent_.value2)
child_=Child()
print(child_.value1)
print(child_.value2)

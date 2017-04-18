import re

exampleString= '''Jessica is 15 years old, and Daniel is 27 years old. Edward is 97, and his grandfather Oscar is 102 '''

ages=re.findall(r'\d{1,3}',exampleString)
names=re.findall(r'[A-Z][a-z]*',exampleString)

print (ages)
print(names)

dict={}
x=0

for name in names:
    dict[name]=ages[x]
    x=x+1


print (dict)



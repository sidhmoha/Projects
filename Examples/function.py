# A function is a group of statement that together perform a specific task

def add(x,y):
    return(x+y)
s=add(3,5)
y=add(5,7)

print(s,y)

def studentScore(name,*score):
    print(name)
    print(score)

studentScore("Mark",45,56,78,93,89,24,56)


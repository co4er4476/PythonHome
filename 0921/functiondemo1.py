#mutabe - dict

student = {} #1.dict 만듬

def myinput(man):
    name = input("Enter your name :")
    age = input("Enter your age :")
    man["name"] = name
    man["age"] = age


myinput(student) #2.함수 
print(student)

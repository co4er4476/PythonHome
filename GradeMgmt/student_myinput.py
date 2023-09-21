
#student_input.py

def myinput(student):
    # print(type(student))
    name = input("Enter your name:")
    kor = int(input("Enter your Kor:"))
    eng = int(input("Enter your Eng:"))
    math = int(input("Enter your Math:"))
    
    student["name"] = name
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math
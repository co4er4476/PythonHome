#main.py
import student_myinput
import student_calc
import student_output

print("Program is Start...")
student = {}

student_myinput.myinput(student) #call by reference(갔다오면 바뀌는)
student_calc.calc(student)
student_output.output(student)


print("Program is Over...")

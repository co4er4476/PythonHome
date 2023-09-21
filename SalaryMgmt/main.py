#김선아--main.py
import salary_input
import salary_calc
import salary_output


employee = {}

salary_input.myinput(employee) #call by reference(갔다오면 바뀌는)
salary_calc.calc(employee)
salary_output.output(employee)


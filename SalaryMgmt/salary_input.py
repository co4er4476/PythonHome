#salary_input

def myinput(employee):
    num = int(input("사원번호 :"))
    geup = int(input("급 : "))     #int - 숫자로 인식
    ho = int(input("호 : "))
    sudang = int(input("수당 : "))
    # math = int(input("입력/출력(I/O)? : "))
    employee["num"] = num
    employee["geup"] = geup
    employee["ho"] = ho
    employee["sudang"] = sudang
    #employee[""]
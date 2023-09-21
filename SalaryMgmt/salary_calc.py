

#지급액 환산
def calc(employee):
    #급여
    salaryamount = None
    if employee["geup"] == 1 and employee["ho"] == 1 : salaryamount = 95000
    elif employee["geup"] == 1 and employee["ho"] == 2 :salaryamount = 92000
    elif employee["geup"] == 1 and employee["ho"] == 3 :salaryamount = 89000
    elif employee["geup"] == 1 and employee["ho"] == 4 :salaryamount = 86000
    elif employee["geup"] == 1 and employee["ho"] == 5 :salaryamount = 83000
    elif employee["geup"] == 2 and employee["ho"] == 1 :salaryamount = 80000
    elif employee["geup"] == 2 and employee["ho"] == 2 :salaryamount = 75000
    elif employee["geup"] == 2 and employee["ho"] == 3 :salaryamount = 70000
    elif employee["geup"] == 2 and employee["ho"] == 4 :salaryamount = 65000
    elif employee["geup"] == 2 and employee["ho"] == 5 :salaryamount = 60000
    else : salaryamount = 0    
    
    #지급액
    jigeup = int(salaryamount + employee["sudang"])
    
    
   #세율
    taxperct = None 
    balnum = None 
    if jigeup < 70000 : taxperct = 0;balnum = 0
    elif 70000 <= jigeup < 80000 : taxperct = 0.005;balnum = 300
    elif 80000 <= jigeup < 90000 : taxperct = 0.007;balnum = 500
    elif 90000 <= jigeup : taxperct = 0.012;balnum = 1000
    else : 1000000
    
    
    
    #세금
    mytax = int(jigeup * taxperct - balnum)
    
    #차인지급액
    
    diffamount = int(jigeup - mytax)
    
    employee ["jigeup"] = jigeup    
    employee ["mytax"] = mytax    
    employee ["diffamount"] = diffamount 
    
#세금 계산 = 지급액 X 세율  
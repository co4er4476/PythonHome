first = int(input("Enter a first Number : "))
second = int(input("Enter a second Number : "))

try :
    print(f"{first} / {second} = {first / second}")

except : #예외 발생시 except로 보냄 = Transfer (유저 입력이 수정되도록 메시지 처리)
    print("Invalid Number")
    
# 예외상황을 에러로 간주
# except Exception as err :    
#     print (err) 
    
else : #정상 작업 완료시 출력, except가 발생하지 않고 정상적으로 실행될 때만 else가 뜸. 
    print("Program Successed")


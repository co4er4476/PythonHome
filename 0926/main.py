'''#0926 project''' #가이드에 따라 docstirng 추가
def myfunction(msg) :
    """This function is pylint testing funcion."""
    #a = 0
    #b = 10 #사용되지 않는 변수 삭제
    msg_local = msg
    def myfunction_inner() :
        return msg_local
    return myfunction_inner
MSG = "Hello, World" #문자열은 immutable이므로 변수명 대문자
aaa = myfunction(MSG)
print(aaa())

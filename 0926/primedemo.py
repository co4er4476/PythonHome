
# Python 스크립트를 작성하여 다음을 수행합니다.

# 1~250 사이의 모든 소수를 표시합니다.
# results.txt 파일에 결과를 저장합니다.
# 스크립트를 테스트합니다. results.txt 파일에 예상된 결과를 생성하는지 확인합니다.

# 스크립트를 저장하고 추후 참조를 위해 위치(절대 경로)를 기록해 둡니다.


def prime_print(x) :
    for num in range(2, x-1) :
        if num % x == 0 :
            return False
        
    return True

 
#list, tuple, dict의 타입 = 수정가능한 mutable
#mutable은 경로가 가리키는 실제 공간의 값이 바뀜

#deepcopy
import copy

original = [1,2,3]
# target = original  
target = copy.deepcopy(original) #deepcopy를 하면 lock을 걸어서 실제 값이 바뀌지 않게 됨
print(original, target) # 'target = original'의 예제와 달리 연동되어 바뀌지 않음

original[0] = 10000
print(original, target) #target도 연동되어서 함께 바뀜. mutable 타입.

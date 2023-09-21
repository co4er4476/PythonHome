original = 5
target = original
print('original = %d, target = %d' % (original, target))
original = 100 #original만 새로운 경로를 가리키게 됨
print('original = %d, target = %d' % (original, target))
#immutable: original value와 target value는 서로 전혀 영향을 주지 않는다.

def change (target):
    target = 100
    print("In the def : target = %d" % target)

original = 5
print("Before Call Change : original = %d" %original)
change(original)
print("After Call Change : original = %d" %original)


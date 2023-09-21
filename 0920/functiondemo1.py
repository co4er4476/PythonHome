

def calc_sum(start, end):

    sum = 0
    for i in range(start, end+1):
        sum += i
    # print('%d부터 %d까지의 합은 %d입니다' % (start, end, sum))
    return sum #함수의 끝

start = 50
end = 340
result = calc_sum(start, end)

print("%d부터 %d까지의 합은 %d 입니다." % (start, end, result)) #리턴이 여기로 값을 가지고 감
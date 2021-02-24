# - *- coding: utf- 8 - *-
import math

def power(x, y):
    # 코드를 작성하세요.
    total = x

    if y == 0:
        return 1

    if y == 1:
        return x

    if y%2 ==0:
        #even
        return power(x,y/2) * power (x,y/2)

    else:
        #odd
        return power(x,y//2) * power (x,y//2) * x






# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    prev_fillup_spot = 0
    fillup_spot =[]
    prev = 0

    for i in water_stops:
        if i - prev_fillup_spot > capacity:
            fillup_spot.append(prev)
            prev_fillup_spot = prev
        prev=i

    fillup_spot.append(prev)
    return fillup_spot

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
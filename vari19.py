# - *- coding: utf- 8 - *-

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
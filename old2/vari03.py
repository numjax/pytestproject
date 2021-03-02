def trapping_rain(buildings):
    # 코드를 작성하세요
    tallest = 0
    tallest_idx = 0
    idx = 0
    trap_cnt = 0
    current = 0



    for i in buildings:
        if i > tallest :
            tallest = i
            tallest_idx = idx
        idx+=1


    if tallest == 0:
        return 0



    for i in buildings[:tallest_idx]:

        if current < i :
            current = i
        else:
            trap_cnt = trap_cnt + current -i



    if tallest_idx < len(buildings) - 1:
        current = 0
        for i in  range(len(buildings[tallest_idx+1:])):
            if current < buildings[-(i+1)]:
                current  = buildings[-(i+1)]

            else:
                trap_cnt = trap_cnt + current -buildings[-(i+1)]

    return trap_cnt






# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))






def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height
# - *- coding: utf- 8 - *-
def sublist_max(profits):
    sum = 0
    profit_list = []
    # 코드를 작성하세요.
    for i in profits:
        sum += i
        profit_list.append(sum)
        # print(sum)

    return max(profit_list)

'''
최대 수익 금액을 리턴
부르트 포스

1. 일단 첫 플러스가 나오는 날 부터 시작
2. 위의 시작일자부터 계속 다음날을 하나씩 더해서 리스트에 넣는다.
3. 리스트에서 맥스값을 뽑는다.

'''






# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))





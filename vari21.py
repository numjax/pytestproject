# - *- coding: utf- 8 - *-

# def sublist_max(profits):
#     # 코드를 작성하세요.
#
#     # 종료조건
#     if len(profits) ==1:
#         return profits[0]
#
#     sumFromEnd = 0
#     maxFromEnd = 0
#
#     for i in profits[::-1]:
#         sumFromEnd += i
#         maxFromEnd = max (maxFromEnd, sumFromEnd)
#
#     # print(maxFromEnd)
#
#     max_profit_so_far = max(sublist_max(profits[:-1]), maxFromEnd)
#
#     return max_profit_so_far


# def sublist_max(profits):
#     max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
#     max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합
#
#     # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
#     for i in profits[1:]:
#         # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
#         max_check = max(max_check + i, i)
#
#         # 최대 구간 합을 비교를 통해 정한다
#         max_profit_so_far = max(max_profit_so_far, max_check)
#
#     return max_profit_so_far

'''
그냥 리스트만 보고 설명하자면, 
max_profit_so_far는 앞에서 부터 하나씩 더한다고 가정할 때 첫 양수가나오는 순간부터 해서
최대값을 가지고 있다.
7,                      7
7, -3,                  7
7, -3, 4,               8
7, -3, 4, -8            8
위와 같이 한칸씩 가면서 최대값을 저장하는 거다.
그러면 최대값을 저장하는데 있어서 
중간에 최대값을 넣을 수 있도록 연산이 필요하다.
즉 한 구간에 왔을 때 
가령 아래구간에 왔을 때 
7, -3, 4,             8
이전에 들고있던 7을 킵할 것인지
아니면 7이라는 시점부터 계산된 값으로 교체할 것인지를 결정한다.
이때 7이라는 시점부터 계산된 값이 max_check라는 변수에 들어있다.
그래서 둘중 어떤 값을 들고 있을지 판단해서 교체여부를 결정한다.
'''
def sublist_max(profits):
    max_profit_so_far=0
    add_ups = 0

    for i in profits:
        add_ups += i
        add_ups = max( add_ups, i )
        max_profit_so_far = max(max_profit_so_far, add_ups)

    return  max_profit_so_far

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
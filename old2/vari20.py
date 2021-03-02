# - *- coding: utf- 8 - *-

'''
divide and conquer 를 이용한다.

1. base case
리스트 길이가 1 일때는 그 값을 리턴
리스트 길이가 2 일때는 둘로 나누고 좀 더 큰 값을 리턴
리스트 길이가 4 일때는 둘로 나누고

왼쪽과 오른쪽의 최대구간을 구한다.
maxL
maxR

최대구간이 오른쪽에만 있다.
maxR
최대구간이 왼쪽에만 있다.
maxL
최대구간이 겹친다.
maxL+maxR


2. 분할
3. 계산
4. 합치기


'''

def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2      # 중간 인덱스

    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0                  # 왼쪽 누적 수익
    left_max = profits[mid]       # 왼쪽 최고 수익; 왼쪽 반 중 가장 오른쪽 값으로 초기화

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0                 # 오른쪽 누적 수익
    right_max = profits[mid + 1]  # 오른쪽 최고 수익; 오른쪽 반 중 가장 왼쪽 값으로 초기화

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    # 범위에 하나의 항목밖에 없으면, 그 항목을 리턴한다
    if start == end:
        return profits[start]

    # 중간 인덱스
    mid = (start + end) // 2

    # 상황별로 최대 수익을 구한다
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))




# def max_crossing_sum(profits, start, end):
#     # 코드를 작성하세요.
#     mid = (end + start) //2
#
#     maxL=0
#     maxR=0
#
#     sumL=0
#     sumR=0
#
#     for i in range(mid+1):
#         sumL += profits [mid-i]
#         maxL = max(maxL, sumL)
#
#     for i in range (mid+1, end+1):
#         sumR += profits[i]
#         maxR = max(maxR, sumR)
#
#     return maxL + maxR
#
#
# def sublist_max(profits, start, end):
#     # 코드를 작성하세요.
#
#     if start == end :
#         return profits[start]
#
#     mid = (end + start) // 2
#
#     max_left =  sublist_max(profits, start, mid)
#     max_rignt=sublist_max(profits, mid +1 , end)
#     max_mid = sublist_max(profits, start, end)
#
#     return max(max_left,max_rignt,max_mid)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

# list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
# print(sublist_max(list2, 0, len(list2) - 1))
#
# list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
# print(sublist_max(list3, 0, len(list3) - 1))
#
# list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
# print(sublist_max(list4, 0, len(list4) - 1))
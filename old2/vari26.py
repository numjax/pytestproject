# - *- coding: utf- 8 - *-
'''
두 가지의 제약이 있습니다.

O(n)O(n) 이상의 공간을 사용할 수 없습니다. 즉 사전이나 리스트와 같이
인풋 리스트의 길이에 비례하는 공간 저장 도구를 사용할 수 없습니다!


인풋으로 받는 리스트 some_list의 요소들을 바꾸거나 변형할 수 없습니다.

'''
def find_same_number(some_list, start=0, end=0):
    end = len(some_list) - 1
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 코드를 쓰세요
    temp_list = []

    for i in some_list:
        # print(i)
        if i in temp_list:
            return i

        temp_list.append(i)

    return 0

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
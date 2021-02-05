
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index is None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    if start_index > end_index :
        return "None"

    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2
    #print ("mid ",  mid)

    #print ("element ",  element)
    #print("some_list[mid] ", some_list[mid])

    # base case: 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    elif some_list[mid] < element:
        start_index = mid +1

    elif some_list[mid] > element:
        end_index = mid - 1


    #print("start_index ", start_index)
    #print("end_index ", end_index)

    return binary_search(element,some_list, start_index, end_index)






print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))



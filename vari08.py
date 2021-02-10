'''
퀵 정렬
'''

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.

    if start == end :
        return 0

    p = my_list[-1]
    p_idx = len(my_list)-1
    i=0
    b=-1
    while True:

        if my_list[i] > p :
            if b < 0:
                b=i

        else:
            if b >= 0:
                swap_elements(my_list, i, b)
                b += 1

        i+=1
        if i == p_idx :
            swap_elements(my_list, i, b)
            return b




# 테스트 1

list1 = [4, 3, 6, 2, 7, 1, 5]

pivot_index1 = partition(list1, 0, len(list1) - 1)

print(list1)

print(pivot_index1)


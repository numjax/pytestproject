# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list


# 이전 과제에서 작성한 코드를 붙여 넣으세요!


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




# 퀵 정렬
def quicksort(my_list, start, end):

    if start == end :
        return

    quicksort(my_list, start, partition(my_list, start,end)-1)

    quicksort(my_list, partition(my_list, start, end)+1, end)


# 코드를 작성하세요.




# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
print (quicksort(list3, 0, len(list3) - 1))
print(list3)
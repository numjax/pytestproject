def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    # 코드를 작성하세요.
    if len(list1) == 0 and len(list2) > 0:
        return list2

    if len(list1) > 0 and len(list2) == 0:
        return list1

    if len(list1) == 0 and len(list2) == 0:
        return

    merged_list = []
    i = 0
    j = 0

    while True:

        if i == len(list1) and j == len(list2) :
            return merged_list

        elif i == len(list1):
            merged_list.append(list2[j])
            j += 1

        elif j == len(list2):
            merged_list.append(list1[i])
            i += 1

        else:
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1



# 합병 정렬
def merge_sort(my_list):

    # 코드를 입력하세요.
    if len(my_list) <= 1:
        return my_list
    else:
        return merge(merge_sort(my_list[:len(my_list)//2]), merge_sort(my_list[len(my_list)//2:]))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

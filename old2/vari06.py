def merge(list1, list2):
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



# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
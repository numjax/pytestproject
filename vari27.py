# - *- coding: utf- 8 - *-

def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요


    #brute force
    # for i in sorted_list:
    #
    #     for j in sorted_list[::-1]:
    #         if i + j == search_sum :
    #             return True
    #
    # return False


    #binary search
    # for i in sorted_list:
    #     target = search_sum - i
    #
    #     st = 0
    #     ed = len(sorted_list) - 1
    #     while st<=ed:
    #         #가운데 값을 가져온다.
    #         mid_idx =(st + ed) // 2
    #         mid_value = sorted_list[mid_idx]
    #
    #         # print(mid_idx)
    #         # print(mid_value)
    #
    #         if mid_value == target:
    #             return True
    #         elif target > mid_value:
    #             st = mid_idx + 1
    #         else:
    #             ed = mid_idx - 1
    #
    # return False


    #sorted된 리스트를 활용
    left_idx = 0

    right_idx = len(sorted_list)-1

    while left_idx < right_idx:

        left = sorted_list[left_idx]
        right = sorted_list[right_idx]

        if left+right == search_sum :
            return True
        elif left+right < search_sum :
            left_idx += 1
        else:
            right_idx -= 1

    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
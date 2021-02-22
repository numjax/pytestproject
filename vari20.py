# - *- coding: utf- 8 - *-

def find_same_number(some_list):
    # 코드를 쓰세요
    # O(n)에 처리하도록?
    dup_list = [0] * (len(some_list) +1)
    #print (dup_list)

    for i in some_list:
        #print(i)
        dup_list[i] += 1
        #print (dup_list)
        if dup_list[i] >= 2:
            return i

    return 0


# 중복되는 수 ‘하나’만 리턴합니다.

print(find_same_number([1, 1, 3, 5, 3, 2]))
#print(find_same_number([1, 4, 3, 5, 3, 2]))
#print(find_same_number([4, 1, 5, 2, 3, 5]))
#print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

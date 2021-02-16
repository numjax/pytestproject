# - *- coding: utf- 8 - *-

def max_product(card_lists):
    # 코드를 작성하세요.
    maxi =1

    for i in card_lists:
        i.sort()
        maxi = maxi * i[-1]

    return maxi



# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))


''''''''

def min_fee(pages_to_print):
    # 코드를 작성하세요.
    pages_to_print.sort()

    fee = 0
    acc = 0

    for i in pages_to_print:
        fee = fee + i
        acc = acc + fee

    return acc


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

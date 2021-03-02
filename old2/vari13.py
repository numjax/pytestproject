# - *- coding: utf- 8 - *-

def max_profit_memo(price_list, count, cache):

    if count<2:
        cache[count]= price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    mid = count//2

    sum = []
    sum.append(0)

    for i in range(1, mid+1):
        sum.append(max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache))


    if count <= len(price_list)-1 :
        sum.append(price_list[count])

    maxi = 0
    for i in sum:
        if i > maxi:
            maxi = i

    cache[count] = maxi

    return cache[count]

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

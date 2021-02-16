# - *- coding: utf- 8 - *-

def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    default_coin_list.sort()

    i=-1
    count =0

    while True:

        if value >= default_coin_list [i]:

            value = value - default_coin_list [i]

            count += 1
        else:
            i = i - 1


        if value == 0 :
            return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
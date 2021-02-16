# - *- coding: utf- 8 - *-


def max_profit(price_list, count):
    # 코드를 작성하세요.
    # 타뷸레이션 방식

    profit_table = [0]
    maxi = 0

    if count ==0:
        return 0


    for i in range(1, count+1):
        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다


        if i < len(price_list):
            maxi = price_list[i]
        else:
            maxi = 0

        for j in range (1, i//2 + 1):
           maxi = max(maxi, profit_table[j] + profit_table[i - j])


        # 가능한 최대 수익을 profit_table에 넣는다
        profit_table.append(maxi)

    return profit_table[count]

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

# - *- coding: utf- 8 - *-


'''
지금까지의 가장 큰 수익을 가지는 변수
위의 때 부터 이후 상황을 계산하는 변수
'''
def max_profit(stock_list):

    if len(stock_list) < 2:
        return 0


    if len(stock_list) == 2:
        return stock_list[1] - stock_list[0]



    max_profit_so_far = -100
    add_ups = 0
    prev = stock_list[0]
    gap = 0

    for i in stock_list[1:]:
        gap =  i-prev #-1
        prev = i  # 6
        add_ups += gap # -1
        add_ups = max(add_ups, gap)
        #print (add_ups)
        max_profit_so_far =max(max_profit_so_far, add_ups)

    return  max_profit_so_far



print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
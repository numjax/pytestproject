# - *- coding: utf- 8 - *-

def trapping_rain(buildings):

    left_max_list =[buildings[0]]
    for i in range(1,len(buildings)):
        left_max_list.append(0)
        left_max_list[i]=max(buildings[i], left_max_list[i-1])


    right_max_list =[buildings[len(buildings)-1]]
    for i in range(len(buildings)-2, -1, -1):
        right_max_list.append(0)
        right_max_list[len(buildings)-1-i]=max(buildings[i], right_max_list[len(buildings)-1-i-1])

    right_max_list.reverse()
    # print(left_max_list)
    # print(right_max_list)

    total = 0
    for i in range(len(buildings)-1):
        calc =   min(left_max_list[i], right_max_list[i]) - buildings[i]
        # print (calc)
        total += calc

    return total



print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# - *- coding: utf- 8 - *-
def course_selection(course_list):
    # 코드를 작성하세요.
    course_selected=[(0,0)]

    mini_tuple = ()
    avail = (0,999)

    mini = 999
    for k in range(len(course_list)):

        for i in course_list:
            for j in course_selected:
                if j[0] <  i[0]  < j[1]  or  j[0] <  i[1]  < j[1]:
                    avail = (0,999)
                    break

                if j[0] <  i[0]  < j[1]  and  j[0] <  i[1]  < j[1]:
                    avail = (0,999)
                    break

                if j[0] >=  i[0]  and j[1] <= i[1]:
                    avail = (0,999)
                    break

                avail =i

            if avail[1] < mini:
                mini = i[1]
                mini_tuple = i

        if mini < 999:
            course_selected.append(mini_tuple)
            course_list.remove(mini_tuple)

            print("mini_tuple: ",mini_tuple)
            print(course_list)
            print(course_selected)
            print("")



        mini = 999

    course_selected.remove((0,0))

    return (course_selected)

print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))

print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

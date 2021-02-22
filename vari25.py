# - *- coding: utf- 8 - *-

# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    cnt = [1,1]

    for height in range(2,stairs+1):
        cnt.append(0)

        for step in possible_steps:
            if height - step >= 0:
                cnt[height] += cnt[height-step]


    return cnt[stairs]





print(staircase(3, [1, 2, 3]))
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))


'''
4
13
24
31
19
'''
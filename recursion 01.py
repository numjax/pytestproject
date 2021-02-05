
def changeCounterIdx(amount, idx):
    change = [50 ,25 ,10 ,5 ,1]

    if amount == 0:
        print(1)
    elif amount < 0 or idx >= len(change):
        print(0)
    else:
        print(changeCounterIdx(amount - change[idx], idx) + changeCounterIdx (amount, idx+1))




def changeCounter (amount):

    if amount == 0:
        print ("root" + 1)
    else:
        changeCounterIdx(amount, 0)



# 5가지 종류의 동전으로 거스름돈을 줄 수 있는 경우의 수

#재귀문으로 풀것
#재귀는 분기가 있는 반복문
#선언적 표기

changeCounter(300)


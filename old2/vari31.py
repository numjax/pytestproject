# - *- coding: utf- 8 - *-

def sum(n):
    if n == 1:
        return 1

    return sum(n - 1) + sum(n - 1)


#depth n짜리 2진 트리의 리프노드 갯수 구하기
print(sum(4))




def fib(n):

    if n == 1 or n == 0:
        return 1

    return fib(n-2) + fib(n-1)


print (fib(5))
# - *- coding: utf- 8 - *-


'''
마지막에 1개가 남거나 2개가 남거나
'''


def staircase(n):
    #
    # if n == 0:
    #     return 0
    #
    # if n==1:
    #     return 1
    #
    # if n==2:
    #     return 2
    #
    # return staircase(n-1) + staircase(n-2)

    a, b = 1, 1
    for i in range(n):
        #a, b = b, a + b
        #a와 b의 연산이 동시에 일어남, 즉 a에 b를 대입하기 전의 a값이 a+b에서 사용된다.
        temp = a
        a = b
        b = temp + b
    return a

'''
Doing:

a, b = b, a+b

is equivalent to:

temp = a
a = b
b = temp + b

---------------------------------------------------------------

It lets you simultaneously do two calculations 
without the need of an intermediate/temporary variable.

The difference is that in your second piece of code, 
when you do the second line b = a+b, 
you have already modifed a in the previous line 
which is not the same as the first piece of code.

---------------------------------------------------------------

Examples
>>> a = 2
>>> b = 3
>>> a,b
2 3
>>> a,b = b,a
>>> a,b
3 2

On the other hand, if you use the second approach shown in your question:

>>> a = 2
>>> b = 3
>>> a,b
2 3
>>> a = b
>>> b = a
>>> a,b
3 3
'''
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
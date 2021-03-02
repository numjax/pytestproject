def fib_memo(n, cache):
    # 코드를 작성하세요.
    if n < 3:
        return 1

    #딕셔너리의 키값의 존재유무 판단
    #없는 키로 조회때리면 에러 발생
    if n in cache :
        return cache[n]
    else:
        cache[n-1] = fib_memo(n-1, cache)
        cache[n-2] = fib_memo(n-2, cache)
        return cache[n-1] + cache[n-2]


def fib(n):
    # n번째 피보나치 수를 담는 딕셔너리
    fib_cache = {}
    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

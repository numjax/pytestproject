def max_product(left):
    #brute force
    max = 0

    right = []

    for i in left:
        right.append(i*2)

    for i in left:
        for j in right:
            if max < i*j:
                max = i*j

    return max

# 테스트
print(max_product([1, 6, 5]))



print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
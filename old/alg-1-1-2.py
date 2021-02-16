
def linear_search(element, some_list):
    front = 0
    end = len(some_list)
    while True:
        middle = int ((front + end)/2 )
        if element  == some_list [middle]:
            return middle
        elif element > some_list [middle]:
            front = middle
        elif element < some_list[middle]:
            end = middle

        if front == end :
            return None


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
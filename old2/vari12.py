def fib_optimized(n):

    prevprevMyvalue = 0
    prevMyvalue = 1
    myvalue = 0

    if n ==0 :
        return 0

    if n == 1:
        return 1


    for i in range(n-1):

        # print ("-2",prevprevMyvalue)
        # print ("-1", prevMyvalue )
        myvalue = prevMyvalue + prevprevMyvalue
        prevprevMyvalue = prevMyvalue
        prevMyvalue = myvalue


        # print ("myval: ", myvalue)


    return myvalue

print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))


def countPrimes(n):

    lst = list(range(4, n))
    # print(lst)


    nonprime = set()

    if n in range(0, 3):
        return 0
    if n == 3:
        return 1

    for value in lst:
        # print("the value is:",value)
        i = 2
        while i * i <= value:
            # print("i is:",i)
            if value % i == 0:
                nonprime.add(value)
                # print("it is not prime")
            i += 1


    # print(nonprime)
    return (n-len(nonprime)-2)

    # i = 0
    # for value in lst:
    #     if value in nonprime:
    #         i += 1
    #
    # return((n-i)-2)
    # # print("number of primes", (n-i)-2)

print(countPrimes(10000))
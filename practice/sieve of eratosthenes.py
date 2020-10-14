# import math
#
#
# # sieve of eratosthenes, input a number, find all primes using the SoE.
#
# def sieve(n):
#     # generates a list based on the input number n.
#     lst = list(range(1, n))
#     print(lst)
#     # The largest prime multiple required by SoE is the floor of sqrt(n)
#     prime = math.floor(n ** 0.5)
#     # the first prime is 2, remove all multiple of 2s
#     primelst = []
#     for x in lst:
#
#         # want to remove all multiples of 2, except 2
#         if x == 2 or x % 2 != 0:
#             primelst.append(x)
#
#
#
#     print(primelst)
#
#
# sieve(50)

# def sieve(n):
#     primelst = []
#     for i in range(2, n+1):
#         if i not in primelst:
#             print(i)
#             for j in range(i*i, n+1, i):
#                 primelst.append(j)
#
# sieve(10)
def sieve(n):
    primelst = []
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primelst.append(i)
    print(primelst)
    print(list(enumerate(primelst)))

sieve(100)
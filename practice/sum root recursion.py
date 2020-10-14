def sumroot(n):
    n = str(n)
    lst = [int(x) for x in n]
    print(lst)
    sum = 0


    for i in range(0, len(lst)):
        sum += lst[i]
    print("the sum is: ", sum)

    if sum > 9:
        return sumroot(sum)
    return sum

n = 942

print("answer", sumroot(n))
print("orig value", n)

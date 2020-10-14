def josephus_survivor(n, k):
    last = 0
    arr = list(range(1, n + 1))

    if k == 1:
        return n

    while len(arr) > 1:
        newarr = []
        for i in range(len(arr)):
            if (i + 1 + last) % k != 0:
                newarr.append(arr[i])
        last += len(arr)
        arr = newarr

    return arr[0]

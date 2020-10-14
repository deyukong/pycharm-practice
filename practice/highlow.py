def high_and_low(numbers):
    # ...
    lst = numbers.split( )
    print(lst)

    max = int(lst[0])
    min = int(lst[0])

    for n in lst:
        if int(n) > max:
            max = int(n)
        elif int(n) < min:
            min = int(n)

    return str(max) +" "+ str(min)


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))


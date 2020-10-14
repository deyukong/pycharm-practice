lst = [1, 1, 1, 0, 0, 0, 2, -2, -2]
nodup = []

lst.sort()
print(lst)

min = lst[0]

#strip the array of dups
for x in lst:
    if x not in nodup:
        nodup.append(x)
print(nodup)

if len(nodup) == 1:
    print("there is no second min or max")
else:
    print("the second min is: ", nodup[1])
    print("the second min is: ", nodup[-2])
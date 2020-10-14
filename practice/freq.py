import collections
lst = [10,10,10,10,20,20,20,20,40,40,50,50,30]

print("original list is {}".format(lst))

ctr = collections.Counter(lst)
print("the frequency of elements in the list: ", ctr)
ctrdict = dict(ctr)
print(ctrdict)
print(len(ctrdict))
for x in ctrdict:
    print(ctrdict[x])
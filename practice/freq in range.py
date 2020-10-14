def freq_range(lst, min, max):
    newlst = [x for x in lst if min <= x <= max]
    print("the new list is: ", newlst)

    return(len(newlst))

# lst = [10,20,30,40,40,40,70,80,99]
# print(freq_range(lst, 40, 100))

lst = ['a','b','c','d','e','f']
print(freq_range(lst, 'a', 'e'))
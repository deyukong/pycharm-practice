a = [1,9,2,10,3,4,4,3,3,3,3,6]
b = [100, 101, 102]

a.append(100)
print(a)

a.extend(b)
print(a)

a.insert(1, 99)
print(a)

a.remove(100)
print(a)

a.pop(0)
print(a)

print(a.count(3))

a.sort(reverse = True)
print(a)

c = a.copy()
print(c)

a.clear()
print(a)

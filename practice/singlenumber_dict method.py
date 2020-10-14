nums = [4,1,2,1,2]

# create a dictionary and store the key and value
# then look through the dictionary and find the key with the value of 1

dict = {}

for n in nums:
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1

for key, value in dict.items():
    if value == 1:
        print(key)


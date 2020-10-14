# def dirReduc(arr):
#     dir = []
#     for i in range(0, len(arr)-1):
#
#         if arr[i] == "NORTH" and arr[i+1] != "SOUTH" or arr[i] == "SOUTH" and arr[i+1] != "NORTH":
#             dir.append(arr[i])
#         elif arr[i] == "EAST" and arr[i+1] != "WEST" or arr[i] == "WEST" and arr[i+1] != "EAST":
#             dir.append(arr[i])
#     print(dir)


#code found onlien, smart.
def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
        # if res means if there are values in there
        # the condition above basically says if res is not empty and the inverse is equal to the last value of res
            res.pop
        else:
            res.append(i)
    return res

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))

dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}

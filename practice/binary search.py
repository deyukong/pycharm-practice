

def binary_search(input_array, value):

    n = len(input_array)
    left = 0
    right = n - 1

    while left <= right:
        mid = int((right + left) / 2)
        median = input_array[mid]
        if value > median:
            left = mid+1
        elif value < median:
            right = mid-1
        else:
            return mid

    return -1

test_list = [1,3,9,15]
test_val1 = 46
print(binary_search(test_list, test_val1))

# Gavin's implementation
# def search(self, nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#     while left < right:
#         mid = int((left + right) / 2 + 1)
#         if target >= nums[mid]:
#             left = mid
#         else:
#             right = mid - 1
#     if nums[left] == target:
#         return left;
#     return -1
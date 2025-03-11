nums = [3, 0, 1, 4, 2]

def missingNumber(arr):
    res = len(arr)
    for i in range(len(arr)):
        res += (i - nums[i])
    return res

print(missingNumber(nums))

# alternative

def missingNumber_2(arr):
    n = len(arr)
    res = n
    for i in range(n):
        res ^= i
        res ^= arr[i]
    return res

print(missingNumber_2(nums))

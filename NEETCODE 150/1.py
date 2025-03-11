nums = [2, 7, 11, 15]
t = 9

def twoSum(arr, target):
    arr_map = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in arr_map:
            return [arr_map[complement] , i]
        arr_map[arr[i]] = i
    return []

print(twoSum(nums, t))
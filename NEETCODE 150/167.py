# twoSum using two pointers

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        temp_sum = numbers[l] + numbers[r]
        if temp_sum > target:
            r -= 1
        elif temp_sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []
            
print(twoSum([2,7,11,15], 9))
def twoSum(nums, target):
    hashmap = {} 
    
    for i, num in enumerate(nums):
        complement = target - num  
        
        if complement in hashmap: 
            return [hashmap[complement], i]  
        
        hashmap[num] = i
    
    return [] 
print(twoSum([3, 2, 2, 3], 6))
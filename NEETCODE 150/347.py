def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for i in range(len(nums)):
        if nums[i] in count :
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1
    res = []
    for key, value in count.items():
        freq[value].append(key)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
print(topKFrequent([1, 2, 3, 4, 5, 6], 6))
def groupAnagrams(arr):
    res = {}
    for i in arr:
        sorted_i = "".join(sorted(i))
        if sorted_i in res:
            res[sorted_i].append(i)
        else:
            res[sorted_i] = [i]
    return list(res.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def groupAnagrams_2(arr):
    res = {}
    for i in range(len(arr)):
        sorted_i = "".join(sorted(i))
        if sorted_i in res:
            res[sorted_i].append(i)
        else:
            res[sorted_i] = [i]
    return list(res.values())
           
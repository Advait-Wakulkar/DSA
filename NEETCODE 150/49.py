def groupAnagrams(arr):
    res = {}
    for i in arr:
        print("i",i)
        print("sorted i", sorted(i))
        sorted_i = "".join(sorted(i))
        print("print sorted_i", sorted_i)
        if sorted_i in res:
            res[sorted_i].append(i)
        else:
            res[sorted_i] = [i]
    return list(res.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
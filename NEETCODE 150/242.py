a = "anagram"
b = "nagaram"

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    else : 
        str_map, str_map_2 = {}, {}
        for i in s:
            if i in str_map:
                str_map[i] += 1
            else:
                str_map[i] = 1
        for j in t:
            if j in str_map_2:
                str_map_2[j] += 1
            else:
                str_map_2[j] = 1
        return (str_map == str_map_2)

print(validAnagram(a, b))
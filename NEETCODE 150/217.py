nums = [1, 2, 3, 1]

def containsDuplicate(arr):
    arr_set = set()
    for i in arr:
        if i in arr_set:
            return True
        else : 
            arr_set.add(i)
    return False

print(containsDuplicate(nums))
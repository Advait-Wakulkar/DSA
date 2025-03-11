nums = [4, 3, 2, 7, 8, 2, 3, 1]

def findAllNumbersDisappearedInArray(arr):
    n = len(arr)
    for i in range(n):
        index = abs(arr[i]) - 1
        if arr[index] > 0:
            arr[index] *= (-1)
    res = []
    for i in range(n):
        if arr[i] > 0:
            res.append(i + 1)
    return res


print(findAllNumbersDisappearedInArray(nums))
 
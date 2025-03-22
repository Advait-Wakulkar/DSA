# 1 Converging Pointers for example palindrom
#Template
toCheck = "abcdecba"

def checkPalindrome(str_):
    l, r = 0 , len(toCheck)-1
    while r > l:
        if toCheck[l] == toCheck[r]:
            l += 1
            r -= 1
        else :
            return False
    return True

print(checkPalindrome(toCheck))


# 2 Parallel Pointers example Sliding Window
# two types fixed sliding window and dynamic window
#for fixe sliding windows examples find subarrays or substrings of a fixed length
# Template for fixed sliding window for maximum sum of substrings with a given window
# we first calculate the sum of the first window of size k

def fixedSlidingWindow(arr, k):
    n = len(arr)
    window_sum = 0

    if n < k:
        return 0

    for i in range(k):
        window_sum += arr[i]

    max_result = window_sum
    
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_result = max(max_result, window_sum)
    return max_result

print(fixedSlidingWindow([5, 3, 1, -4, 7, 9], 4))


# Dynamic Sliding Window examples find longest/shortes subarray/substring 
# that satisfies a condition

def dynamicSlidingWindow(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
        
    n = len(arr)
    window_sum = sum(arr[:k])  # Sum of first k elements
    max_sum = window_sum
    
    for i in range(k, n):
        # Add the new element and remove the element leaving the window
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

print(dynamicSlidingWindow([5, 3, 1, -4, 7, 9], 3))  # k=3 will find max sum of 3 consecutive elements

'''
You are given a sorted array consiting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appear only once:
Your solution must run in O(logN) time and O(1) space

example 1:
input: nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
output: 2

example 2:
input: nums = [3, 3, 7, 7, 10, 11, 11]
output: 10

the trick here is the runtime: O(logN)

I: a list of nums, with 1 single digit, so length is odd
O: the single digit
C: O(logN) runtime
E: a list with 1 number [1]

if you are returning from inside the loop, use left <= right, like the binary search
if you are reducing the search space, use left < right and finally return a[left]
'''

def singleNonDuplicate(nums):
    low = 0
    hi = len(nums) - 1

    while low < hi:
        mid = low + (hi - low) // 2
        is_right_haft_even = (hi - mid) % 2 == 0

        # mid partner to the right of mid
        if nums[mid] == nums[mid + 1]:
            if is_right_haft_even:
                low = mid + 2
            else:
                hi = mid - 1

        # mid partner to the left of mid
        elif nums[mid] == nums[mid - 1]:
            if is_right_haft_even:
                hi = mid -2
            else:
                low = mid + 1
        # mid is the single number
        else:
            return nums[mid]

    return nums[low]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))
print(singleNonDuplicate([1]))

'''
runtime: O(logN), for Binary Search
space: O(1)

'''

'''
intuition:
- the single digit is at the even index always
- so every pair before the single digit start with an even index
- every pair after the single digit start with an odd index

'''
def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        if mid % 2 == 1:
            mid -= 1

        # have not seen the single digit yet
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        # already seen the single digit
        # either at mid or before mid
        else:
            high = mid
    return nums[low]


print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(singleNonDuplicate([1]))

'''
runtime: O(log(n/2)) => O(logN)
space: O(1)

'''
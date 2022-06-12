'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index.  Otherwise, return -1:

You must write an algo with O(logN) runtime complexity

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

example 2:
Input: nums = [-1, 0, 3, 5, 9, 12] target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

'''

def search(nums, target):

    def binary_search(start, end):
        if end >= start:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)
        else:
            return -1

    return binary_search(0, len(nums)-1)

print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))

'''
time: O(N)
space: O(N)
for recursive stack, if I dont find it, it will run for n time

'''


def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))

'''
time: O(N)
- a while loop, go through all of them and dont find the result
space: O(1)
- only space for mid, start and end

'''
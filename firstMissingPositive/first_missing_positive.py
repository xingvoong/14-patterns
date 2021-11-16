"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space

Example 1:
Input: nums = [1, 2, 0]
Output: 3

Example 2:
Input: nums = [3, 4, -1, 1]
Output: 2

Example 3:
Input: nums = [7, 8, 9, 11, 12]
Output: 1

I: an array of unsorted integer, with both positive and negative number
O: integer, the smallest missing positive integer
C: time: O(n), space: O(1)
1 <= nums.length <= 5 * 10 ^ 5

E:
Hint 1:
"""


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    hash_map = {}
    for i in range(1, n + 1):
        hash_map[i] = False

    for j in nums:
        if j in hash_map:
            hash_map[j] = True

    for k in hash_map.keys():
        if not hash_map[k]:
            return k

    return k + 1


def test():
    inputs = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1]]
    expected = [3, 2, 1, 2]

    count = 0
    for i in range(len(inputs)):
        actual = firstMissingPositive(inputs[i])
        if actual != expected[i]:
            print("Wrong at input: {count}").format(count=count)
            temp = expected[i]
            print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
            return
        count += 1

    print("Passed test")


test()

"""
Complexity Analysis:

runtime:
O(N) to build a hashmap
O(N) to change hashmap to truth and false
O(N) to check whether an entry is in the hashmap
=> total: O(N)

space: O(N) for hashmap

"""

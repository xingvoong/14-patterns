"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3].  2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0, 1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2].
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0, 9].
8 is the missing number in the range since it does not appear in nums

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique

Follow up: could you implement a solution using only O(1) extra space complexity and O(n)
runtime complexity?
"""

"""
so what if I get the length of nums
so that I know what number I got

- get the range
- build a hashmap for looking up
- I can search if the number is in there
- O(N) for the loop, O(1) for loop up
- O(N) for space
how can I do it without extra space?
I swap the number
    [9, 6, 4, 2, 3, 5, 7, 0, 1]
=>  []
 0  1  2  3  4  5  6  7  8
[0, 1, 2, 3, 4, 5, 6, 7, 9]


so the range is always off by one
ok, so it only miss one number


"""


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dictionary = {}
    for i in nums:
        dictionary[i] = True

    for j in range(n + 1):
        if j not in dictionary:
            return j


def test():
    inputs = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [0]]
    expected = [2, 2, 8, 1]
    count = 0
    for i in range(len(inputs)):
        actual = missingNumber(inputs[i])
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
Time: O(N)
O(N) to build a hashmap
O(N) to check j in range n + 1 in dictionary

Space: O(N)
for hashmap

"""
